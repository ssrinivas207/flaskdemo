from flask import Flask, render_template
app = Flask(__name__)

#@app.route('/')
#def home():
#    return 'Hello DXC'
    #return render_template("main.html")

@app.route('/user/<name>')
def user(name):
    return render_template('main.html', name=name)

if __name__ == "__main__":
    app.run()