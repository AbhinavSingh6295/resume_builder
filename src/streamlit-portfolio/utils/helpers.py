def load_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def format_project_data(project):
    return {
        "title": project.get("title", "Untitled"),
        "description": project.get("description", "No description available."),
        "link": project.get("link", "#")
    }

def format_skill_data(skill):
    return {
        "name": skill.get("name", "Unknown Skill"),
        "level": skill.get("level", "N/A")
    }