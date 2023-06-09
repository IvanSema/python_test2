import csv
from flask import Flask, url_for, render_template, request, redirect
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', new_line='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writter = csv.writer(database2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again.'