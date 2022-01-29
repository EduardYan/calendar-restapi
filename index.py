"""
This is the principal
file for execute the server.
"""

from app import app

if __name__ == '__main__':
  # running the server
  app.run(host = '0.0.0.0', debug = True)