"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from forms import ProfileForm
import datetime

from app import db
from app.models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    profileForm = ProfileForm()
    
    if request.method == 'POST' and profileForm.validate_on_submit():
        first = profileForm.firstname.data
        last = profileForm.lastname.data
        gender = profileForm.gender.data
        email = profileForm.email.data
        location = profileForm.location.data
        bio = profileForm.biography.data
        
        photo = request.files['photo']
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        userId = createId(first,last,gender)
        created_on = date_joined()
        
        profile = UserProfile(userid = userId,firstname = first,lastname = last,gender = gender,email = email,location = location,biography = bio,date = created_on,photo = filename)
        db.session.add(profile)
        db.session.commit()
        
        flash('Your profile was saved successfully', 'success')
        return redirect(url_for('home'))
        
    flash_errors(profileForm)
    return render_template('profile.html',form=profileForm)

@app.route('/profiles')
def profiles():
    users = UserProfile.query.all()
    return render_template('profiles.html', users=users)

@app.route('/profiles/<userId>')
def userProfile(userId):
    """Render the website's about page."""
    user = UserProfile.query.get(userId)
    return render_template('userProfile.html', user=user)



###
# The functions below should be applicable to all Flask apps.
###

def createId(first,last,gender):
    fname = first[:4]
    middle = gender[:1]
    lname = last[:4]
    id = fname+middle.upper()+lname
    return id
    
def date_joined():
    date = datetime.date.today().strftime("%B %d, %Y")
    return "Joined" + date

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
