# Backend API Failure Analysis

## Overview
Backend API project that manages reports with structured responses, validation, and error handling. The project focuses on request tracing, clean API design, and handling edge cases that commonly cause data inconsistencies.

## Features
- Create and fetch reports
- Input validation for required fields
- Structured JSON responses
- Empty-state and invalid-input handling
- Layered backend structure

## Tech Stack
Python, Flask, REST APIs, JSON

## Architecture
Client → Routes → Service Layer → Data Model

## What I implemented
- Built API endpoints for report creation and retrieval
- Separated route handling from service logic
- Added validation for missing and invalid input
- Returned consistent JSON responses for success and failure cases

## How to run
1. Clone the repository
2. Install dependencies with `pip install -r requirements.txt`
3. Run `python app/app.py`

## Sample Output
See `output_example.json`

## Status
Improved backend prototype with validation and layered structure
