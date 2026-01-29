class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ['name_vacancy', 'url', 'description', 'salary']

    def __init__(self, name_vacancy, url, description, salary):
        self.name_vacancy = name_vacancy
        self.url = url
        self.description = description
        self.salary = self.__valid_salary(salary)

    def __valid_salary(self, salary):
        """Проверка зарплаты"""
        if not salary:
            return 0
        if isinstance(salary, dict):
            return salary.get("from") or salary.get("to") or 0
        return salary

    def __lt__(self, other):
        """Меньше"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Больше"""
        return self.salary > other.salary

    def __str__(self):
        """Вывод вакансии"""
        if self.salary:
            return f"{self.name_vacancy} | {self.salary} руб. | {self.url}"
        return f"{self.name_vacancy} | Зарплата не указана | {self.url}"

    @classmethod
    def cast_to_object_list(cls, vacancies_data):
        """Создание списка объектов из данных API"""
        vacancies_list = []

        for item in vacancies_data:
            name = item.get('name', 'Без названия')
            url = item.get('alternate_url', '')

            snippet = item.get('snippet', {})
            requirement = snippet.get('requirement', '')
            responsibility = snippet.get('responsibility', '')
            description = requirement or responsibility

            salary_data = item.get('salary')

            vacancy = cls(name, url, description, salary_data)
            vacancies_list.append(vacancy)

        return vacancies_list