
import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


def show_players(cursor, title):

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n\n  -- {} --".format(title))
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:

    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    new_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    player_metrics = ("Smeagol", "Shire Folk", 1)

    cursor.execute(new_player, player_metrics)
 
    db.commit()

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    additional_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(additional_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    remove_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(remove_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n  Press the ENTER key to continue... ")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Username or password error, please try again later. ")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database that you have requested does not exist ")

    else:
        print(err)

finally:

    db.close()
