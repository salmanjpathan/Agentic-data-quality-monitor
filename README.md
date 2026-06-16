# Agentic Data Quality Monitoring System

## Overview

This project demonstrates an end-to-end Agentic Data Quality Monitoring System built using Databricks, PySpark, LangGraph, and Ollama (Llama 3.2).

The system follows the Medallion Architecture (Bronze, Silver, Gold), performs automated data quality checks, classifies issue severity, generates AI-powered business impact reports, and triggers alerts for critical data quality incidents.

---

## Architecture

Customer Data
↓
Bronze Layer
↓
Silver Layer
↓
Gold Layer
↓
Data Quality Checks
↓
dq_results.json
↓
LangGraph Agent
↓
Llama 3.2 (Ollama)
↓
AI Report Generation
↓
Alert Generation

---

## Tech Stack

* Databricks Free Edition
* PySpark
* Python
* LangGraph
* LangChain
* Ollama
* Llama 3.2
* Git
* GitHub

---

## Features

### Data Engineering

* Bronze Layer for raw data ingestion
* Silver Layer for data cleansing and standardization
* Gold Layer for business-ready datasets
* Automated data quality validation

### Data Quality Checks

* Null value detection
* Duplicate record detection
* Invalid age detection
* Data quality summary generation

### Agentic AI Workflow

* Severity classification
* AI-powered business impact analysis
* Remediation recommendations
* Alert generation for critical issues

---

## Project Structure

Agentic-Data-Quality-Monitor/

├── agents/

│ ├── dq_agent.py

│ └── langgraph_dq_agent.py

├── quality_checks/

│ └── generate_dq_results.py

├── data/

│ └── dq_results.json

├── main.py

├── requirements.txt

└── README.md

---

## Sample Output

Severity: HIGH

Issues Detected:

* Null Names: 1
* Duplicate Records: 1
* Invalid Ages: 2

Alert Status: TRIGGERED

High severity data quality issues detected.

Immediate investigation required.

---

## How to Run

### 1. Clone Repository

git clone <repository-url>

cd Agentic-Data-Quality-Monitor

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Environment

Windows:

venv\Scripts\activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Run Pipeline

python main.py

---

## Future Enhancements

* Databricks SQL integration
* Automated Slack notifications
* Email alerting
* Schema drift detection
* Anomaly detection using ML models
* Real-time monitoring dashboards

---

## Learning Outcomes

This project demonstrates:

* Data Engineering fundamentals
* Medallion Architecture implementation
* Data Quality Management
* Agentic AI workflows
* LangGraph orchestration
* Local LLM integration using Ollama
* Git and GitHub project management
