from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "industrial-equipment-monitoring-api"
    }