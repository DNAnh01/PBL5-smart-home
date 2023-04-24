from daos.gatehouse_dao import GateHouseDao
from schemas.gatehouse_schema import GateHouse


gatehouse_dao = GateHouseDao()

class GatehouseService:
    def create_gatehouse(self, gatehouse_create: GateHouse) -> GateHouse:
        return gatehouse_dao.create(gatehouse_create)

    def get_gatehouse(self, gatehouse_document_ID: str) -> GateHouse:
        return gatehouse_dao.get(gatehouse_document_ID)
    
    def update_gatehouse(self, gatehouse_document_ID: str, gateHouse_update: GateHouse) -> GateHouse:
        return gatehouse_dao.update(gatehouse_document_ID, gateHouse_update)