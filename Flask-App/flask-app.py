from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
	return 'Hello The Real World!'
	
@app.route('/goodbye'):
def goodbye():
	return 'See ya . . .'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
