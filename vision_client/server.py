from flask import Flask

app = Flask(__name__)

count = 0

@app.route("/")
def root():
    global count
    return str(count)

@app.route("/someone")
def someone():
    global count
    count = 1
    return str(count)

@app.route("/no_one")
def no_one():
    global count
    count = 0
    return str(count)

if __name__=="__main__":
    app.run(host='0.0.0.0')
