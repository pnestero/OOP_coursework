from abc import ABC, abstractmethod

"""Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
 получения данных из файла по указанным критериям и удаления информации о вакансиях."""

class ConnectFile(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass





