"""Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты,
такие как название вакансии, ссылка на вакансию, зарплата, краткое описание
или требования и т. п. (всего не менее четырех атрибутов).
Класс должен поддерживать методы сравнения вакансий между собой по зарплате и
валидировать данные, которыми инициализируются его атрибуты."""


class Vacancy:
    """класс для работы с вакансиями"""
    __slots__ = ['name_vacancy', 'url', 'description', 'salary']

    def __init__(self, name_vacancy, url, description, salary):
        self.name_vacancy = name_vacancy
        self.url = url
        self.description = description
        self.salary = self.__valid_salary(salary)



    def __valid_salary(self, salary):
        """шаги сравнения"""
        if not salary:
            return 0
        if isinstance(salary, dict):
            return salary.get("from", 0) or salary.get("to", 0)
        return salary

    def __lt__(self, other):
        """Сравнения если меньше"""
        return self.salary < other.salary


    def __gt__(self, other):
        """Сравнения если больше"""
        return self.salary > other.salary

