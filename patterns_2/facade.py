class ProviderCommunication:
    def receive(self):
        print("Получение продукции от производителя")

    def payment(self):
        print("Оплата поставщику с удержанием комисии за продажу продукции")


class Site:
    def placement(self):
        print("Размещение на сайте")

    def delete(self):
        print("Удаление с сайта")


class Database:
    def insert(self):
        print("Запись в БД")

    def delete(self):
        print("Удаление из БД")


class MarketPlace:
    def __init__(self):
        self._provide_communication = ProviderCommunication()
        self._site = Site()
        self._database = Database()

    def product_receipt(self):
        self._provide_communication.receive()
        self._site.placement()
        self._database.insert()

    def product_release(self):
        self._provide_communication.payment()
        self._site.delete()
        self._database.delete()


if __name__ == "__main__":
    market_place = MarketPlace()
    market_place.product_receipt()
    print("------------")
    market_place.product_release()
