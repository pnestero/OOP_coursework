from src.hh_api import HH_API
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def user_interaction():
    """Основная функция программы"""

    # Ввод данных от пользователя
    search_query = input("Введите поисковый запрос: ")
    if not search_query:
        print("Запрос не может быть пустым!")
        return

    top_n = int(input("Сколько вакансий показать в топе? "))
    filter_words = input("Ключевые слова для фильтрации (через пробел): ").split()

    # Получение вакансий с HH
    print("\nИщем вакансии...")
    hh_api = HH_API()
    vacancies_data = hh_api.get_vacancies(search_query)

    if not vacancies_data:
        print("Вакансий не найдено")
        return

    # Создание объектов вакансий
    vacancies = Vacancy.cast_to_object_list(vacancies_data)
    print(f"Найдено вакансий: {len(vacancies)}")

    # Сохранение в файл
    saver = JSONSaver()
    # очищаем файл перед записью
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        f.write('[]')
    # добавляем
    for vacancy in vacancies:
        saver.add_vacancy(vacancy)
    print("Вакансии сохранены в файл vacancies.json")

    # Фильтрация по ключевым словам
    if filter_words:
        filtered_vacancies = []
        for vacancy in vacancies:
            text = (vacancy.name_vacancy + vacancy.description).lower()
            for word in filter_words:
                if word.lower() in text:
                    filtered_vacancies.append(vacancy)
                    break
        vacancies = filtered_vacancies

    # Сортировка и вывод топ N
    vacancies.sort(reverse=True)  # от большей зарплаты к меньшей
    top_vacancies = vacancies[:top_n]

    print(f"\nТоп {len(top_vacancies)} вакансий по зарплате:")

    for i, vacancy in enumerate(top_vacancies, 1):
        print(f"{i}. {vacancy}")
        print()


if __name__ == "__main__":
    user_interaction()