from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def bighome():
    return render_template ( 'index.html', x=8, y=8, color1='black', color2='red')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def home(x,y,color1,color2):
    return render_template ('index.html', x=x, y=y, color1=color1,color2=color2) 

@app.route('/<path:path>')
def catch_all (path):
    return 'Sorry! Nothing here. Try again.'

if __name__=='__main__':
    app.run(debug=True)