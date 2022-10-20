from flask import render_template, request, redirect, url_for
from helpers import login_required

class CompanyBranchRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):
        @self.app.route('/company_branches', methods=['get'])
        @login_required
        def company_branch_index():
            open_connection = self.db_connection.cursor(dictionary=True)
            open_connection.execute('select * from company_branches')
            company_branches = open_connection.fetchall()
            open_connection.close()
            return render_template('company_branches/index.html', company_branches=company_branches)


        @self.app.route('/company_branches/new_company_branch', methods=['get'])
        @login_required
        def new_company_branch():
            return render_template('company_branches/create.html')


        @self.app.route('/company_branches', methods=["POST"])
        @login_required
        def create_company_branch():
            Company_name = request.form.get('Company_name')
            Branch_name = request.form.get('Branch_name')
            Address = request.form.get('Address')
            Is_active = request.form.get('Is_active')

            insert_company_branches_query = f"INSERT  into company_branches (Company_name, Branch_name, Address, Is_active) values ('{Company_name}','{Branch_name}','{Address}','{Is_active}')"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(insert_company_branches_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('company_branch_index'))


        @self.app.route('/company_branches/<id>', methods=['get'])
        @login_required
        def edit(id):
            opened_connection = self.db_connection.cursor(dictionary=True)
            opened_connection.execute("SELECT * FROM company_branches where id = '{}'".format(id))
            company_branch = opened_connection.fetchone()
            opened_connection.close()
            return render_template('company_branches/edit.html', company_branch=company_branch)


        @self.app.route('/company_branches/<id>', methods=['post'])
        @login_required
        def update(id):
            Company_name = request.form.get('Company_name')
            Branch_name = request.form.get('Branch_name')
            Address = request.form.get('Address')
            Is_active = request.form.get('Is_active')

            update_company_branches_query = f"update company_branches set Company_name = '{Company_name}',  Branch_name = '{Branch_name}', Address = '{Address}', Is_active = '{Is_active}' WHERE id = {id}"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(update_company_branches_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('company_branch_index'))


        @self.app.route('/company_branches/<id>/delete_company_branch', methods=['post'])
        @login_required
        def delete_company_branch(id):
            delete_company_branches_query = f"delete from company_branches where id = '{id}'"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(delete_company_branches_query)
            self.db_connection.commit()
            opened_connection.close()
            return redirect(url_for('company_branch_index'))
