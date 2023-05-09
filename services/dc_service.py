from daos.dc_dao import DCDao
from schemas.dc_schema import DC


dc_dao = DCDao()

class DCService:
    def create_dc(self, dc_create: DC) -> DC:
        return dc_dao.create(dc_create)

    def get_dc(self, dc_document_ID: str) -> DC:
        return dc_dao.get(dc_document_ID)
    
    def update_dc(self, dc_document_ID: str, dc_update: DC) -> DC:
        return dc_dao.update(dc_document_ID, dc_update)