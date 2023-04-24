from daos.humidity_sensor_dao import HumiditySensorDao
from schemas.humidity_sensor_schema import HumiditySensor

humidity_sensor_dao = HumiditySensorDao()

class HumiditySensorService:
    def create_humidity_sensor(self, humidity_sensor_create: HumiditySensor) -> HumiditySensor:
        return humidity_sensor_dao.create(humidity_sensor_create)

    def get_humidity_sensor(self, humidity_sensor_document_ID: str) -> HumiditySensor:
        return humidity_sensor_dao.get(humidity_sensor_document_ID)
    
    def update_humidity_sensor(self, humidity_sensor_document_ID: str, humidity_sensor_update: HumiditySensor) -> HumiditySensor:
        return humidity_sensor_dao.update(humidity_sensor_document_ID, humidity_sensor_update)