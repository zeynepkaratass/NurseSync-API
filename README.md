# Overview

NurseSync API is a robust, modern backend service designed for managing nursing tasks, patient administration, medication tracking, and log records. Built with FastAPI, SQLAlchemy, and PostgreSQL (Neon Tech), it provides high-performance, asynchronous endpoints with automated OpenAPI (Swagger) documentation.

## Features

Nurse & Patient Management: Endpoints for fetching nurse profiles and patient details.

Medication Records: System for querying medications and dosages.

Administration Logging: Track which nurse administered what medication to which patient, including dosages and timestamps.

Cloud-Native Database: Fully integrated with serverless PostgreSQL via Neon.tech.

Data Validation: Strict schema validation powered by Pydantic v2.

## Project Structure

nursesync_api/
├── database.py    # Database connection & session setup
├── models.py      # SQLAlchemy ORM database models
├── schemas.py     # Pydantic data validation schemas
├── main.py        # FastAPI app initialization & API endpoints
└── README.md      # Project documentation


## Prerequisites

Python 3.9+

Neon PostgreSQL Account (or any local/remote PostgreSQL instance)

Installation & Setup

Clone the Repository:

git clone https://github.com/your-username/nursesync-api.git
cd nursesync-api


## Create a Virtual Environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


## Install Dependencies:

pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic


## Environment Configuration:
Update DATABASE_URL in database.py with your PostgreSQL Connection String:

DATABASE_URL = "postgresql://user:password@ep-xyz.neon.tech/neondb?sslmode=require"


Run the Application:

uvicorn main:app --reload


## Interactive API Documentation:
Open http://127.0.0.1:8000/docs in your browser to access the Swagger UI.

# Disclaimer & Legal Notice

IMPORTANT: This software is an educational/developmental prototype and is provided "as is", without warranty of any kind, express or implied. It is NOT intended, certified, or compliance-tested for real-world clinical use, medical decision-making, patient diagnosis, or processing live Electronic Health Records (EHR/HIPAA/GDPR data).

The author(s) and contributor(s) assume no legal liability or responsibility for any direct, indirect, incidental, or consequential damages, medical errors, data losses, or regulatory non-compliance resulting from the deployment, testing, or misuse of this software.
