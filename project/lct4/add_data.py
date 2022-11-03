import csv
import sys
from django.conf import settings
import os
import django
import shutil
import psycopg2

settings.configure()
django.setup()

arr = [[]]

def insert_products():
    connect = psycopg2.connect(dbname='lct4', user='postgres', password='postgres', host='localhost')
    cursor = connect.cursor()
    for k in range(3, 93):
        print(k)
        dataReader = csv.reader(open(f"./data/{k}/DATTSVT.csv", encoding="utf8"), delimiter='\t', quotechar='"')
        i = 0
        for row in dataReader:
            if i == 0:
                i += 1
                continue
            cursor.execute(f"insert into lct4_products (direction, date, country, product, ezdim, stoim, netto, kol, region, district) values ('{row[0]}', "
                           f"'{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}', '{row[9]}');")

    connect.commit()
    cursor.close()
    connect.close()


insert_products()
