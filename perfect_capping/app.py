"""
App for finding perfect honor 
This base code is taken from example projects for CIS 322 at UO by Professor Ramakrishnan Durairajan 
"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import perfect_cap_calc  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates the honor from different amounts of people
    """
    app.logger.debug("Got a JSON request")
    honor = request.args.get('honor', 999, type=float)

    app.logger.debug("honor={}\n".format(honor))
    
    # dictionary of persons and options
    options = perfect_cap_calc.calculate_honor(honor)
    one_person = options[1] # list of 1 person
    two_people = options[2]
    three_people = options[3]
    result = {"one_person": one_person, "two_people": two_people, "three_people": three_people}
    return flask.jsonify(result=result)

@app.route('/new', methods=['POST'])
def new():
    honor = request.form.getlist('honor')
    return '', 204

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    print("Opening for global access on port 5000")
    app.run(port=5000, host="0.0.0.0")
