from abc import ABC, abstractmethod
from typing import Any, Dict, List


class VacancyStorage(ABC):
    """Абстрактный класс для работы с данными вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy) -> None:
        """Добавить вакансию"""
        pass

    @abstractmethod
    def get_vacancies(self, **criteria) -> List[Dict[str, Any]]:
        """Получить вакансии"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy) -> None:
        """Удалить вакансии"""
        pass
