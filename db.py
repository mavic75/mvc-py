import psycopg2
from psycopg2 import DatabaseError

def conn():
    try:
        connection = psycopg2.connect(
            host='dpg-cf36s202i3mnjchjl9bg-a.oregon-postgres.render.com',
            user='api_rest_j1py_user',
            password='rHaEl34znvMEL6ybEv4b1CQsgCCrFkyk',
            database='api_rest_j1py'
        )
                    # connection = psycopg2.connect(**cred)
            # cur = connection.cursor()
            # cur.execute('select version()')
            # res = cur.fetchone()
        return connection
    except Exception as ex:
        raise ex