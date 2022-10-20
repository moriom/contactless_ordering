from flask import Flask
import mysql.connector


app = Flask(__name__)
app.config['SECRET_KEY'] =
db_connection = mysql.connector.connect(
    host =
    user =
    password =
    database =
)

#import here
from routes.shops import ShopRoutes
from routes.product_categories import ProductCategoryRoutes
from routes.products import ProductRoutes
from routes.companies import CompanyRoutes
from routes.company_branches import CompanyBranchRoutes
from routes.users import UsersRoutes
from routes.home import HomeRoutes
from routes.menu import MenuRoutes

#Initializing route instance
ShopRoutes(app, db_connection)
ProductCategoryRoutes(app, db_connection)
ProductRoutes(app, db_connection)
CompanyRoutes(app, db_connection)
CompanyBranchRoutes(app, db_connection)
UsersRoutes(app, db_connection)
HomeRoutes(app, db_connection)
MenuRoutes(app, db_connection)

if __name__ == '__main__':
    app.run()
