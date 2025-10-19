from flask import Blueprint, flash, redirect, url_for, render_template
from werkzeug.security import generate_password_hash

from app import db
from app.forms import RegisterForm
from app.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return "Login Page"

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered.', 'danger')
            return redirect(url_for('auth.register'))

        new_user = User(
            name = form.username.data,
            email = form.email.data,
            password = generate_password_hash(form.password.data)
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
@auth_bp.route('/logout')
def logout():
    return "Logout Page"