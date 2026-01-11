# DevOps Python Practice Assignment

## Overview
This repository contains solutions to a DevOps-oriented Python assignment covering:
- Password security validation
- CPU health monitoring
- Configuration management with MongoDB backend
- Automated backup scripting

## Project Structure
```
devops-python-assignment/
├── Q1_password/
│   └── password_checker.py
├── Q2_cpu/
│   └── cpu_monitor.py
├── Q3_config/
│   ├── config.ini
│   └── config_parser.py
├── Q4_backup/
│   └── backup.py
├── venv/
└── README.md
```

## Q1 – Password Strength Checker
Validates passwords based on:
- Minimum 8 characters
- Uppercase and lowercase letters
- At least one digit
- At least one special character (!@#$%)

Run:
```
cd Q1_password
python3 password_checker.py
```

## Q2 – CPU Monitoring
Continuously monitors CPU usage and raises an alert when usage exceeds 80%.

Run:
```
cd Q2_cpu
python3 cpu_monitor.py
```

## Q3 – Configuration Management using MongoDB
Reads `config.ini`, converts it to JSON, stores it in MongoDB, and exposes it via a REST API.

### Run
```
cd Q3_config
python3 config_parser.py
```

### Fetch Data
```
curl http://localhost:5000/config
```

Data is stored in MongoDB database `devops_config` and collection `configs`.

## Q4 – Backup Automation
Copies files from a source directory to a destination directory, appending timestamps to avoid overwrites.

Run:
```
cd Q4_backup
python3 backup.py /path/to/source /path/to/destination
```

## DevOps Concepts Demonstrated
- Security and validation
- System monitoring
- Configuration management
- Database-backed APIs
- Backup and recovery

## Submission
This repository contains all code and documentation required for evaluation.
