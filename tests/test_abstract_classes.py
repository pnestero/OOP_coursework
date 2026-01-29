import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from src.abstract_classes import VacancyAPI
from src.file_storage_abc import VacancyStorage


def test_abstract_class_vacancyapi():
    """Тест что VacancyAPI абстрактный"""
    with pytest.raises(TypeError):
        # Нельзя создать экземпляр абстрактного класса
        api = VacancyAPI()


def test_abstract_class_vacancystorage():
    """Тест что VacancyStorage абстрактный"""
    with pytest.raises(TypeError):
        # Нельзя создать экземпляр абстрактного класса
        storage = VacancyStorage()


def test_abstract_methods():
    """Тест наличия абстрактных методов"""
    # Проверяем что методы объявлены в VacancyAPI
    assert hasattr(VacancyAPI, 'get_vacancies')
    assert hasattr(VacancyAPI, '_connect')

    # Проверяем что методы объявлены в VacancyStorage
    assert hasattr(VacancyStorage, 'add_vacancy')
    assert hasattr(VacancyStorage, 'get_vacancies')
    assert hasattr(VacancyStorage, 'delete_vacancy')

