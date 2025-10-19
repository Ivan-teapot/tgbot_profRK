from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def root():
    return {"service": "root", "status": "ok"}
