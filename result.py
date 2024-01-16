from bs4 import BeautifulSoup
import requeｓts
import time
import sqlite3

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=44&block_no=1133&year=2024&month=1&day=9&view='

r = requeｓts.get(url)
r.encoding = 'utf-8'

html_soup = BeautifulSoup(r.text, 'html.parser') # HTMLソースをBeautifulSoupオブジェクトに変換する（プログラムで扱いやすくするため）
print(type(html_soup))

tag1 = html_soup.find_all('table', class_='data2_s')

print(tag1)

tag2 = html_soup.find_all('td', class_='data_0_0')

data1 = [tag.string for tag in tag2]

import sqlite3
import os

path = '/Users/kosuke/DS2final'  
db_name = 'weather.sqlite'

if not os.path.exists(path + db_name):
   
    open(path + db_name, 'w').close()

con = sqlite3.connect(path + db_name)

con.close()

import sqlite3

con = sqlite3.connect(path + db_name)
cur = con.cursor()

cur.execute('CREATE TABLE weather_data (value TEXT)')

con.commit()
con.close()

data_to_save = tag2

con = sqlite3.connect(path + db_name)

cur = con.cursor()

for item in data_to_save:
    value = item.string
    cur.execute('INSERT INTO weather_data (value) VALUES (?)', (value,))

con.commit()
con.close()

import sqlite3

con = sqlite3.connect(path + db_name)
cur = con.cursor()

cur.execute('SELECT * FROM weather_data')
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()