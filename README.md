# Expense Management System Documentation

### Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Folder Structure](#folder-structure)
* [Setup Instructions](#setup-instructions)
* [Dependencies](#dependencies)
* [Contact](#contact)

## 1. Project Overview

The Expense Management System is a comprehensive application designed to track, manage, and analyze personal or business expenses. The system is built with a modern architecture that separates frontend and backend components:

- **Frontend**: A user-friendly Streamlit web application that provides intuitive interfaces for expense entry, data visualization, and reporting.
- **Backend**: A FastAPI-based RESTful API service that handles data processing, storage, and retrieval from a MySQL database.

This system allows users to record expenses by date, categorize them, add notes, and generate analytical reports to understand spending patterns over time and across different categories.

## 2. Features

### UI Features

- **Multi-tab Interface**: The application is organized into four main tabs for different functionalities:
  - Add/Update: For entering and modifying expense data by date
  - Analytics By Category: For visualizing expense distribution across categories
  - Analytics By Month: For tracking monthly spending patterns
  - Expense Data: For viewing all recorded expenses in tabular format
- **Data Entry**: User-friendly forms with date selection, amount input, category dropdown, and notes field
- **Data Visualization**: 
  - Bar charts showing expense breakdown by category with percentage distribution
  - Monthly expense trends with total amounts
  - Sortable tables with formatted values
- **Responsive Design**: The interface is designed with a wide layout for optimal data presentation

### Backend Features

- **RESTful API**: Well-structured endpoints for all data operations
- **Database Operations**:
  - Create, read, update, and delete expense records
  - Query expenses by date range
  - Generate categorical and monthly expense summaries
- **Data Processing**:
  - Calculation of expense percentages by category
  - Aggregation of expenses by month
  - Sorting and formatting of analytical data
- **Error Handling**: Comprehensive error handling with HTTP status codes and detailed error messages
- **Logging**: Detailed logging of database operations for debugging and auditing

## 3. Folder Structure

### Project Root
- **Backend/**: Contains all server-side code and API implementation
  - `server.py`: Main FastAPI application entry point
  - `db_helper.py`: Database connection and query functions
  - `logging_setup.py`: Logging configuration
  - `requirements.txt`: Backend dependencies
  - `server.log`: API operation logs

- **Frontend/**: Contains all client-side Streamlit application code
  - `app.py`: Main Streamlit application entry point
  - `add_or_update_ui.py`: UI components for adding/editing expenses
  - `analytics_category_ui.py`: Category-based analytics visualization
  - `analytics_month_ui.py`: Monthly analytics visualization
  - `data_ui.py`: Data table display components

- **Tests/**: Contains test suites for backend and frontend components
  - `conftest.py`: Pytest configuration and fixtures
  - **Backend/**: Backend-specific tests
    - `test_db_helper.py`: Database helper function tests
- **README.md**: Quick start guide and project overview
- **.gitignore**: Git version control exclusion patterns

## 4. Setup Instructions

1. **Database Setup**:
   - Install MySQL server
   - Create a database named `expense_manager`
   - Configure the database connection in `Backend/db_helper.py` with your credentials

2. **Backend Setup**:
   - Navigate to the Backend directory
   - Install required dependencies: `pip install -r requirements.txt`
   - Start the FastAPI server: `uvicorn server:app --reload`
   - The API will be available at http://localhost:8000

3. **Frontend Setup**:
   - Navigate to the Frontend directory
   - Install required dependencies (if not already installed with backend requirements)
   - Start the Streamlit app: `streamlit run app.py`
   - The web interface will be available at http://localhost:8501

## 4. Dependencies

### Backend Dependencies
- fastapi==0.115.12: Modern, fast web framework for building APIs
- pydantic==2.11.3: Data validation and settings management
- uvicorn==0.34.0: ASGI server for FastAPI
- mysql-connector-python==9.2.0: MySQL database connector
- pandas==2.2.3: Data manipulation and analysis
- requests==2.32.3: HTTP library for API calls
- pytest==8.3.5: Testing framework

### Frontend Dependencies
- streamlit==1.44.1: Web application framework for data apps
- pandas: Data manipulation and visualization
- requests: HTTP client for API communication

### System Requirements
- Python 3.13 or higher
- MySQL Server

## Contact

- Linkedin Post: 
