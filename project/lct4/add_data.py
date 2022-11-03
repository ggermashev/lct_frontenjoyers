import csv
import sys
import time

from django.conf import settings
import os
import django
import shutil
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

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


def insert_codes():
    connect = psycopg2.connect(dbname='lct4', user='postgres', password='postgres', host='localhost')
    cursor = connect.cursor()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.alta.ru/tnved/')
    time.sleep(5)
    driver.implicitly_wait(15)
    pluses = driver.find_elements(By.XPATH, "//i[@class='jstree-icon jstree-ocl']")
    driver.implicitly_wait(15)
    for p in pluses:
        time.sleep(0.3)
        p.click()
        time.sleep(0.3)

    driver.implicitly_wait(5)
    descriptions = driver.find_elements(By.XPATH, "//li/ul/li/a/span[@class='pTnved_title']")
    i = 1
    for d in descriptions:
        cursor.execute(f"insert into lct4_codes (id, description) values ('{i}', '{d.text}')")
        i += 1
        if i == 77:
            i += 1

    connect.commit()
    cursor.close()
    connect.close()


def update_regions():
    conn = psycopg2.connect(dbname='lct4', user='postgres', password='postgres', host='localhost')
    cur = conn.cursor()
    cur.execute(f"select region from lct4_products;")
    regions_wnames = set(cur.fetchall())
    for r_wn in regions_wnames:
        reg = r_wn[0].split(' - ')
        r = reg[0]
        name = reg[1]
        cur.execute(f"update lct4_products set region={r} where region='{r_wn[0]}'")
        cur.execute(f"insert into lct4_regions (id, name) values ('{r}', '{name}');")
    conn.commit()
    cur.close()
    conn.close()


def update_districts():
    conn = psycopg2.connect(dbname='lct4', user='postgres', password='postgres', host='localhost')
    cur = conn.cursor()
    cur.execute(f"select district from lct4_products;")
    districts_wnames = set(cur.fetchall())
    for d_wn in districts_wnames:
        dist = d_wn[0].split('-')
        d = dist[0]
        name = '-'.join(dist[1:])
        cur.execute(f"update lct4_products set district={d} where district='{d_wn[0]}'")
        cur.execute(f"insert into lct4_districts (id, name) values ('{d}', '{name}');")
    conn.commit()
    cur.close()
    conn.close()


update_districts()
