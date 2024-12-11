CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            second_name TEXT NOT NULL,
            middle_name TEXT NOT NULL,
            login TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            hashed_password TEXT NOT NULL,
            address_registry TEXT NOT NULL
        );

INSERT INTO users (first_name, second_name, middle_name, login, email, phone, hashed_password, address_registry)
VALUES
    ('Иван', 'Иванов', 'Иванович', 'ivan123', 'ivan@example.com', '+79991234567', 'hashed_password_1', '123e4567-e89b-12d3-a456-426614174000'),
    ('Петр', 'Петров', 'Петрович', 'petr456', 'petr@example.com', '+79992345678', 'hashed_password_2', '234e5678-f90c-23e4-b567-537725285001'),
    ('Анна', 'Сидорова', 'Андреевна', 'anna789', 'anna@example.com', '+79993456789', 'hashed_password_3', '345f6789-g01d-34f5-c678-648836396002'),
    ('Елена', 'Кузнецова', 'Ивановна', 'elena101', 'elena@example.com', '+79994567890', 'hashed_password_4', '456g7890-h12e-45g6-d789-759947407003'),
    ('Дмитрий', 'Смирнов', 'Александрович', 'dmitry202', 'dmitry@example.com', '+79995678901', 'hashed_password_5', '567h8901-i23f-56h7-e890-860058518004'),
    ('Ольга', 'Морозова', 'Сергеевна', 'olga303', 'olga@example.com', '+79996789012', 'hashed_password_6', '678i9012-j34g-67i8-f901-971169629005'),
    ('Сергей', 'Васильев', 'Игоревич', 'sergey404', 'sergey@example.com', '+79997890123', 'hashed_password_7', '789j0123-k45h-78j9-g012-082270730006'),
    ('Мария', 'Федорова', 'Алексеевна', 'maria505', 'maria@example.com', '+79998901234', 'hashed_password_8', '890k1234-l56i-89k0-h123-193381841007'),
    ('Алексей', 'Козлов', 'Владимирович', 'alexey606', 'alexey@example.com', '+79999012345', 'hashed_password_9', '901l2345-m67j-90l1-i234-204492952008'),
    ('Татьяна', 'Николаева', 'Павловна', 'tatiana707', 'tatiana@example.com', '+79990123456', 'hashed_password_10', '012m3456-n78k-01m2-j345-315503063009'),
    ('Владимир', 'Соколов', 'Андреевич', 'vladimir808', 'vladimir@example.com', '+79991234567', 'hashed_password_11', '123n4567-o89l-12n3-k456-426614174000'),
    ('Ирина', 'Белова', 'Геннадьевна', 'irina909', 'irina@example.com', '+79992345678', 'hashed_password_12', '234o5678-p90m-23o4-l567-537725285001'),
    ('Николай', 'Попов', 'Дмитриевич', 'nikolay101', 'nikolay@example.com', '+79993456789', 'hashed_password_13', '345p6789-q01n-34p5-m678-648836396002'),
    ('Екатерина', 'Лебедева', 'Игоревна', 'ekaterina202', 'ekaterina@example.com', '+79994567890', 'hashed_password_14', '456q7890-r12o-45q6-n789-759947407003'),
    ('Александр', 'Ковалев', 'Сергеевич', 'alexander303', 'alexander@example.com', '+79995678901', 'hashed_password_15', '567r8901-s23p-56r7-o890-860058518004'),
    ('Марина', 'Иванова', 'Алексеевна', 'marina404', 'marina@example.com', '+79996789012', 'hashed_password_16', '678s9012-t34q-67s8-p901-971169629005'),
    ('Геннадий', 'Петров', 'Владимирович', 'gennady505', 'gennady@example.com', '+79997890123', 'hashed_password_17', '789t0123-u45r-78t9-q012-082270730006'),
    ('Людмила', 'Смирнова', 'Дмитриевна', 'lyudmila606', 'lyudmila@example.com', '+79998901234', 'hashed_password_18', '890u1234-v56s-89u0-r123-193381841007'),
    ('Павел', 'Федоров', 'Иванович', 'pavel707', 'pavel@example.com', '+79999012345', 'hashed_password_19', '901v2345-w67t-90v1-s234-204492952008'),
    ('Оксана', 'Козлова', 'Сергеевна', 'oksana808', 'oksana@example.com', '+79990123456', 'hashed_password_20', '012w3456-x78u-01w2-t345-315503063009');