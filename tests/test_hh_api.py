from src.hh_api import HH_API
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))


def test_hh_api_creation():
    """Создание объекта API"""

    api = HH_API()
    assert api is not None
    assert hasattr(api, "_base_url")
    assert api._base_url == "https://api.hh.ru/vacancies"


def test_connect_method():
    """Проверка метода подключения"""
    from src.hh_api import HH_API

    api = HH_API()
    # Просто проверяем что метод существует
    assert hasattr(api, "_connect")


def test_get_vacancies_method():
    """Проверка метода получения вакансий"""
    from src.hh_api import HH_API

    api = HH_API()
    result = api.get_vacancies("Python")

    # Должен вернуть список (даже если пустой)
    assert isinstance(result, list)


def test_get_vacancies_with_empty_query():
    """Проверка с пустым запросом"""
    from src.hh_api import HH_API

    api = HH_API()
    result = api.get_vacancies("")
    # Должен вернуть список
    assert isinstance(result, list)


def test_api_attributes():
    """Проверка атрибутов API"""
    from src.hh_api import HH_API

    api = HH_API()

    # Проверяем все атрибуты
    assert hasattr(api, "_headers")
    assert isinstance(api._headers, dict)
