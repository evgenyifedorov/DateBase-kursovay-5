# Проект DatdBase
__________
В рамках проекта получаем данные о компаниях и вакансиях с сайта hh.ru, проектируем таблицы в БД PostgreSQL и загружаем полученные данные в созданные таблицы.
__________
## Основные шаги проекта
________
1. Получаем данные о работодателях и их вакансиях с сайта hh.ru. Для этого используется публичный API hh.ru и библиотека 'requests'
2. Выбирается 10 или менее интересных компаний, от которых пользователь получает данные о вакансиях по API.
3. Таблицы проектируются в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используется библиотека 'psycopg2'
4. Реализуется код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
5. Результаты выводятся в консоль
6. Запуск проекта происходит в файле main.py, далее вся работа по выводу результатов происходит в консоли 
