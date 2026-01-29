import json, os
from typing import List, Dict, Any
from src.file_storage_abc import VacancyStorage


class JSONSaver(VacancyStorage):
    def __init__(self, filename="vacancies.json"):
        self._filename = filename
        self._ensure_file_exists()


    def _ensure_file_exists(self):
        """Проверка на существование файла"""
        if not os.path.exists(self._filename):
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_vacancy(self, vacancy) -> None:
        """Добавить вакансию в файл"""
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                # не пустой ли файл
                content = f.read()
                if content.strip():
                    data = json.loads(content)
                else:
                    data = []

            vacancy_dict = {
                'name_vacancy': vacancy.name_vacancy,
                'url': vacancy.url,
                'description': vacancy.description,
                'salary': vacancy.salary
            }

            # нет ужк такой вакансии (проверка)
            for item in data:
                if item.get('url') == vacancy_dict['url']:
                    return
            # добавить
            data.append(vacancy_dict)

            # сохранение
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Ошибка: {e}")

    def get_vacancies(self, **criteria) -> List[Dict[str, Any]]:
        """Получить вакансии"""
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)

            if not criteria:
                return vacancies

            keyword = criteria.get('keyword')
            if keyword:
                filtered = []
                for item in vacancies:
                    text = f"{item.get('name_vacancy', '')} {item.get('description', '')}".lower()
                    if keyword.lower() in text:
                        filtered.append(item)
                return filtered
            return vacancies

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Ошибка файла {e} при получении")
            return []

    def delete_vacancy(self, vacancy) -> None:
        """Удалить вакансию"""
        try:
            # Читаем файл
            with open(self._filename, 'r') as f:
                data = json.load(f)

            # Получаем URL
            url_to_delete = vacancy.url

            # Удаляем
            new_data = []
            for item in data:
                if item['url'] != url_to_delete:
                    new_data.append(item)

            # Сохраняем
            with open(self._filename, 'w') as f:
                json.dump(new_data, f, indent=2)

            print("Вакансия удалена")

        except Exception as e:
            print(f"Ошибка {e} при удалении")

