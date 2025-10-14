from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, OTT Sharing Service!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}