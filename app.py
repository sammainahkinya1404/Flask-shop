from flask import Flask,render_template
# from flask import SQLAlchemy

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')



if __name__ =='main':
    app.run(debug=True)
