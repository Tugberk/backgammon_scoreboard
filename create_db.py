import sqlite3

conn = sqlite3.connect('scoreboard.db')
print 'db opened..'
c = conn.cursor()
c.execute('create table data(ID INTEGER PRIMARY KEY AUTOINCREMENT, playeronescore TEXT, playertwoscore TEXT, playertwoname TEXT, sonuc TEXT, tarih TEXT)')	
conn.commit()