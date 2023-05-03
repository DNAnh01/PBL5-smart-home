from daos.led_dao import LedDao
from schemas.led_schema import Led


led_dao = LedDao()

class LedService:
    def create_led(self, led_create: Led) -> Led:
        return led_dao.create(led_create)

    def get_led(self, led_document_ID: str) -> Led:
        return led_dao.get(led_document_ID)
    
    def update_led(self, led_document_ID: str, led_update: Led) -> Led:
        return led_dao.update(led_document_ID, led_update)