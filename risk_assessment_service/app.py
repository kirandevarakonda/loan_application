# risk_assessment_service/app.py
from flask import Flask, request, jsonify, abort
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId class
from risk_assessment import RiskAssessment  # Import RiskAssessment class

app = Flask(__name__)

mongo_uri = "mongo_uri"
client = MongoClient(mongo_uri)

# Access the database
db = client.get_database("loan_applications_db")

# Access a collection
loan_applications_collection = db.get_collection("loan_applications")

@app.route('/assess-risk/<string:loan_id>', methods=['POST'])
def assess_risk(loan_id):
    # Fetch loan application from MongoDB
    loan_application = loan_applications_collection.find_one({'_id': ObjectId(loan_id)})

    # Check if loan application exists
    if not loan_application:
        abort(404, description="Loan application not found")

    # Use the RiskAssessment class to calculate the risk score
    risk_score = RiskAssessment.calculate_risk_score(loan_application)

    # Update MongoDB with risk score
    loan_applications_collection.update_one(
        {'_id': ObjectId(loan_id)},
        {'$set': {'risk_score': risk_score}}
    )

    return jsonify({'risk_score': risk_score})

#to het loan approval
@app.route('/approve-loan/<string:loan_id>', methods=['POST'])
def approve_loan(loan_id):
    # Fetch loan application from MongoDB
    loan_application = loan_applications_collection.find_one({'_id': ObjectId(loan_id)})

    # Check if loan application exists
    if not loan_application:
        abort(404, description="Loan application not found")

    # Access the risk score from the MongoDB document
    risk_score = loan_application.get('risk_score')

    # Implement your loan approval logic based on the risk score
    # For example, if risk score is below a certain threshold, approve the loan
    if risk_score and risk_score < 0.5:
        approval_status = 'Approved'
    else:
        approval_status = 'Rejected'

    # Update MongoDB with approval status
    loan_applications_collection.update_one(
        {'_id': ObjectId(loan_id)},
        {'$set': {'approval_status': approval_status}}
    )

    return jsonify({'approval_status': approval_status})


#to get loan status
@app.route('/get-loan-status/<string:loan_id>', methods=['GET'])
def get_loan_status(loan_id):
    # Fetch loan application from MongoDB
    loan_application = loan_applications_collection.find_one({'_id': ObjectId(loan_id)})

    # Check if loan application exists
    if not loan_application:
        abort(404, description="Loan application not found")

    # Extract relevant information for response
    response_data = {
        'applicant_name': loan_application.get('applicant_name'),
        'risk_score': loan_application.get('risk_score'),
        'approval_status': loan_application.get('approval_status')
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
