from abc import ABC, abstractmethod
from typing import Dict, Any, List


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API сервисов вакансий"""

    @abstractmethod
    def _connect(self, url: str, params: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
        """Подключение API"""
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        """Получение вакансий через API"""
        pass