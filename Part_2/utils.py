import json


def load_candidates_from_json(path):
    """Получает содержимое страницы в формате json и переводит в список"""
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    for item in load_candidates_from_json("candidates.json"):
        if item['id'] == candidate_id:
            return item


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    candidates = []
    for item in load_candidates_from_json("candidates.json"):
        if candidate_name.lower() in item['name'].lower():
            candidates.append(item)
    return candidates


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    candidates = []
    for item in load_candidates_from_json("candidates.json"):
        skills = item['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(item)
    return candidates

