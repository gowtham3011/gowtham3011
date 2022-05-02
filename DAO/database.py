import psycopg2

conection= psycopg2.connect("dbname='statergy' user='postgres' host='localhost' password='4563' port=1103")
cur = conection.cursor()


