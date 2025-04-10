# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()


class AgentRequest(BaseModel):
    user_text: str
    parameters: Optional[Dict] = {}
    sentiment: Optional[str] = ""


@app.post("/loan_balance")
def loan_balance_handler(data: AgentRequest):
    return {
        "response": "You have a remaining car loan balance of $12,450.67 with 36 payments left."
    }


@app.post("/balance_enquiry")
def balance_enquiry_handler(data: AgentRequest):
    return {
        "response": "Your checking account has $2,543.78 and savings account has $15,689.22."
    }


@app.post("/loan_status")
def loan_status_handler(data: AgentRequest):
    return {
        "response": "Your home loan application submitted 3 days ago is still under review."
    }
