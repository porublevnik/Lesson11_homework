from utils import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def candidates_list():
    items = load_candidates_from_json("candidates.json")
    return render_template("list.html", items=items)


@app.route('/candidate/<int:x>')
def candidate_card(x):
    candidate = get_candidate(x)
    return render_template("card.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    items = get_candidates_by_name(candidate_name)
    count = len(items)
    return render_template("search.html", items=items, count=count, candidate_name=candidate_name)

@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    items = get_candidates_by_skill(skill_name)
    count = len(items)
    return render_template("skill.html", items=items, count=count, skill_name=skill_name)

app.run()
