import json
import MySQLdb
HOST = 'localhost'
USER = 'ganesh'
PASSWORD = 'ganesh55'
DATABASE = 'MOVIES'

db = MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
cursor = db.cursor()
movieslist = open('movies.json','r').read()
data = json.loads(movieslist)
for rec in data:
    query = "INSERT INTO MOVIES_movies (popularity, director, genre, movielist_score, name) values('%f', '%s', '%s', '%f', '%s')"
    popularity, director, genre, movielist_score, name = rec['99popularity'],\
                rec['director'], rec['genre'], rec['movielist_score'], rec['name']
    strip_list = [item.strip() for item in genre]
    values = (popularity, director, '<>'.join(strip_list), movielist_score, name)
    cursor.execute(query % values)
    db.commit()




#cursor.execute('INSERT INTO MOVIES_movies(popularity, director, genre, movielist_score, name) values(%d, %s, %f, %f, %s)',(rec[0],rec[1],rec[2],rec[3],rec[4]))
