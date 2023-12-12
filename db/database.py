# -*- coding: utf-8 -*-
import sqlite3

# Класс для работы с базой данных книг
class BookDatabase:
    # Инициализация класса
    def __init__(self, db_name='db/library.db') -> None:
        # Инициализация соединения и курсора БД
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # Создание таблицы, если она не существует
        self.create_table()

    # Метод для создания таблицы книг, если она не существует
    def create_table(self) -> None:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                description TEXT,
                genre TEXT
            )
        ''')
        self.connection.commit()

    # Метод для добавления новой книги в БД
    def add_book(self, title, author, description, genre) -> None:
        self.cursor.execute('INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)',
                            (title, author, description, genre))
        self.connection.commit()

    # Метод для получения списка всех книг (ID, название, автор)
    def get_all_books(self) -> list:
        self.cursor.execute('SELECT id, title, author FROM books')
        return self.cursor.fetchall()

    # Метод для получения подробной информации о книге
    def get_book_details(self, book_id) -> tuple:
        self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        return self.cursor.fetchone()

    # Метод для получения списка книг по жанру
    def get_books_by_genre(self, genre) -> list:
        self.cursor.execute('SELECT id, title, author FROM books WHERE genre = ?', (genre,))
        return self.cursor.fetchall()

    # Метод для поиска книг по ключевому слову в названии или авторе
    def search_books(self, keyword) -> list:
        self.cursor.execute('SELECT id, title, author FROM books WHERE title LIKE ? OR author LIKE ?',
                            ('%' + keyword + '%', '%' + keyword + '%'))
        return self.cursor.fetchall()

    # Метод для удаления книги из БД
    def delete_book(self, book_id) -> None:
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.connection.commit()

    # Метод для закрытия соединения с БД
    def close_connection(self) -> None:
        self.connection.close()
