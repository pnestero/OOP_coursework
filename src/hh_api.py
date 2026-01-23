"""Реализовать класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
Класс должен уметь подключаться к API и получать вакансии."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from src.abstract_classes import VacancyAPI



class HH_API(VacancyAPI):

    def __init__(self, name_vacancy, url, description, salary):
        self.name_vacancy = name_vacancy
        self.url = "https://api.hh.ru/vacancies"
        self.description = description
        self.__valid_salary(salary)



    def _connect(self, url: str, params: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
        pass


    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        pass

api = HH_API()  # Без параметров!
vacancies = api.get_vacancies("Python")  # Получаем список вакансий


    #
    # def valid_salary(self, salary):
    #     """шаги сравнение """
    #     self.salary = логика валидации(сравнения)
    #
    #
    # def __lt__(self, other):
    #     """Сравнения если меньше"""
    #     return self.salary < other.salary
    #
    #
    # def __gt__(self, other):
    #     """Сравнения если больше"""
    #     return self.salary > other.salary
    #
















