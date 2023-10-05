from confirg import create


def Insert_tours(name, street, price, date):
    try:

        with create().cursor() as cursor:
            cursor.execute(
                """Insert into tour(name,street,price,date) 
                    Values (name,street,price,date);""")
            create().commit()
        cursor.close()
        print(name)
    except Exception as exp:
        print('Error')
    finally:
        create().close()
