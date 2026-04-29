from flask import Flask, Blueprint, render_template
import flask
# Create a Blueprint named 'main'
main = flask.Blueprint('main', __name__)
@main.route('/')
def home():
    # This looks for index.html inside your templates folder
    return flask.render_template('index.html')
@main.route('/about')
def about():
    # This looks for about.html inside your templates folder
    return flask.render_template('about.html')