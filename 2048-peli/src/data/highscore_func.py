from database_connection import get_database_connection


def insert_in_table(self,connection):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Highscores (result) VALUES (?)", [self.highscore])
    connection.commit()


def top_3(self,connection):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT h.player, h.result FROM Highscores h ORDER BY result DESC LIMIT 3;")
    rows = cursor.fetchall()
    self.highest_scores = ""
    for i, row in enumerate(rows):
        player = row[0]
        result = row[1]
        score_str = f"{i+1}. {player}: {result}"
        self.highest_scores += score_str
    return self.highest_scores
    connection.commit()

def get_hs(connection):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
            "SELECT h.result FROM Highscores h ORDER BY result DESC LIMIT 1;")
    rows = cursor.fetchall()
    if rows:
        return rows[0][0]
    else:
        return 0
    connection.commit()


# def initialize_database():
#     connection = get_database_connection()

#     insert_in_table(connection)
#     top_3(connection)


# if __name__ == "__main__":
#     initialize_database()