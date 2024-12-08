-- Создание таблицы Users
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first_name TEXT,
    second_name TEXT,
    middle_name TEXT,
    phone TEXT,
    email TEXT,
    address TEXT NOT NULL
);

-- Пример добавления пользователя
INSERT INTO Users (login, password, first_name, second_name, middle_name, phone, email, address)
VALUES ('user1', 'pass123', 'Иванов Иван Иванович', '123456789', 'user1@example.com', 'uuid_компьютера_1');