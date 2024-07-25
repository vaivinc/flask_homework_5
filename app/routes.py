from flask import render_template, request, url_for, redirect
from app.models import Group
from data.data_db import insert_data
from db import Session
from app import app


@app.route("/")
def index():
    return render_template("index.html",
                           title="Pizzawow",
                           )


@app.route("/menu/")
def menu():
    with Session() as session:
        pizza = session.query(Group).all()
    context = {
        "title": "Pizzawow", "pizzas": pizza}

    return render_template("menu.html", **context)


@app.route("/add_pizza/", methods=["GET", "POST"])
def add_pizza():
    with Session() as session:

        if request.method == "POST":
            name = request.form["name"]
            ingredients = request.form["ingredients"]
            price = request.form["price"]

            item = Group(name=name,
                         ingredients=ingredients,
                         price=price)


            session.add(item)
            session.commit()

            return redirect(url_for("menu"))
        else:
            return render_template("form_add_pizza.html")


@app.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html", error=404)


@app.errorhandler(500)
def error_500(error):
    return render_template("errors/500.html", error=500)
