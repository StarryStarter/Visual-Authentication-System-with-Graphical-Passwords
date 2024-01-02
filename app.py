from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_sqlalchemy import SQLAlchemy


import base64
import hashlib


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.db'  
db = SQLAlchemy(app)
app.SECRET_KEY= 'secret'
MAX_LOGIN_ATTEMPTS = 4
MAX_LOGIN_ATTEMPTS1 = 1
MAX_LOGIN_ATTEMPTS2 = 2
MAX_LOGIN_ATTEMPTS3 = 3


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(50), unique=True, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    data1 = db.Column(db.LargeBinary, nullable=False)
    data2 = db.Column(db.LargeBinary, nullable=False)
    data3 = db.Column(db.LargeBinary, nullable=False)
    data4 = db.Column(db.LargeBinary, nullable=False)
    data5 = db.Column(db.LargeBinary, nullable=False)
    data6 = db.Column(db.LargeBinary, nullable=False)
    data7 = db.Column(db.LargeBinary, nullable=False)
    data8 = db.Column(db.LargeBinary, nullable=False)
    
    
    

    def __init__(self,name,email,data,data1,data2,data3,data4,data5,data6,data7,data8):
        self.name=name
        self.email=email
        self.data=data
        self.data1=data1
        self.data2=data2
        self.data3=data3
        self.data4=data4
        self.data5=data5
        self.data6=data6
        self.data7=data7
        self.data8=data8
        

   
    
with app.app_context():
        db.create_all()


def hash_image_data(image_data):
    return hashlib.md5(image_data).hexdigest()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    
    if request.method == 'POST':
        name = request.form['name']
        email= request.form['email']
        file = request.files['file']
        file1= request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        file4= request.files['file4']
        file5 = request.files['file5']
        file6 = request.files['file6']
        file7 = request.files['file7']
        file8 = request.files['file8']

        # If the user does not select a file, the browser may submit an empty file without a filename
        if file.filename == '':
            e7="please select images !!"
            return render_template('register.html', error=e7)
        

        try:
            # Get the binary data from the file
            binary_data = file.read()
            binary_data1 = file1.read()
            binary_data2 = file2.read()
            binary_data3 = file3.read()
            binary_data4 = file4.read()
            binary_data5 = file5.read()
            binary_data6 = file6.read()
            binary_data7 = file7.read()
            binary_data8 = file8.read()

            # Save the binary data to the database
            new_user = User(name=name,email=email, data=binary_data,data1=binary_data1,data2=binary_data2,data3=binary_data3,data4=binary_data4,data5=binary_data5,data6=binary_data6,data7=binary_data7,data8=binary_data8)
            db.session.add(new_user)
            db.session.commit()

            return redirect('/order')
        except Exception as e:
            e9="User Already Exist"
            return render_template('index.html', error=e9)

      
        

       

        
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']

        file=request.files['file']
        files=file.read()

        file1=request.files['file1']
        files1=file1.read()

        file2=request.files['file2']
        files2=file2.read()

        file3=request.files['file3']
        files3=file3.read()

        file4=request.files['file4']
        files4=file4.read()

        file5=request.files['file5']
        files5=file5.read()

        file6=request.files['file6']
        files6=file6.read()

        file7=request.files['file7']
        files7=file7.read()

        file8=request.files['file8']
        files8=file8.read()
        

        # bdata=file1.read()

        # hashed_password = bcrypt.hashpw(bdata, bcrypt.gensalt())
        
        with app.app_context():
            user = User.query.filter_by(email=email).first()
            if user:

        
       
       
                stored_image_data = user.data
                stored_image_data1 = user.data1
                stored_image_data2 = user.data2
                stored_image_data3 = user.data3
                stored_image_data4 = user.data4
                stored_image_data5 = user.data5
                stored_image_data6 = user.data6
                stored_image_data7 = user.data7
                stored_image_data8 = user.data8
            else:

                error6="Email Does't Match ,Please Try Again !!"
                return render_template('order.html', error=error6)
         

        if files+files1+ files2+ files3+ files4+ files5+ files6+ files7+ files8==stored_image_data +stored_image_data1+stored_image_data2+stored_image_data3+stored_image_data4+stored_image_data5+stored_image_data6+stored_image_data7+stored_image_data8:
         
            session.pop(f'login_attempts_{email}', None)
            session['authenticated'] = True
            session['user_email'] = email 
            flash('Login successful!', 'success')
            return redirect('/dashboard')
        else:
            # Increment the unsuccessful attempts counter
            login_attempts = session.get(f'login_attempts_{email}', 0) + 1
            session[f'login_attempts_{email}'] = login_attempts
            if login_attempts == MAX_LOGIN_ATTEMPTS1:
                error1="wrong order!!  ,3 more attempts left!!"
                return render_template('order.html', error=error1)
            if login_attempts == MAX_LOGIN_ATTEMPTS2:
                error1="wrong order!!  2 more attempts left!!"
                return render_template('order.html', error=error1)
            elif login_attempts == MAX_LOGIN_ATTEMPTS3:
                error2="wrong order!!  1 more attempts left!!"
                return render_template('order.html', error=error2)
            # Check if the maximum attempts limit has been reached
            if login_attempts >= MAX_LOGIN_ATTEMPTS:
                with app.app_context():
                    data_to_delete = User.query.filter_by(email=email)  # Specify your filter criteria
                    data_to_delete.delete()
                    db.session.commit()
                flash('Too many unsuccessful login attempts. Your account is locked.', 'danger')
                
                errors="your account is blocked since you have reached the limit"      # You may want to log or notify about the account lockout here
                return render_template('order.html' , error=errors)
            else:
                flash('Incorrect username or password. Attempt {}/{}'.format(login_attempts, MAX_LOGIN_ATTEMPTS), 'danger')

    return render_template('order.html')
            # flash('Login successful!', 'success')
            
            # return redirect(url_for('dashboard'))
        # else:
        #     errors="invalid id ,please try again"
        #     return render_template('login.html', error=errors)
        
        
    
    # return render_template('login.html')





@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/user_images/<email>')
def user_images(email):
    user = User.query.filter_by(email=email).first()

    if user:
        image_data_base64 = base64.b64encode(user.data).decode('utf-8')
        image_data_base641 = base64.b64encode(user.data1).decode('utf-8')
        image_data_base642 = base64.b64encode(user.data2).decode('utf-8')
        image_data_base643 = base64.b64encode(user.data3).decode('utf-8')
        image_data_base644 = base64.b64encode(user.data4).decode('utf-8')
        image_data_base645 = base64.b64encode(user.data5).decode('utf-8')
        image_data_base646 = base64.b64encode(user.data6).decode('utf-8')
        image_data_base647 = base64.b64encode(user.data7).decode('utf-8')
        image_data_base648 = base64.b64encode(user.data8).decode('utf-8')

        return render_template('user_images.html', image_data_base641=image_data_base641, image_data_base64=image_data_base64 ,image_data_base642=image_data_base642 ,image_data_base643=image_data_base643 ,image_data_base644=image_data_base644 ,image_data_base645=image_data_base645 ,image_data_base646=image_data_base646,image_data_base647=image_data_base647, image_data_base648=image_data_base648)
    error5="No User Found !!"
    return render_template('order.html',error=error5)


@app.route('/dashboard')
def dashboard():
    # Check if the user is authenticated
    if 'authenticated' not in session or not session['authenticated']:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))

    print("User is authenticated!")  # Add this line for debugging

    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()

    # Redirect to the login page or any other desired page
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
