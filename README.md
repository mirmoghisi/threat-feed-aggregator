# 🛡️ Threat Feed Aggregator

A robust, automated DevSecOps utility designed to ingest unstructured network logs, extract valid IPv4 Indicators of Compromise (IoCs) using precision Regular Expressions, and output sanitized data ready for SD-WAN or SASE firewall blocklists.

## 📖 Overview
Enterprise edge gateways and SASE nodes rely on threat intelligence feeds to block malicious traffic. However, raw syslog exports and public threat feeds are often unstructured. Manually parsing these logs for valid IP addresses is time-consuming and introduces critical security risks through human error. 

This tool solves that by providing an automated, test-driven parsing pipeline.

## ✨ Key Features
* **Automated Ingestion:** Reads raw, messy text files or syslog exports.
* **Regex Precision:** Identifies potential IP addresses while ignoring invalid formatting.
* **Mathematical Validation:** Ensures every extracted IP octet falls strictly within the valid `0-255` range (filtering out edge-case errors like `999.888.1.1`).
* **Continuous Integration Ready:** Includes a `pytest` QA suite and a Bash execution wrapper to guarantee reliability before firewall deployment.

## 🏗️ Architecture
```text
[Raw Logs/Feeds] ──> [Bash Orchestrator] ──> [Python Extractor] ──> [Sanitized IoC List]
                                                    │
                                                    v
                                          [Pytest Validation]
```

## 📁 Repository Structure
```text
threat-feed-aggregator/
├── data/                    # Sample unstructured log files
│   └── sample_logs.txt
├── src/                     # Core Python extraction engine
│   ├── __init__.py
│   └── extractor.py         # Regex and validation logic
├── tests/                   # Pytest QA and Compliance suite
│   ├── __init__.py
│   └── test_extractor.py    # Unit tests for the extraction logic
├── main.py                  # Main Python execution script
├── update.sh                # Bash script for streamlined Git updates
└── README.md                # Project documentation
```

## 🚀 Quick Start Guide

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/threat-feed-aggregator.git
cd threat-feed-aggregator
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

### 2. Run the Security Tests
Ensure the extraction logic is flawless before processing real data:
```bash
pytest
```

### 3. Process the Logs
Extract the validated IPs from your sample data:
```bash
python main.py
```

## 🤝 Contributing
This project demonstrates core network automation and DevSecOps principles. Contributions are welcome! Please ensure all new regex logic is fully covered by the `pytest` suite before submitting a pull request.