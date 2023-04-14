# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from app.forms import MainForm
from app.service import comparator


class User:
    def __init__(self, username):
        self.username = username


user = User('Maxim')
matched = False


@app.route('/', methods=['GET', 'POST'])
def index():
    global matched
    form = MainForm()
    if form.validate_on_submit():
        source = form.raw_data.data
        regular_ex = form.regular_expression.data
        matched = comparator.RegularExpressionComparator.equals_source_and_regular_ex(source, regular_ex)
        print(matched)
        return render_template('index.html', form=form, matched=matched)
    return render_template('index.html', form=form)
