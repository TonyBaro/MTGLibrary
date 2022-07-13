from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/new_card')
def new_card():
    data={
        'id':session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('new_card.html', user = user)
