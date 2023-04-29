from daos.gas_sensor_dao import GasSensorDao
from schemas.gas_sensor_schema import GasSensor

gas_sensor_dao = GasSensorDao()

class GasSensorService:
    def create_gas_sensor(self, gas_sensor_create: GasSensor) -> GasSensor:
        return gas_sensor_dao.create(gas_sensor_create)

    def get_gas_sensor(self, gas_sensor_document_ID: str) -> GasSensor:
        return gas_sensor_dao.get(gas_sensor_document_ID)
    
    def update_gas_sensor(self, gas_sensor_document_ID: str, gas_sensor_update: GasSensor) -> GasSensor:
        return gas_sensor_dao.update(gas_sensor_document_ID, gas_sensor_update)