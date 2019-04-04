from flask import Blueprint, render_template, abort

quiz = Blueprint('quiz_controller', __name__, template_folder='templates')

@quiz.route('/quiz')
def danger_assessment():
    return render_template("dangerous_ass.html");
