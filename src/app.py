from flask import Flask
from src.routes.public_routes import *
from src.routes.private_routes import *

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'asdasjnwjasdm,asd'
)

"""
    Public routes
"""
#Signin route.
app.add_url_rule(public["signin_route"], view_func=public["signin_controller"])

"""
    Private routes
"""
app.add_url_rule(private["private_route"], view_func=private["private_controller"])
app.add_url_rule(private["panel-delete_route"], view_func=private["panel-delete_controller"])
app.add_url_rule(private["invoicing_route"], view_func=private["invoicing_controller"])
app.add_url_rule(private["close-box_route"], view_func=private["close-box_controller"])
app.add_url_rule(private["config_route"], view_func=private["config_controller"])

#Cash register routes.
app.add_url_rule(private["cash-register-list_route"], view_func=private["cash-register-list_controller"])
app.add_url_rule(private["cash-register-edit_route"], view_func=private["cash-register-edit_controller"])

#Invoices routes.
app.add_url_rule(private["invoices-list_route"], view_func=private["invoices-list_controller"])

#User routes
app.add_url_rule(private["user-list_route"], view_func=private["user-list_controller"])
app.add_url_rule(private["user-edit_route"], view_func=private["user-edit_controller"])
app.add_url_rule(private["register_route"], view_func=private["register_controller"])
app.add_url_rule(private["logout_route"], view_func=private["logout_controller"])

#Customers routes.
app.add_url_rule(private["customer-add_route"], view_func=private["customer-add_controller"])

#Excel file route.
app.add_url_rule(private["load_route"], view_func=private["load_controller"])

#Products routes.
app.add_url_rule(private["add-products_route"], view_func=private["add-products_controller"])
app.add_url_rule(private["products-list_route"], view_func=private["products-list_controller"])
app.add_url_rule(private["products-edit_route"], view_func=private["products-edit_controller"])

#Categories routes.
app.add_url_rule(private["categories-list_route"], view_func=private["categories-list_controller"])
app.add_url_rule(private["categories-add_route"], view_func=private["categories-add_controller"])

""" 
    Handle erros.
"""
app.register_error_handler(public["not_found_route"], public["not_found_controller"])