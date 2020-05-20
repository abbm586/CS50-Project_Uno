from flask import Blueprint, render_template, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignupForm, UserLoginForm
from flask_login import current_user, login_user
from .models import Users, db
from . import login_manager

auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


#   ============================================
#       User Login
#   ============================================
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.default'))         # direct user if already logged in

    form = UserLoginForm()
    user = Users.query.filter_by(email=form.email.data).first()
    if user and user.check_password_hash(password=form.password.data):
        login_user(user)                                    # login the current user
        flash('Loggged in Successfully', 'success')
        return redirect(url_for('home_bp.default'))
    else:
        flash('email or Password incorrect', 'warning')

    return render_template('login.html',
                           title='Flask with Blueprint',
                           subtitle='User Account Login',
                           body='Login with User Account',
                           form=form)


#   ============================================
#       User Registration
#   ============================================
# noinspection PyArgumentList
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form_items = ('name', 'surname', 'email', 'password', 'confirm')
    form = SignupForm()
    if form.validate_on_submit():
        print('form validated : Register')
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            print('No User found, ready to continue')
            new_user = Users(name=form.name.data,
                             surname=form.surname.data,
                             smart_nr=form.smart_nr.data,
                             # occupation=form.occupation.data,
                             email=form.email.data,
                             bio=form.bio.data,
                             password=generate_password_hash(form.password.data, method='sha256'))
            # Users.set_password(password=form.password.data)          # hash the password
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created Successfully', 'success')
            return redirect(url_for('home_bp.default'))
        else:
            flash('Email already registered', 'warning')
    else:
        flash('Something went wrong. Please try again', 'alert')
        # return redirect(url_for('auth_bp.register'))

    return render_template('register.html',
                           title='Flask with Blueprint development',
                           subtitle='Create User Account',
                           form=form, form_items=form_items)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return Users.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('Logged in required to continue')
    return redirect(url_for('auth_bp.login'))