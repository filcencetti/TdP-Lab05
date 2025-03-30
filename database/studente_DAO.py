# Add whatever it is needed to interface with the DB Table studente
import database.DB_connect

def addstudent():
        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("select * from studente ")
        cursor.execute(query)
        students = []
        for row in cursor:
            students.append(row)
        cnx.close()
        return students