"""Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты,
такие как название вакансии, ссылка на вакансию, зарплата, краткое описание
или требования и т. п. (всего не менее четырех атрибутов).
Класс должен поддерживать методы сравнения вакансий между собой по зарплате и
валидировать данные, которыми инициализируются его атрибуты."""


class Vacancy():

    def __init__(self, name_vacancy, url, description, salary):
        self.name_vacancy = name_vacancy
        self.url = url
        self.description = description
        self.__valid_salary(salary)




    def valid_salary(self, salary):
        """шаги сравнение """
        self.salary = логика валидации(сравнения)


    def __lt__(self, other):
        """Сравнения если меньше"""
        return self.salary < other.salary


    def __gt__(self, other):
        """Сравнения если больше"""
        return self.salary > other.salary
