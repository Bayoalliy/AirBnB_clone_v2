#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the
storage engine (FileStorage or DBStorage) =>
from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in
DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_of_states(id=None):
    state_lst = storage.all(State).values()

    if id:
        state_obj = None
        for state in state_lst:
            if state.id == id:
                state_obj = state
        return render_template('9-states.html', state=state_obj)
    else:
        return render_template('7-states_list.html', lst=state_lst)


@app.teardown_appcontext
def close_connection(exception):
    storage.close()


if __name__ == '__main__':
    app.run()
