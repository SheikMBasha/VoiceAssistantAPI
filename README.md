python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate

pip install -r requirements.txt

to run the code:
uvicorn main:app --host 0.0.0.0 --port 8085 --reload


Testing
1. curl -X POST http://localhost:8085/loan_balance -H "Content-Type: application/json" -d "{\"user_text\": \"How much is my loan balance?\"}"
2. curl -X POST http://localhost:8085/balance_enquiry -H "Content-Type: application/json" -d "{\"user_text\": \"What is my account balance?\"}"
3. curl -X POST http://localhost:8085/loan_status -H "Content-Type: application/json" -d "{\"user_text\": \"What is the status of my loan application?\"}"
