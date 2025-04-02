import database.DB_connect

cnx = database.DB_connect.get_connection()

def addregistration():
        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("select * from iscrizione ")
        cursor.execute(query)
        registrations = []
        for row in cursor:
            registrations.append(row)
        cnx.close()
        return registrations

def addstudent(matr,course):
        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("insert into "
        "iscrizione (matricola,codins)"
        "values (%s,%s)")

        cursor.execute(query,
                       (matr,course))
        cnx.commit()
        cnx.close()
        return