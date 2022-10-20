from flask import render_template


class HomeRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):
         @self.app.route('/', methods=['GET'])
         def home():
             return render_template('home.html')
