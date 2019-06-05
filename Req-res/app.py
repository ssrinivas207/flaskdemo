from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/dinner')
@app.route('/dinner/<food>')
def eat(food = None):
    return render_template('main.html', food=food)

if __name__=="__main__":
    app.run()