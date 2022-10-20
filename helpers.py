import functools
from flask import redirect, url_for, session

#Decorator
def login_required(route_func):

    @functools.wraps(route_func)
    def inner_callback_func(**kwargs):
        if session.get('email') is None:
            return redirect(url_for('login'))
        return route_func(**kwargs)

    return inner_callback_func