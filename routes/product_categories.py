from flask import render_template, request, redirect, url_for
from helpers import login_required

class ProductCategoryRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):
        @self.app.route('/product_categories', methods=['get'])
        @login_required
        def product_category_index():
            open_connection = self.db_connection.cursor(dictionary=True)
            open_connection.execute('select * from product_categories')
            product_categories = open_connection.fetchall()
            open_connection.close()
            return render_template(' product_categories/index.html', product_categories=product_categories)


        @self.app.route('/product_categories/new_product_categories', methods=['get'])
        @login_required
        def new_product_categories():
            return render_template('product_categories/create.html')


        @self.app.route('/product_categories', methods=["POST"])
        @login_required
        def create_product_category():
            name = request.form.get('name')
            insert_product_categories_query = f"INSERT  into product_categories ( name ) values ('{name}')"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(insert_product_categories_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('product_category_index'))


        @self.app.route('/product_categories/<id>', methods=['get'])
        @login_required
        def edit_product_category(id):
            opened_connection = self.db_connection.cursor(dictionary=True)
            opened_connection.execute("SELECT * FROM product_categories where id = '{}'".format(id))
            product_category = opened_connection.fetchone()
            opened_connection.close()
            return render_template('product_categories/edit.html', product_category=product_category)


        @self.app.route('/product_categories/<id>', methods=['post'])
        @login_required
        def update_product_category(id):
            name = request.form.get('name')
            update_product_categories_query = f"update product_categories set name = '{name}' WHERE id = '{id}'"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(update_product_categories_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('product_category_index'))


        @self.app.route('/product_categories/<id>/delete', methods=['post'])
        @login_required
        def delete_product_category(id):
            delete_product_categories_query = f"delete from product_categories where id = '{id}'"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(delete_product_categories_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('product_category_index'))
