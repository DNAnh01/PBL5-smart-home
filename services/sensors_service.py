from daos.sensors_dao import SensorsDao
from schemas.sensors_schema import Sensors
from services.sensors_view_service import SensorsViewService
from schemas.sensors_view_schema import SensorsView

from collections import deque

sensors_dao = SensorsDao()
sensors_view_service = SensorsViewService()

class SensorsService:

    def create_sensors(self, sensors_create: Sensors) -> Sensors:
        return sensors_dao.create(sensors_create)

    def get_sensors(self, sensors_document_ID: str) -> Sensors:
        return sensors_dao.get(sensors_document_ID)
    
    def update_sensors(self, sensors_document_ID: str, sensors_update: Sensors) -> Sensors:
            
        sensors_view = sensors_view_service.get_sensors_view("SensorsViewDocumentID")

        temperature_sensor = {"timestamp": sensors_update.timestamp, "data": str(sensors_update.temperature_sensor_data)}
        humidity_sensor = {"timestamp": sensors_update.timestamp, "data": str(sensors_update.humidity_sensor_data)}
        gas_sensor = {"timestamp": sensors_update.timestamp, "data": str(sensors_update.gas_sensor_data)}
        
        temperature_sensor_update = deque(sensors_view.temperature_sensor, maxlen=10)
        temperature_sensor_update.append(temperature_sensor)
        temperature_sensor_update = list(temperature_sensor_update)
        
        humidity_sensor_update = deque(sensors_view.humidity_sensor, maxlen=10)
        humidity_sensor_update.append(humidity_sensor)
        humidity_sensor_update = list(humidity_sensor_update)

        gas_sensor_update = deque(sensors_view.gas_sensor, maxlen=10)
        gas_sensor_update.append(gas_sensor)
        gas_sensor_update = list(gas_sensor_update)
        
        sensors_view_service.update_sensors_view(sensors_view_document_ID="SensorsViewDocumentID",
                                                sensors_view_update=SensorsView(temperature_sensor=temperature_sensor_update,
                                                                                humidity_sensor=humidity_sensor_update,
                                                                                gas_sensor=gas_sensor_update))
        
        return sensors_dao.update(sensors_document_ID, sensors_update)