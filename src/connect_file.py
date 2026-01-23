from connect_file_abc import ConnectFile

"Создать класс для сохранения информации о вакансиях в JSON-файл."

class Connest_JSON(ConnectFile):

    def __init__(self, filename):.
        self.filename = filename
        pass


    def add_vacancy(self, vacancy):
        """Добавление вакансий"""
        pass


    def get_vacancies(self):
        """Получение вакансий"""
        pass


    def delete_vacancies(self):
        """Удаление вакансий"""
        pass




















