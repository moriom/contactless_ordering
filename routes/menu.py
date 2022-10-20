from flask import render_template

class MenuRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):
        @self.app.route('/menu', methods = ['GET'])
        def menu_index():
            opened_connection = self.db_connection.cursor(dictionary=True)
            opened_connection.execute('SELECT * FROM shops')
            menu = opened_connection.fetchall()
            opened_connection.close()
            return render_template('menu/index.html', menu=menu)
