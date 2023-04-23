from daos.gatehouse_dao import GateHouseDao
from schemas.gatehouse_schema import GateHouse


gatehouse_dao = GateHouseDao()

class GatehouseService:
    def create_gatehouse(self, gatehouse_create: GateHouse) -> GateHouse:
        return gatehouse_dao.create(gatehouse_create)

    def get_gatehouse(self) -> GateHouse:
        return gatehouse_dao.get()
    
    def update_gatehouse(self, gateHouse_update: GateHouse) -> GateHouse:
        return gatehouse_dao.update(gateHouse_update)