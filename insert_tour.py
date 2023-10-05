import psycopg2

def Insert_tour(name,street,price,date):
        try:
            connection = psycopg2.connect(
                host='127.0.0.1',
                user="postgres",
                password="12121987Ser",
                database='tour'
            )
            with connection.cursor() as cursor:
                request="Insert into tours(name,street,price,date) Values(%s,%s,%s,%s,%s)"
                record=[name,street,price,date]
                cursor.execute(request,record)
            return True
        except:
            return False



def Get_allbook():
    connection = psycopg2.connect(
        host='127.0.0.1',
        user="postgres",
        password="postgres",
        database='book'
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'Select * from books;'
        )
        return cursor.fetchall()
        connection.commit()

def Getbook(id):
    connection = psycopg2.connect(
        host='127.0.0.1',
        user="postgres",
        password="postgres",
        database='book'
    )

    with connection.cursor() as cursor:
        cursor.execute(
            f'Select * from books where id={id};'
        )
        return cursor.fetchone()
        connection.commit()