from flask import Flask, url_for, request, render_template
from app import app

# server/
@app.route('/')
def hello():
	createLink = "<a href='" + url_for('create') + "'>Create a question</a>"
	return """<html>
				<head>
					<title>Ciao Mondo!!'</title>
				</head>
				<body>
					""" + createLink + """
					<h1>Hello Vitto!</h1>
				</body>
			</html>"""
#server/create
@app.route('/create')
def create():
	if request.method == 'GET':
		#send user the format
		return render_template('CreateQuestion.html')
	elif request.method == 'POST':
		#read form and data and save it
		title = request.form['title']
		answer = request.form['answer']
		question = request.form['question']
		#Store data in data store
		return render_tempalte('CreatedQuestion.html',question = question)
		
	else:
		return "<h2>Invalid request</h2>"

#server/question/<tile>
@app.route('/question/<title>')
def question(title):
	return "<h2>" + title + "</h2>"
