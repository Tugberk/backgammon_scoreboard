from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date



app = Flask(__name__)
myDatabase = 'scoreboard.db'

@app.route('/')
def index():
	conn = sqlite3.connect(myDatabase)
	c = conn.cursor()
	c.execute('select * from data order by id desc')
	result = c.fetchall()
	c.execute('select count(*) from data where sonuc = ?', ['WON'])
	won = c.fetchall()
	won = won[0]
	c.execute('select count(*) from data where sonuc = ?', ['LOST'])
	lost = c.fetchall()
	lost = lost[0]
	return render_template('index.html', icerik=result, won=won, lost=lost)

@app.route('/ekle', methods=['POST'])
def ekle():
	rakip = request.form['playerTwo']
	playerOneScore = request.form['scoreOne']
	playerTwoScore = request.form['scoreTwo']
	tarih = date.today()
	tarih = str(tarih)
	sonuc = ''
	
	if(int(playerOneScore) > int(playerTwoScore)):
			sonuc = 'WON'
	else:
		sonuc = 'LOST'

	
	#connect to db and add values
	conn = sqlite3.connect(myDatabase)
	c = conn.cursor()
	c.execute('insert into data(playeronescore, playertwoscore, playertwoname, sonuc, tarih) values(?,?,?,?,?)', (playerOneScore, playerTwoScore, rakip, sonuc,tarih))
	conn.commit()
	#return render_template('index.html', rakip = playerTwoName, playeronescore = playerOneScore, playertwoscore = playerTwoScore, sonuc = sonuc, tarih=tarih)
	return redirect(url_for('index'))

@app.route('/delete/<int:post_id>')
def delete(post_id):
	conn = sqlite3.connect(myDatabase)
	c = conn.cursor()
	c.execute('delete from data where id = ?', [post_id])
	conn.commit()
	return redirect(url_for('index'))


if __name__ == "__main__":
	app.run(debug=True)