# 🧾 Receipt Verification API

A modular, scalable backend API for verifying in-app purchase receipts from **Apple App Store** and **Google Play** — built with Flask and SQLite.

> 🔧 Designed to simulate a real-world microservice used in mobile gaming environments for processing millions of receipts with idempotency, reliability, and resilience.

---

## 📌 Why This Project Exists

This project was built as part of a backend systems design challenge, reflecting real business requirements from my work in mobile game publishing. It demonstrates how to:

- Structure backend code for **clean scalability**
- Handle **external third-party API integrations** (e.g., Apple/Google receipt verification)
- Ensure **data consistency and idempotency**
- Design APIs for **robust error handling**
- Incorporate **unit testing and deployment readiness**

It’s intended to be used as both:
1. A technical proof-of-concept, and
2. A foundation for production-grade backend service.

---

## 🏗️ Features

- ✅ Flask-based REST API
- ✅ Class-based platform-specific receipt handling (`AppleReceipt`, `GoogleReceipt`)
- ✅ Input validation & receipt platform routing
- ✅ Duplicate receipt prevention using DB constraints and pre-checks
- ✅ Support for both **SQLite** (for quick testing) and **MySQL** (for production)
- ✅ Fully testable with **Pytest**
- ✅ Easily extendable to include async queueing (Celery, SQS, etc.)

---

## 🧠 Architectural Decisions

- **OOP** was used to encapsulate platform differences (via `baseReceipt.py`)
- **Idempotency** is enforced by checking and inserting with uniqueness constraints (`receipt_id`)
- **Extensibility**: The `verify()` methods are mocked for now, but are structured to call 3rd-party APIs with retry/backoff strategies in production
- **Resilience**: In a real-world scenario, failures from Apple/Google could be queued or logged and retried later without affecting live traffic

---

## 🧪 Tech Stack

| Component | Description |
|----------|-------------|
| **Flask** | Lightweight Python web framework |
| **SQLite** | Persistent storage with support for unique constraints |
| **Pytest** | Python testing framework for API logic |
| **Python OOP** | For clean encapsulation and scalability |

---

## 🚀 Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/receipt-verification-api.git
cd receipt-verification-api
pip install -r requirements.txt
python app.py
