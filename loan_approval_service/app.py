from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from models import LoanApplication

mongo_uri = "mongodb+srv://sriramkiran:12345@cluster0.osquyjl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Access the database
db = client.get_database("loan_applications_db")

# Access a collection
loan_applications_collection = db.get_collection("loan_applications")

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb+srv://sriramkiran:12345@cluster0.osquyjl.mongodb.net/?retryWrites=true&w=majority'
mongo = PyMongo(app)

# MongoDB collection for LoanApplications
loan_applications_collection = db.get_collection("loan_applications")

class LoanApplication:
    def __init__(self, applicant_name, credit_score, loan_amount, loan_purpose, income, employment_status):
        self.applicant_name = applicant_name
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.loan_purpose = loan_purpose
        self.income = income
        self.employment_status = employment_status
        self.risk_score = None
        self.approval_status = None

@app.route('/loan-application', methods=['POST'])
def submit_loan_application():
    try:
        data = request.get_json()

        # Extract data from JSON
        applicant_name = data.get('applicant_name')
        credit_score = int(data.get('credit_score'))
        loan_amount = float(data.get('loan_amount'))
        loan_purpose = data.get('loan_purpose')
        income = float(data.get('income'))
        employment_status = data.get('employment_status')

        # Create a LoanApplication object
        loan_application = LoanApplication(
            applicant_name=applicant_name,
            credit_score=credit_score,
            loan_amount=loan_amount,
            loan_purpose=loan_purpose,
            income=income,
            employment_status=employment_status
        )

        # Save to MongoDB
        loan_applications_collection.insert_one({
            'applicant_name': loan_application.applicant_name,
            'credit_score': loan_application.credit_score,
            'loan_amount': loan_application.loan_amount,
            'loan_purpose': loan_application.loan_purpose,
            'income': loan_application.income,
            'employment_status': loan_application.employment_status,
            'risk_score': None,
            'approval_status': None
        })

        return jsonify({'status': 'Loan application submitted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)