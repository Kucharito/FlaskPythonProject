from flask import request

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.forms import ExpenseForm
from app.models import Expense

expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@expenses_bp.route('/')
@login_required
def list_expenses():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('expenses_dashboard.html', expenses=expenses)

@expenses_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_expenses():
    form = ExpenseForm()
    print("DEBUG | Is form submitted?", form.is_submitted())
    print("DEBUG | Is form validated?", form.validate_on_submit())
    print("DEBUG | Errors:", form.errors)

    if form.validate_on_submit():
        new_expense = Expense(
            amount=form.amount.data,
            category=form.category.data,
            description=form.description.data,
            date=form.date.data,
            user_id=current_user.id
        )
        db.session.add(new_expense)
        db.session.commit()
        print("DEBUG | Uložil som expense")
        flash('Expense added successfully.', 'success')
        return redirect(url_for('expenses.list_expenses'))
    print("Raw request form data:", request.form)
    print("Form date field data:", form.date.data)

    return render_template('expense_form.html', form=form)

