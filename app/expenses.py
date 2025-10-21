from flask import request

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.forms import ExpenseForm
from app.models import Expense

expenses_bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@expenses_bp.route('/',methods =['GET'])
@login_required
def list_expenses():
    category_filter = request.args.get('category','')
    if category_filter:
        expenses = Expense.query.filter(
            Expense.user_id == current_user.id,
            Expense.category.ilike(f'%{category_filter}%')
        ).all()
    else:
        expenses = Expense.query.filter_by(user_id=current_user.id).all()

    form = ExpenseForm()
    return render_template('expenses_dashboard.html', expenses=expenses, category_filter=category_filter, form = form)

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


@expenses_bp.route('/delete/<int:expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    if expense.user_id != current_user.id:
        flash('You do not have permission to delete this expense.', 'danger')
        return redirect(url_for('expenses.list_expenses'))

    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully.', 'success')
    return redirect(url_for('expenses.list_expenses'))


@expenses_bp.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    expense = Expense.query.filter_by(id=expense_id, user_id=current_user.id).first_or_404()
    form = ExpenseForm(obj=expense)

    if form.validate_on_submit():
        expense.amount = form.amount.data
        expense.category = form.category.data
        expense.description = form.description.data
        expense.date = form.date.data
        db.session.commit()
        flash('Expense updated successfully.', 'success')
        return redirect(url_for('expenses.list_expenses'))
    return render_template('expense_form.html', form=form, edit_mode=True)