from flask import Flask,jsonify
import random

from quotes import funny_quotes

app = Flask(__name__)

@app.route("/api/randquo")
def random_run_method():
    quotes = funny_quotes()
    length = len(quotes)
    selected_quotes = quotes[random.randint(0,length-1)]
    return jsonify(selected_quotes)

#val = random_run_method()
#print(val)

if __name__ == "__main__":
    app.run()

