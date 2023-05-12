from database_connection import get_database_connection


def drop_table(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists Highscores;
    ''')

    connection.commit()


def create_table(connection):
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE Highscores (id INTEGER PRIMARY KEY, player TEXT, result INTEGER);")

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_table(connection)
    create_table(connection)


if __name__ == "__main__":
    initialize_database()
