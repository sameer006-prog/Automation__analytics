from fastapi import FastAPI
import sqlite3
import uvicorn
from pydantic import BaseModel
import requests

app = FastAPI()

class TicketRequest(BaseModel):
    property_id: int
    issue_description: str

def get_ai_urgency_score(description: str) -> int:
    description = description.lower()
    if "water" in description or "fire" in description or "leak" in description:
        return 10
    elif "light" in description or "paint" in description:
        return 2
    else:
        return 5

def trigger_n8n_webhook(ticket_data: dict):
    print(f"\n[n8n SIMULATOR]  EMERGENCY DETECTED!")
    print(f"[n8n SIMULATOR] Sending data to n8n: {ticket_data}")

@app.post("/create-ticket")
async def create_ticket(request: TicketRequest):
    try:
       score = get_ai_urgency_score(request.issue_description)
       if score == 10:
        trigger_n8n_webhook({
            "property_id": request.property_id,
            "issue": request.issue_description,
            "urgency": "IMMEDIATE_ACTION"
        })

        conn = sqlite3.connect('reltix_ops.db')
        cursor = conn.cursor()
        cursor.execute(
        "INSERT INTO tickets (property_id, issue_description, urgency_score, status) VALUES (?, ?, ?, ?)",
        (request.property_id, request.issue_description, score, "New")
        )
        conn.commit()
        conn.close()
        return {"status": "Success", "urgency_assigned": score}
    except sqlite3.Error as e:
        print(f" Database Error: {e}")
        return {"status": "Error", "message": "Database is currently unavailable."}
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {"status": "Error", "message": "An unexpected error occurred."}

# --- THIS IS THE PART YOU WERE MISSING ---
@app.get("/ask-ai")
async def ask_ai_about_data(question: str):
    question = question.lower()
    conn = sqlite3.connect('reltix_ops.db')
    cursor = conn.cursor()

    if "how many" in question and "high" in question:
        cursor.execute("SELECT COUNT(*) FROM tickets WHERE urgency_score >= 8")
        result = cursor.fetchone()[0]
        answer = f"There are currently {result} high-urgency tickets in the system."
    elif "list" in question:
        cursor.execute("SELECT issue_description FROM tickets")
        result = cursor.fetchall()
        answer = f"Current tickets: {result}"
    else:
        answer = "I don't understand. Try: 'How many high urgency tickets?'"

    conn.close()
    return {"ai_answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)