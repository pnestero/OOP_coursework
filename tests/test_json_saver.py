import json
import os

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def test_create_saver():
    """Создание JSONSaver"""
    saver = JSONSaver("test.json")

    assert saver is not None
    assert saver._filename == "test.json"

    # Проверяем что файл создан
    assert os.path.exists("test.json")

    # Убираем за собой
    if os.path.exists("test.json"):
        os.remove("test.json")


def test_add_vacancy_simple():
    """Добавление вакансии"""
    test_file = "test_vacancy.json"

    # Удаляем если был старый файл
    if os.path.exists(test_file):
        os.remove(test_file)

    saver = JSONSaver(test_file)
    vacancy = Vacancy("Тест", "http://test.com", "Описание", 50000)

    saver.add_vacancy(vacancy)

    # Проверяем что файл не пустой
    assert os.path.exists(test_file)
    assert os.path.getsize(test_file) > 0

    # Убираем
    if os.path.exists(test_file):
        os.remove(test_file)


def test_read_vacancies():
    """Чтение вакансий"""
    test_file = "test_read.json"

    # Создаем тестовый файл вручную
    test_data = [{"name_vacancy": "Test", "url": "http://test.com", "salary": 100000}]

    with open(test_file, "w") as f:
        json.dump(test_data, f)

    saver = JSONSaver(test_file)
    vacancies = saver.get_vacancies()

    assert len(vacancies) == 1
    assert vacancies[0]["name_vacancy"] == "Test"

    # Убираем
    if os.path.exists(test_file):
        os.remove(test_file)


def test_filter_vacancies():
    """Фильтрация вакансий"""

    test_file = "test_filter.json"

    # Создаем тестовый файл
    test_data = [
        {
            "name_vacancy": "Python Developer",
            "url": "url1",
            "description": "Python job",
            "salary": 100000,
        },
        {
            "name_vacancy": "Java Developer",
            "url": "url2",
            "description": "Java job",
            "salary": 120000,
        },
    ]

    with open(test_file, "w") as f:
        json.dump(test_data, f)

    saver = JSONSaver(test_file)

    # Фильтруем по Python
    python_vacancies = saver.get_vacancies(keyword="Python")
    assert len(python_vacancies) == 1
    assert python_vacancies[0]["name_vacancy"] == "Python Developer"

    # Все вакансии
    all_vacancies = saver.get_vacancies()
    assert len(all_vacancies) == 2

    # Убираем
    if os.path.exists(test_file):
        os.remove(test_file)


def test_delete_vacancy():
    """Удаление вакансии"""


    test_file = "test_delete.json"

    # Создаем тестовый файл
    test_data = [
        {
            "name_vacancy": "Удалить",
            "url": "delete_me",
            "description": "test",
            "salary": 50000,
        },
        {
            "name_vacancy": "Оставить",
            "url": "keep_me",
            "description": "test",
            "salary": 100000,
        },
    ]

    with open(test_file, "w") as f:
        json.dump(test_data, f)

    saver = JSONSaver(test_file)

    # Создаем вакансию для удаления
    vacancy_to_delete = Vacancy("Удалить", "delete_me", "test", 50000)

    # Удаляем
    saver.delete_vacancy(vacancy_to_delete)

    # Проверяем что осталась одна
    with open(test_file, "r") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["url"] == "keep_me"

    # Убираем
    if os.path.exists(test_file):
        os.remove(test_file)
