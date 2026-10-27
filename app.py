from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'megha_hospitals_secret_key'

# Dummy in-memory database
users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email in users and users[email]['password'] == password:
            session['user'] = users[email]['full_name']
            flash('Login Successful! Welcome to Megha Hospitals.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid Email or Password. Please try again.', 'danger')
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        
        if email in users:
            flash('Email already registered! Please login.', 'warning')
            return redirect(url_for('login'))
        
        users[email] = {
            'full_name': full_name,
            'phone': phone,
            'password': password
        }
        flash('Registration Successful! Please login to your account.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)