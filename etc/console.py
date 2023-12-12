# -*- coding: utf-8 -*-

# Класс для управления программой через консоль
class ConsoleProgram:
    # Инициализация класса, принимает БД в качестве параметра
    def __init__(self, database) -> None:
        self.database = database

    # Метод запуска
    def start(self) -> None:
        print('Добро пожаловать в базу данных управления книгами в библиотеке.')
        while True:
            # Вывод меню с возможными действиями
            print('\nВыберите действие:')
            print('1. Просмотреть текущий каталог книг')
            print('2. Найти книгу')
            print('3. Добавить новую книгу')
            print('4. Удалить книгу')
            print('0. Выйти')

            # Получение выбора пользователя
            user_choice = input('Введите номер необходимого действия (ex. 1): ')

            # Обработка выбора пользователя
            if user_choice == '1':
                self.display_books()
            elif user_choice == '2':
                self.search_books()
            elif user_choice == '3':
                self.add_book()
            elif user_choice == '4':
                self.delete_book()
            elif user_choice == '0':
                print('Хорошего дня! :D')
                break
            else:
                print('\n[!] Некорректный ввод. Пожалуйста, выберите снова.\n')

    # Метод для отображения списка книг
    def display_books(self) -> None:
        # Парсинг всех книг из БД
        books = self.database.get_all_books()
        # Проверка наличия книг в БД
        if len(books) != 0:
            # Вывод списка книг
            print('Список книг:')
            for book in books:
                print(f"{book[0]}. {book[1]} - {book[2]}")

            # Получение ID книги для вывода подробной информации пользователю
            book_id = input('Введите ID книги для подробной информации (или нажмите Enter для возврата): ')

            # Проверка ввода пользователя
            if book_id and book_id.isdigit():
                # Отображение информации о книге
                self.display_book(int(book_id))
            else:
                print('\n[!] Введите корректный ID книги.\n')
        else:
            print('\n[!] Библиотека книг пуста.\n')

    # Метод для отображения информации о книге
    def display_book(self, book_id) -> int:
        # Получение информации о книге из БД
        book = self.database.get_book_details(book_id)
        # Проверка наличия книги
        if book:
            # Вывод информации
            print('\nПодробная информация о книге:')
            print(f"Название: {book[1]}")
            print(f"Автор: {book[2]}")
            print(f"Описание: {book[3]}")
            print(f"Жанр: {book[4]}\n")
            return 1
        else:
            print('\n[!] Книга не найдена.\n')
            return 0

    # Метод для поиска книг по ключевому слову
    def search_books(self) -> None:
        # Получение ключевого слова от пользователя
        keyword = input('Введите ключевое слово для поиска: ')
        # Поиск книг по ключевому слову в БД
        found_books = self.database.search_books(keyword)
        # Проверка наличия найденных книг
        if found_books:
            # Вывод найденных книг
            print('\nНайденные книги:')
            for book in found_books:
                print(f"{book[0]}. {book[1]} - {book[2]}")
        else:
            print('\n[!] Книги не найдены.\n')

    # Метод для добавления новой книги
    def add_book(self) -> None:
        # Получение информации о новой книге от пользователя
        title = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        description = input('Введите описание книги: ')
        genre = input('Введите жанр книги: ')

        # Добавление книги в БД
        self.database.add_book(title, author, description, genre)
        print('\nКнига успешно добавлена в базу данных.\n')

    # Метод для удаления книги
    def delete_book(self) -> None:
        # Получение ID книги для удаления
        book_id = input('Введите ID книги, которую вы хотите удалить: ')
        # Проверка корректности ввода пользователя
        if book_id.isdigit():
            book_id = int(book_id)
            # Проверка книги на существование и отображение информации о книге перед удалением 
            if self.display_book(book_id) != 0:
                # Запрос подтверждения удаления
                confirmation = input('Вы уверены, что хотите удалить эту книгу? (y/n): ')
                if confirmation.lower() == 'y':
                    # Удаление книги из БД
                    self.database.delete_book(book_id)
                    print('Книга успешно удалена.')
        else:
            print('\n[!] Введите корректный ID книги.\n')
