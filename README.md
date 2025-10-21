# BME 547: Biomedical Software Design

Coursework repository demonstrating foundational biomedical software engineering principles and Python development practices.

## Project Overview

This repository contains implementations developed as part of BME 547, focusing on healthcare data processing, API development, and software testing methodologies.

## Key Components

### Blood Analysis System
- **Cholesterol Classification**: Automated HDL, LDL, and total cholesterol analysis with clinical threshold categorization
- **Interactive CLI**: Command-line interface for blood test result interpretation
- **RESTful API**: Flask-based web service for remote blood test analysis

### Patient Data Management
- Patient record database with structured data storage (name, ID, age, test results)
- JSON-based data serialization and retrieval

### Clinical Calculations
- **Weight Conversion**: Multi-unit weight parser with kg/lb conversion
- **Pediatric Dosing**: First-day medication dosing calculator for common pediatric conditions

### Software Engineering Practices
- Unit testing with pytest and parametrized test cases
- HTTP client-server architecture implementation
- Logging and error handling
- Code style compliance (PEP 8)

## Technologies

- Python 3
- Flask (REST API framework)
- pytest (testing framework)
- requests (HTTP client library)

## Usage

Set up Python virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the Flask server (enables remote blood test analysis via HTTP API):
```bash
python3 server.py
```

Run blood calculator interface (interactive command-line tool for cholesterol classification):
```bash
python3 blood_calculator.py
```

Execute test suite (runs unit tests with pytest):
```bash
pytest
```
