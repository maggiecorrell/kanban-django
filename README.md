# kanban-django

Django REST Framework + Ajax

Create a REST API backend and Ajax frontend.


## Installation

'pip install -r requirements.txt' in your command line

## Usage

A requirements.txt file.
A Django project.


## Contributing

- Maggie Correll: https://github.com/maggiecorrell
- Tara Davis: https://github.com/tarakdavis
- Andrew Musicant: https://github.com/andrewmusicant


## Objectives

Summarize the REST architecture.
Design and build a REST API.
Design and build a data-driven JavaScript UI with Ajax.

Build a Trello clone using Django REST Framework and Ajax in JavaScript.

### Build a REST API

First, using the Django REST Framework, build an API with one resource: tasks.

URLs are nested under /api/. Create an API with the following endpoints:

- GET /api/tasks/
- POST /api/tasks/
- PUT /api/tasks/{id}
- DELETE /api/tasks/{id}

The task resource includes the following fields:
id, title, status, priority

### Build a UI

Built a user interface with HTML, CSS, and JavaScript that works with the Django REST API using Ajax.

### Able to do all of the following via Ajax...

- Create a user and login.
- Create/edit/delete tasks.
- Re-prioritize tasks.
