from flask import render_template, request, redirect, url_for
from helpers import login_required

class ProductRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):
        @self.app.route('/products', methods=['get'])
        @login_required
        def products_index():
            open_connection = self.db_connection.cursor(dictionary=True)
            open_connection.execute('select * from products')
            products = open_connection.fetchall()
            open_connection.close()
            return render_template(' products/index.html', products=products)


        @self.app.route('/products/new_product', methods=['get'])
        @login_required
        def new_product():
            return render_template('products/create.html')


        @self.app.route('/products', methods=["POST"])
        @login_required
        def create_products():
            name = request.form.get('name')
            banner = request.form.get('banner')
            is_feature = request.form.get('is_feature')
            priority = request.form.get('priority')
            price = request.form.get('price')
            categori_id = request.form.get('categori_id')
            discount = request.form.get('discount')

            insert_products_query = f"INSERT  into products ( name, banner, is_feature, priority,  price, categori_id, discount) values ('{name}','{banner}','{is_feature}','{priority}','{price}','{categori_id}','{discount}')"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(insert_products_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('products_index'))


        @self.app.route('/products/<id>', methods=['get'])
        @login_required
        def edit_products(id):
            opened_connection = self.db_connection.cursor(dictionary=True)
            opened_connection.execute("SELECT * FROM products where id = '{}'".format(id))
            product = opened_connection.fetchone()
            opened_connection.close()
            return render_template('products/edit.html', product=product)


        @self.app.route('/products/<id>', methods=['post'])
        @login_required
        def update_products(id):
            name = request.form.get('name')
            banner = request.form.get('banner')
            is_feature = request.form.get('is_feature')
            priority = request.form.get('priority')
            price = request.form.get('price')
            categori_id = request.form.get('categori_id')
            discount = request.form.get('discount')

            update_products_query = f"update products set name = '{name}', banner = '{banner}',is_feature = '{is_feature}',priority = '{priority}',price = '{price}',categori_id = '{categori_id}',discount = '{discount}' WHERE id = {id}"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(update_products_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('products_index'))


        @self.app.route('/products/<id>/delete', methods=['post'])
        @login_required
        def delete_products(id):
            delete_products_query = f"delete from products where id = '{id}'"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(delete_products_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('products_index'))

