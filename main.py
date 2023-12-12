# -*- coding: utf-8 -*-
from etc.console import ConsoleProgram  # Класс для работы с консолью
from db.database import BookDatabase  # Класс для работы с базой данных

# Функция запуска программы
def starting() -> None:
    # Обьявление имен для классов
    database = BookDatabase()
    console = ConsoleProgram(database)
    # Запуск самой программы. Вызов метода start в функции ConsoleProgram
    console.start()
    # Закрытие соединения с БД после завершения работы программы
    database.close_connection()

# Если файл используется как основной скрипт
if __name__ == "__main__":
    # Вызов функции для запуска программы
    starting()
