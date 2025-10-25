from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user




budgets_bp = Blueprint('budgets', __name__, url_prefix='/budgets')

@budgets_bp.route('/', methods=['GET', 'POST'])
@login_required
def list_budgets():
    from app import db
    from app.models import Budget
    from sqlalchemy import func
    from app.forms import BudgetForm
    from app.models import Expense

    form = BudgetForm()
    budgets = Budget.query.filter_by(user_id=current_user.id).all()

    if form.validate_on_submit():
        new_budget = Budget(
            category=form.category.data,
            limit=form.limit.data,
            user_id=current_user.id
        )
        db.session.add(new_budget)
        db.session.commit()
        flash('Budget added successfully!', 'success')
        return redirect(url_for('budgets.list_budgets'))

    budgets_data = []
    for b in budgets:
        total_spent = db.session.query(func.sum(Expense.amount)).filter(
            Expense.user_id == current_user.id,
            Expense.category == b.category
        ).scalar() or 0

    remaining = float(b.limit) - total_spent
    percent_used = (total_spent / b.limit * 100) if b.limit > 0 else 0

    budgets_data.append({
        'category': b.category,
        'limit': b.limit,
        'total_spent': total_spent,
        'remaining': remaining,
        'percent_used': percent_used
    })

    return render_template('budgets_dashboard.html', budgets=budgets_data, form=form)
