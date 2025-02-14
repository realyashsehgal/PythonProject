from flask import Flask, render_template, request, redirect, url_for
from Config import Config
from DbManager import add_jobs
import os


# pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config.from_object(Config)
UPLOAD_FOLDER = 'UPLOAD_FOLDER/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate the admin credentials
        if username == "yash" and password == "123":

            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid credentials! Please try again."
    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')




@app.route('/Job_Adding',methods=['POST'])
def updatejobs():
    title = request.form['title']
    description = request.form['description']
    skills = request.form['skills']
    date = request.form['date']
    link = request.form['link']

    add_jobs(title, description, skills, date,link)
    return render_template('admin_dashboard.html')






@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    print("i ran")
    if 'file' not in request.files:
        print("Debug: File not found ")
        return redirect(request.url)
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return "File uploaded successfully!"
    print("Mil gayi")
    return render_template('results.html')

@app.route('/results')
def results():
    return render_template('results.html')
if __name__ == '__main__':
    app.run(debug=True)