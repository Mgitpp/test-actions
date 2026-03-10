from fastapi import FastAPI
from datetime import datetime, date

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "VPe04 FastAPI backend is running",
        "server_time": datetime.now().isoformat(),
        "server_date": date.today().isoformat()
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/time")
def get_time():
    return {"server_time": datetime.now().isoformat()}


@app.get("/date")
def get_date():
    return {"server_date": date.today().isoformat()}


@app.get("/datetime")
def get_datetime():
    now = datetime.now()
    return {
        "server_datetime": now.isoformat(),
        "server_date": now.date().isoformat(),
        "server_time": now.time().isoformat(timespec="seconds")
    }


@app.get("/info")
def info():
    return {
        "service": "VPe04",
        "framework": "FastAPI"
    }