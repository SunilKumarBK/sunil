from flask import Blueprint, render_template

read = Blueprint('read',__name__)

@read.route('/read')
def default():
    return render_template('design.html')