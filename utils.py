import json


def load_candidates_from_json():
    """
    Возвращает список всех кандидатов
    :param:
    :return: candidates
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


def get_candidate_by_id(candidate_id):
    """
    Возвращает одного кандидата по его id
    :param candidate_id:
    :return: candidate
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Возвращает одного кандидата по имени
    :param candidate_name: 
    :return: candidates_by_name
    """
    candidates = load_candidates_from_json()
    candidates_by_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_by_name.append(candidate)
    return candidates_by_name


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    :param skill_name:
    :return: skilled_candidates
    """
    candidates = load_candidates_from_json()
    skilled_candidates = []
    for candidate in candidates:
        skills_list = candidate["skills"].lower().split(", ")
        if skill_name.lower() in skills_list:
            skilled_candidates.append(candidate)
    return skilled_candidates



