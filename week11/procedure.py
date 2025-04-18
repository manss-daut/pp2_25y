import psycopg2
from config import load_config

def create_procedures():
    config = load_config()
    procedures = [

        # функция поиска по шаблону
        """
        CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
        RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM PhoneBook
            WHERE name ILIKE '%' || pattern || '%'
               OR phone ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
        """,

        # процедура вставки или обновления одного пользователя
        """
        CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM PhoneBook WHERE name = p_name) THEN
                UPDATE PhoneBook SET phone = p_phone WHERE name = p_name;
            ELSE
                INSERT INTO PhoneBook(name, phone) VALUES (p_name, p_phone);
            END IF;
        END;
        $$;
        """,

        # процедура массовой вставки с проверкой номера
        """
        CREATE OR REPLACE PROCEDURE insert_many_users(
            IN names TEXT[], IN phones TEXT[], OUT bad_data TEXT[]
        )
        LANGUAGE plpgsql
        AS $$
        DECLARE
            i INTEGER := 1;
        BEGIN
            bad_data := ARRAY[]::TEXT[];
            WHILE i <= array_length(names, 1) LOOP
                IF phones[i] ~ '^[0-9]{11}$' THEN
                    BEGIN
                        INSERT INTO PhoneBook(name, phone)
                        VALUES (names[i], phones[i]);
                    EXCEPTION
                        WHEN unique_violation THEN
                            UPDATE PhoneBook SET phone = phones[i] WHERE name = names[i];
                    END;
                ELSE
                    bad_data := array_append(bad_data, names[i] || ' - ' || phones[i]);
                END IF;
                i := i + 1;
            END LOOP;
        END;
        $$;
        """,

        # функция пагинации
        """
        CREATE OR REPLACE FUNCTION get_paginated_contacts(p_limit INT, p_offset INT)
        RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM PhoneBook
            ORDER BY id
            LIMIT p_limit OFFSET p_offset;
        END;
        $$ LANGUAGE plpgsql;
        """,

        # процедура удаления по имени или номеру
        """
        CREATE OR REPLACE PROCEDURE delete_by_value(val TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            DELETE FROM PhoneBook
            WHERE name = val OR phone = val;
        END;
        $$;
        """
    ]

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for proc in procedures:
                    cur.execute(proc)
                print("успе[]")
    except Exception as e:
        print("ошибка:", e)

if __name__ == '__main__':
    create_procedures()