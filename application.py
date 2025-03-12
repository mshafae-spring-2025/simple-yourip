from flask import Flask, render_template, request

application = Flask(__name__)

@app.route("/")
def show_me():
    ip = request.remote_addr
    return render_template('show.html', remote_ip=ip)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name='World'):
    return render_template('hello.html', name=name.title())

@app.route("/sqrt/<number>")
def square_root(number="0"):
    from math import sqrt
    d = {
        "number": number,
        "root": sqrt(float(number))
    }
    return render_template('square_root.html', **d)