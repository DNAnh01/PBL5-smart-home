from daos.devices_dao import DevicesDao
from schemas.devices_schema import Devices


devices_dao = DevicesDao()

class DevicesService:
    def create_devices(self, devices_create: Devices) -> Devices:
        return devices_dao.create(devices_create)

    def get_devices(self, devices_document_ID: str) -> Devices:
        return devices_dao.get(devices_document_ID)
    
    def update_devices(self, devices_document_ID: str, devices_update: Devices) -> Devices:
        return devices_dao.update(devices_document_ID, devices_update)