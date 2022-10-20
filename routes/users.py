from flask import render_template, redirect, url_for, session
from forms import SignUpForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required

class UsersRoutes:
    def __init__(self, app, db_connection):
        self.app = app
        self.db_connection = db_connection
        self.routes()

    def routes(self):
        @self.app.route("/users/signup", methods=["POST", "get"])
        @login_required
        def signup():
            form = SignUpForm()
            if not form.validate_on_submit():
                return render_template("users/signup.html", form=form)

            # if everything fine
            email = form.email.data
            name = form.name.data
            password = form.password.data
            password = generate_password_hash(password)

            insert_users_query = f"INSERT  into users ( name, email, password, is_active ) values ('{name}', '{email}', '{password}', '{1}')"
            opened_connection = self.db_connection.cursor()
            opened_connection.execute(insert_users_query)
            self.db_connection.commit()
            opened_connection.close()

            return render_template("users/signup.html", message="Successfully signed up")


        @self.app.route("/users/login", methods=["POST", "get"])
        def login():
            form = LoginForm()
            if form.validate_on_submit():

                email = form.email.data
                password = form.password.data

                opened_connection = self.db_connection.cursor(dictionary=True)
                opened_connection.execute(f"SELECT * FROM users where email ='{email}'")
                user = opened_connection.fetchone()
                opened_connection.close()

                if user is None or not check_password_hash(user.get('password'), password):
                    return render_template("users/login.html", form=form, message="Wrong Credentials. Please Try Again.")
                else:
                    session['email'] = user.get('email')
                    return render_template("users/login.html", message="Successfully Logged In!")
            return render_template("users/login.html", form=form)


        @self.app.route("/users/logout")
        @login_required
        def logout():
            # if 'email' in session:
            #     session.pop('email')
            session.clear()
            return redirect(url_for('shops_index'))



