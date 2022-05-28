from flask import Flask, render_template, url_for, flash, redirect


from forms import RegistrationForm, LoginForm


import dbconn


def register(user):
    if dbconn.add_user(user):
        flash(f'Account created for {user.username}!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', title='Login')

def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)