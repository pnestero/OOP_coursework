"""Реализовать класс, наследующийся от абстрактного класса,
для работы с платформой hh.ru.
Класс должен уметь подключаться к API и получать вакансии."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

import requests

from src.abstract_classes import VacancyAPI


class HH_API(VacancyAPI):

    def __init__(self):
        self._base_url = "https://api.hh.ru/vacancies"
        self._headers = {'User-Agent': 'HH-User-Agent'}

    def _connect(self, url: str, params: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
        """
        Подключение API
        :param url: ссылка для подключения
        :param params: параметр запроса
        :param headers: заголовки запроса
        :return: ответ JSON
        """
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения API {e}")
            return {}

    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        """Получение вакансий с hh.ru
        :param search_query: Поисковый запрос
        :return: Список словарей
        """
        params = {
            'text': search_query,  # Критерий: параметр text
            'per_page': 100,  # Критерий: параметр per_page
            'area': 113,  # Россия (необязательно, но удобно)
            'page': 0  # Начинаем с первой страницы
        }
        data = self._connect(self._base_url, params, self._headers)
        return data.get('items', [])
