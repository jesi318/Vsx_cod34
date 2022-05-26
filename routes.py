
from app import app, db
from flask import render_template,redirect,url_for,flash,get_flashed_messages
import forms
from models import Task
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/')

@app.route('/about' , methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title = form.title.data , date = datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task added to db')
        return redirect(url_for('index'))
    return render_template('about.html', form=form, title = form.title.data)


    return render_template ('about.html', current_title="About page title", form=form)

@app.route('/links') 
def link():
    return render_template('links.html')


@app.route('/edit<int:task_id>', methods=["POST","GET"])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()

    #if task exists
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been successfully edited')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id= task_id)

    return redirect(url_for('index'))
