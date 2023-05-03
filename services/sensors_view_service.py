from daos.sensors_view_dao import SensorsViewDao
from schemas.sensors_view_schema import SensorsView

sensors_view_dao = SensorsViewDao()

class SensorsViewService:

    def create_sensors_view(self, sensors_view_create: SensorsView) -> SensorsView:
        return sensors_view_dao.create(sensors_view_create)

    def get_sensors_view(self, sensors_view_document_ID: str) -> SensorsView:
        return sensors_view_dao.get(sensors_view_document_ID)
   
    def update_sensors_view(self, sensors_view_document_ID: str, sensors_view_update: SensorsView) -> SensorsView:
        return sensors_view_dao.update(sensors_view_document_ID, sensors_view_update)