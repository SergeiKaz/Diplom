from flask import Flask, render_template, url_for, request, redirect,make_response,flash,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from insert_tour import Insert_tour
from user import Uniq, Insert_user, Chek

app = Flask(__name__)
app.config['SECRET_KEY']='cnkjasnckjsacnkjsa6t75326674gfbgf'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tour.db'
# db = SQLAlchemy(app)

# db.init_app(app)


# class Travel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     street = db.Column(db.String(300), nullable=False)
#     price = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return '<Travel %r>' % self.id


@app.route('/')
def base():
    return render_template("base.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-place', methods=["POST", "GET"])
def create_place():
    if request.method == "POST":
        print("request.form")
    return render_template("create-place.html", title="Обратная связь", menu='Меню')


@app.route('/signin',methods=['POST','GET'])
def signin():
    if 'login' in session:
        return redirect(url_for('profile', username=session['login']))
    elif request.method =='POST':
        login=request.form['login']
        password=request.form['password']
        if Chek(login,password):
            session['login']=login
            return redirect(url_for('profile', username=session['login']))
    else:
        return render_template('signin.html')


@app.route('/registr',methods=['POST','GET'])
def registr():
        if request.method=='POST':
            name=request.form['name']
            sname=request.form['sname']
            email = request.form['email']
            login = request.form['login']
            password1=request.form['password']
            password2 = request.form['passwordanother']
            if password1==password2 and Uniq(login,email): # логин и почта уникальны
                Insert_user(name,sname,email,login,password1)
            return redirect('/')
        else:
            return render_template('registr.html')


def Insert_tour(name, street, price, date):
    pass


@app.route('/add',methods=['POST','GET'])
def add_tour():
        if request.method =='POST':
            name=request.form['name']
            street=request.form['street']
            price=request.form['price']
            date=request.form['date']
            if Insert_tour(name,street,price,date):
                flash('Запись успешно добавлена')
            else:
                flash('При вводе данных произошла ошибка, попробуйте снова')
            return render_template('add.html')
        else:
            return render_template('add.html')

@app.route('/enter')
def enter():
    return render_template("enter.html")


@app.route('/Price')
def Price():
    return render_template("Price.html")


if __name__ == "__main__":
    app.run(debug=True)
