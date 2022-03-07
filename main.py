from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_all_candidates():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidates/<int:candidate_id>")
def page_candidate_by_id(candidate_id):

    candidate = get_candidate_by_id(candidate_id)
    if not candidate:
        return "Кандидат не найден"

    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_candidate_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    candidates_total = len(candidates)
    if not candidates:
        return "Кандидат не найден"

    return render_template("search.html", candidates=candidates, candidates_total=candidates_total)


@app.route("/skill/<skill_name>")
def page_candidate_by_skill(skill_name):
    skilled_candidates = get_candidates_by_skill(skill_name)
    candidates_total = len(skilled_candidates)
    if not skilled_candidates:
        return "Кандидаты не найдены"
    return render_template(
        "skill.html", skilled_candidates=skilled_candidates, skill_name=skill_name, candidates_total=candidates_total
    )


app.run()
