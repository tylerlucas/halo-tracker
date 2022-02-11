# write and load files to database
import sqlite3
import gamer





def get_conn():
    return sqlite3.connect('example.db')
    
# Insert a gamer object into gamers table
def update_gamer_to_db(gamer):
    con = get_conn()
    cur = con.cursor()
    stats = [stat for stat in gamer.get_stats().values()]
    cur.execute("SELECT * FROM gamers WHERE gamertag = ?", (stats[0], ))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO gamers VALUES (?, ?, ?, ?, ?, ?)", stats)
    else:
        stats.append(stats.pop(0))
        cur.execute("UPDATE gamers SET kda=?, win_rate=?, rank_open=?, rank_kbm_sd=?, rank_con_sd=? WHERE gamertag = ?", stats)
    print('Gamertag added to GamerDB!')
    # save/close
    con.commit()
    con.close()

def get_gamer_db():
    con = get_conn()
    cur = con.cursor()

    print(f"""
|--------------------------------------GAMER DB-------------------------------------------------------|
|                                                                                                     |
|    Gamertag    |      KDA       |    Win Rate    |    Open ELO    | KB/M Solo/Duo  |  Con Solo/Duo  |
|-----------------------------------------------------------------------------------------------------|""")
    # print full table
    for row in cur.execute('SELECT * FROM gamers ORDER BY gamertag'):
            #print(row)
            counter = 0
            column_len = 13
            for stat in row:
                print(f'| {stat}', end =" ")
                add_length = column_len - len(stat)
                print(' ' * add_length, end = " ")
                counter += 1
                if counter > 5:
                    print('|')
                    counter = 0
                #print(len(stat))
    print(f"""|-----------------------------------------------------------------------------------------------------|
    """)


def recreate_gamer_db():
    con = get_conn()
    cur = con.cursor()
    cur.execute('DROP TABLE gamers')
    cur.execute('''CREATE TABLE gamers(gamertag text, kda text, win_rate text, rank_open text, rank_kbm_sd text, rank_con_sd text)''')
    # save/close
    con.commit()
    con.close()