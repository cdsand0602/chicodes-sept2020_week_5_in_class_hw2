# Import the app variable from the init
from hw2 import app

# Import specific packages from flask
from flask import render_template,request

# Import Our Forms(s)
from hw2.forms import UserInfoForm

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')


        
 # GET == Gathering Info
# POST == Sending Info
@app.route('/avenger', methods = ['GET','POST'])
def avenger():
    # Init our Form
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes from the form
        print(name,phone,email,password)
               
    return render_template('avenger.html',user_form = form)