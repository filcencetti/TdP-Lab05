# Add whatever it is needed to interface with the DB Table corso
import database.DB_connect

def addcourses():
    cnx = database.DB_connect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = ("select * from corso ")
    cursor.execute(query)
    courses = []
    for row in cursor:
        courses.append(row)
    cnx.close()
    return courses