from flask import Flask, render_template, request
from setuptools.command.register import register

app = Flask(__name__)


@app.route('/')
def log():
    return render_template('login1.html')


@app.route('/shop')
def shoplogin():
    return render_template('items.html')


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['username']
    passwrd = request.form['userpass']
    if uname == "nasar" and passwrd == "aweawe":
        return "Welcome %s" % uname + request.method
    else:
        return "Error in logging in" + request.method


@app.route('/Shop', methods=['POST'])
def shop():
    item_name = request.form['item_name']
    item_id = request.form['item_id']
    quantity = request.form['quantity']
    price = request.form['price']
    items = {"item_name": item_name, "item_id":item_id, "quantity": quantity, "price": price}
    return render_template('showitems.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
