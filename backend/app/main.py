from fastapi import FastAPI
from backend.app.routers.sensor_data import router


app = FastAPI(
    title="Industrial Equipment Monitoring API",
    description="Industrial IoT monitoring backend for collecting temperature and humidity data.",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "industrial-equipment-monitoring-api"
    }

app.include_router(router)