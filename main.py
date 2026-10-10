import os
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="NAAI Tech App", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "NAAI Tech App is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
