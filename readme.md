# Loan Approval System

A simplified, scalable loan approval system that evaluates loan applications, calculates the risk of lending, and approves or rejects applications based on predefined criteria. The system can handle a high volume of loan applications, is easily maintainable, and allows for the addition of new features.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Applications](#running-the-applications)
- [Endpoints](#endpoints)

## Features

- **Loan Application Service**: Accepts and stores loan applications with applicant information.
- **Risk Assessment Service**: Evaluates loan applications, calculates risk scores, and updates the database.
- **RESTful API**: Exposes endpoints for submitting loan applications, assessing risk, and retrieving loan statuses.
- **MongoDB Database**: Stores loan applications and their statuses.
- **Logging and Monitoring**: Implements logging mechanisms to track events and errors.
- **Unit and Integration Tests**: Validates the functionality and performance of the system.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [MongoDB](https://www.mongodb.com/try/download/community) (installed and running)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/loan-approval-system.git
   cd loan-approval-system

### Install dependencies
    ```bash
    pip install -r requirements.txt


### Running the Application
*The application consists of three main components : Loan_application_service, risk_assessment_service and risk_approval

## Start the Loan application Service
    ```bash```
    cd loan_application_service
    python app.py

### Endpoints

The service will be accessible at http://127.0.0.1:5000/.

1.open Postman and paste address in POST method by this address which is the enpoint http://127.0.0.1:5000/loan-application
in Body select 'raw' and 'json' and paste the customer details and post they will store in mongodb in loan_application_db

*customer details Example :

{
  "applicant_name": "Joseph",
  "credit_score": 750,
  "loan_amount": 50000.0,
  "loan_purpose": "Home Improvement",
  "income": 75000.0,
  "employment_status": "Employed"
}

it will store in mongodb as :

{"_id":{"$oid":"65aa721bcdd2add14f37666a"},"applicant_name":"John Doe","credit_score":{"$numberInt":"500"},"loan_amount":{"$numberDouble":"50000.0"},"loan_purpose":"Home Improvement","income":{"$numberDouble":"75000.0"},"employment_status":"Employed","risk_score":{"$numberDouble":None},"approval_status":None}

### Start the RIsk Assessment Service
    ```bash```
    cd risk_assessment_service
    python app.py
The service will be accessible at http://127.0.0.1:5000/.

    http://127.0.0.1:5000/assess-risk/{loan_id}

1.POST /assess-risk/{loan_id}: Assess the risk for a specific loan application.

2.POST /approve-loan/{loan_id}: Approve or reject a loan application.

3.GET /get-loan-status/{loan_id}: Retrieve the status of a loan application.
