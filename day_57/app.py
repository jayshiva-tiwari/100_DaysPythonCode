# Day 57 of python with programming paglu 🎀
# Build a Portfolio API


from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
PROJECTS_FILE = 'projects.json'

# Helper to load and save JSON
def load_projects():
    if os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE) as f:
            return json.load(f)
    return []

def save_projects(projects):
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent=2)

@app.route('/')
def home():
    return "📂 Portfolio API is running!"

# GET all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    tech = request.args.get('tech')  # Filter by tech query param
    projects = load_projects()
    if tech:
        projects = [p for p in projects if tech in p.get('tech', [])]
    return jsonify(projects)

# GET single project
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    projects = load_projects()
    for project in projects:
        if project['id'] == project_id:
            return jsonify(project)
    return jsonify({"error": "Project not found"}), 404

# POST new project
@app.route('/projects', methods=['POST'])
def add_project():
    new_project = request.json
    projects = load_projects()

    # Auto assign ID
    new_project['id'] = (projects[-1]['id'] + 1) if projects else 1

    projects.append(new_project)
    save_projects(projects)
    return jsonify(new_project), 201

if __name__ == '__main__':
    app.run(debug=True)
