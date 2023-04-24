from daos.temperature_sensor_dao import TemperatureSensorDao
from schemas.temperature_sensor_schema import TemperatureSensor

temperature_sensor_dao = TemperatureSensorDao()

class TemperatureSensorService:
    def create_temperature_sensor(self, temperature_sensor_create: TemperatureSensor) -> TemperatureSensor:
        return temperature_sensor_dao.create(temperature_sensor_create)

    def get_temperature_sensor(self, temperature_sensor_document_ID: str) -> TemperatureSensor:
        return temperature_sensor_dao.get(temperature_sensor_document_ID)
    
    def update_temperature_sensor(self, temperature_sensor_document_ID: str, temperature_sensor_update: TemperatureSensor) -> TemperatureSensor:
        return temperature_sensor_dao.update(temperature_sensor_document_ID, temperature_sensor_update)