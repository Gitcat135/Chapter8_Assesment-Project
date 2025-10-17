from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import RegisterForm, AddproductForm

@app.route('/')
@app.route('/shop')
def shop():
    """Shop URL"""
    return render_template('shop.html', title='Shop Page')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Add Product URL"""
    form = AddproductForm()
    if form.validate_on_submit():
        flash(f'Your Product has been saved.')
        return redirect(url_for('shop'))
    return render_template('add_product.html', title='Add Product Page',  form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You have been Registerd.')
        return redirect(url_for('shop'))
    return render_template('register.html', title='Register', form=form)
