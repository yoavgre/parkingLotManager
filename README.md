# 🚗 Parking Lot Manager API (FastAPI + MongoDB)

This is a backend project built with **FastAPI** and **MongoDB** to manage a smart parking lot system.

---

## 📦 Features

* Register vehicle entries and exits
* MongoDB backend for persistent storage

---

## 📁 Project Structure

```
parkingLotManager/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # Pydantic models
│   ├── db.py            # MongoDB connection
│   ├── parking.py       # Business logic
│   └── utils.py         # Utility functions
├── README.md            # This file
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yoavgre/parkingLotManager.git
cd parkingLotManager
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start MongoDB (locally or in Docker)

**Option 1: Using Docker**

```bash
docker run -d --name mongodb -p 27017:27017 mongo:6
```

**Option 2: Locally installed MongoDB**

Make sure MongoDB is running on default port 27017:

```bash
sudo systemctl start mongod
```

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

Then open your browser at:

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Deployment

For cloud deployment using AWS EC2 and Pulumi, see the [infrastructure repo](https://github.com/yoavgre/parkingLotDeploy).

---