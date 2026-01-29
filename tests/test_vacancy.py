from src.vacancy import Vacancy

# Тестируем создание вакансии
def test_create_vacancy():

    v = Vacancy("Python Developer", "http://hh.ru/vacancy/123", "Разработка на Python", 100000)

    # Проверяем что поля установлены правильно
    assert v.name_vacancy == "Python Developer"
    assert v.url == "http://hh.ru/vacancy/123"
    assert v.salary == 100000
    assert v.description == "Разработка на Python"

    print("✓ test_create_vacancy пройден")


# Тестируем сравнение вакансий
def test_compare_vacancies():
    from src.vacancy import Vacancy

    v1 = Vacancy("Junior", "url1", "desc", 50000)
    v2 = Vacancy("Senior", "url2", "desc", 150000)

    assert v2 > v1

    assert v1 < v2

    assert v1 != v2

    print("✓ test_compare_vacancies пройден")


# Тестируем вакансию без зарплаты
def test_vacancy_no_salary():
    from src.vacancy import Vacancy

    v = Vacancy("Test", "url", "desc", None)

    assert v.salary == 0

    print("✓ test_vacancy_no_salary пройден")


# Тестируем строковое представление
def test_vacancy_str():
    from src.vacancy import Vacancy

    v = Vacancy("Тест", "http://test.com", "Описание", 120000)
    result = str(v)

    assert "Тест" in result
    assert "120000" in result

    print("✓ test_vacancy_str пройден")


# Запускаем все тесты
if __name__ == "__main__":
    print("Запуск тестов Vacancy...")
    test_create_vacancy()
    test_compare_vacancies()
    test_vacancy_no_salary()
    test_vacancy_str()
    print("\n✅ Все тесты Vacancy пройдены!")