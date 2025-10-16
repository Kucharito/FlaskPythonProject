from flask import Blueprint
expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@expenses_bp.route('/')
def list_expenses():
    return "List of Expenses"