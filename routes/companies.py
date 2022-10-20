from flask import render_template, request, redirect, url_for
from helpers import login_required

class CompanyRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):
        @self.app.route('/companies', methods=['get'])
        @login_required
        def company_index():
            open_connection = self.db_connection.cursor(dictionary=True)
            open_connection.execute('select * from companies')
            companies = open_connection.fetchall()
            open_connection.close()
            return render_template(' company/index.html', companies=companies)


        @self.app.route('/company/new_company', methods=['get'])
        @login_required
        def new_company():
            return render_template('companies/create.html')


        @self.app.route('/companies', methods=["POST"])
        @login_required
        def create_company():
            company_name = request.form.get('company_name')
            Domain_name = request.form.get('Domain_name')
            Is_active = request.form.get('Is_active')

            insert_companies_query = f"INSERT  into companies (company_name, Domain_name, Is_active) values ('{company_name}','{Domain_name}','{Is_active}')"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(insert_companies_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('company_index'))


        @self.app.route('/companies/<id>', methods=['get'])
        @login_required
        def edit_company(id):
            opened_connection = self.db_connection.cursor(dictionary=True)
            opened_connection.execute("SELECT * FROM companies where id = '{}'".format(id))
            company = opened_connection.fetchone()
            opened_connection.close()
            return render_template('companies/edit_company.html', company=company)


        @self.app.route('/companies/<id>', methods=['post'])
        @login_required
        def update_company(id):
            company_name = request.form.get('companies_name')
            Domain_name = request.form.get('Domain_name')
            Is_active = request.form.get('Is_active')

            update_companies_query = f"update companies set company_name = '{company_name}', Domain_name = '{Domain_name}',Is_active = '{Is_active}' WHERE id = {id}"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(update_companies_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('company_index'))


        @self.app.route('/companiesy/<id>/delete', methods=['post'])
        @login_required
        def delete_company(id):
            delete_companies_query = f"delete from companies where id = '{id}'"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(delete_companies_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('company_index'))