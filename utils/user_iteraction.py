import psycopg2
from src.hh_vacancy_parser import HHVacancyParsing
from src.db_module import DBmodule
from config import config


def user_interaction(value, db_name):
    """
    Взаимодействие с пользователем, получает данные от пользователя, записывает в базу данных и сортирует.
    """
    HHVacancyParsing(value)
    module = DBmodule(db_name)
    module.create_tabls()
    module.full_table(value)


def delete_database(db_name):
    """
    Удаление базы данных
    """
    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE {db_name}")
    cursor.close()
    conn.close()


def create_database(db_name):
    """
    Создание базы данных и таблиц для сохранения данных о каналах и видео
    """
    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cursor.execute(f"CREATE DATABASE {db_name}")
    cursor.close()
    conn.close()


if __name__ == '__main__':
    delete_database("python")


