
from app import app
from flask import render_template
import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title="New Index Title")

@app.route('/')

@app.route('/about' , methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        return render_template('about.html', form=form, title = form.title.data)

    return render_template ('about.html', current_title="About page title", form=form)

@app.route('/links') 
def link():
    return render_template('links.html')