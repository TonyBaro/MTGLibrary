from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.card import Card

@app.route('/new_card')
def new_card():
    data={
        'id':session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('new_card.html', user = user)

@app.route('/add_card' , methods=["POST"])
def add_card():
    data = {
        'name':request.form['name'],
        'cost':request.form['cost'],
        'type':request.form['type'],
        'keywords':request.form['keywords'],
        'flavor':request.form['flavor'],
        'power':request.form['power'],
        'toughness':request.form['toughness'],
        'user':request.form['user']
    }
    Card.add_card(data)
    return redirect('/dashboard')

@app.route('/view_card/<num>')
def view_card(num):
    data = {
        'num':num,
        'id':session['user_id']
    }
    card = Card.get_card(data)
    user = User.get_user_by_id(data)
    return render_template ('view_card.html' , card = card, user = user)


