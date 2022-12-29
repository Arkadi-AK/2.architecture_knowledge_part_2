class DatabaseHelper:
    __database_connection = None
    __data: str = ""

    def __new__(cls):
        if cls.__database_connection is None:
            cls.__database_connection: DatabaseHelper = object.__new__(cls)
            print("Подключение к ДБ")
        return cls.__database_connection

    def select_data(self) -> str:
        return self.__data

    def insert_data(self, new_data):
        self.__data = new_data


if __name__ == "__main__":
    connection1 = DatabaseHelper()
    connection1.insert_data("123")

    connection2 = DatabaseHelper()
    print(connection2.select_data())  # Получает данные из единственного экземпляра
    print(id(connection1), id(connection2))
