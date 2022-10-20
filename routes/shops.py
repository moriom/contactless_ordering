from flask import render_template, request, redirect, url_for, session
from helpers import login_required

class ShopRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):

        @self.app.route('/shops', methods = ['GET'])
        @login_required
        def shop_index():
            opened_connection = self.db_connection.cursor(dictionary=True)
            opened_connection.execute('SELECT * FROM shops')
            shops = opened_connection.fetchall()
            opened_connection.close()
            return render_template('shops/index.html', shops=shops)

        @self.app.route('/shops/new_shop', methods=['get'])
        @login_required
        def new_shop():
            if session.get('email') is None:
                return redirect(url_for('login'))

            return render_template('shops/create.html')


        @self.app.route('/shops', methods=["POST"])
        @login_required
        def create_shop():
            if session.get('email') is None:
                return redirect(url_for('login'))

            banner = request.form.get('banner')
            title = request.form.get('title')
            description = request.form.get('description')
            offer = request.form.get('offer')
            currency = request.form.get('currency')

            insert_shops_query = f"INSERT  into shops ( banner, title, description, offer, currency ) values ('{banner}', '{title}', '{description}', '{offer}', '{currency}')"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(insert_shops_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('shop_index'))

        @self.app.route('/shops/<id>', methods=['get'])
        @login_required
        def edit_shop(id):
            if session.get('email') is None:
                return redirect(url_for('login'))

            opened_connection = self.db_connection.cursor(dictionary=True)
            opened_connection.execute("SELECT * FROM shops where id = '{}'".format(id))
            shop = opened_connection.fetchone()
            opened_connection.close()
            return render_template('shops/edit.html', shop=shop)

        @self.app.route('/shops/<id>', methods=['post'])
        @login_required
        def update_shop(id):
            if session.get('email') is None:
                return redirect(url_for('login'))

            banner = request.form.get('banner')
            title = request.form.get('title')
            description = request.form.get('description')
            offer = request.form.get('offer')
            currency = request.form.get('currency')

            update_shops_query = f"update shops set banner = '{banner}', title = '{title}', description = '{description}', offer = '{offer}', currency = '{currency}' WHERE id = {id}"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(update_shops_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('shop_index'))

        @self.app.route('/shops/<id>/delete', methods=['post'])
        @login_required
        def delete_shop(id):

            delete_shops_query = f"delete from shops where id = '{id}'"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(delete_shops_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('shop_index'))
