# The-most-basic-projects-in-Python.
I'm new to software development, and I'll share the small projects I've done with you.
This repository will be updated after each project I complete.


### Mini ATM Project
An open-source Mini ATM project developed in Python using basic loops and conditional statements. Feel free to review it for your feedback and contributions.

# Secure Ledger System

A secure, file-based ledger and transaction tracking system built with Python.

## Features
- **Encapsulation & Security:** File path is protected with private attributes and exposed via read-only `@property`.
- **Dynamic File In-Place Updates:** Updates the audit summary header at the top of the file without rewriting the entire ledger using `r+`, `seek(0)`, and `truncate()`.
- **Balance Calculation:** Automatically parses structured income and expense entries (`[TYPE] AMOUNT TL - DESCRIPTION`).
- **Audit Logging:** Dumps formatted audit history directly to the console.

## Usage
Run the script directly:
```bash
python secure_ledger.py
