"""
This file have some configurations
for run the server, also the routes for the
server. Execute index.py for the server.
"""

from flask import Flask
from routes.calendars import calendars


# creating the server
app = Flask(__name__)

# using routes
app.register_blueprint(calendars)