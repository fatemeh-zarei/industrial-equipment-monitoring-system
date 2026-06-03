from fastapi import APIRouter
from backend.app.schemas import SensorData

router = APIRouter()

sensor_data_storage = []


@router.post("/sensor-data")
def create_sensor_data(data: SensorData):

    sensor_data_storage.append(data)

    return {
        "message": "Sensor data received successfully",
        "data": data
    }

@router.get("/sensor-data")
def get_sensor_data():
    return {
        "count": len(sensor_data_storage),
        "data": sensor_data_storage
    }