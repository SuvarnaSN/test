from flask import Flask, render_template, request, redirect

app = Flask(__name__)


users = {
    'user1': 'Password1',
    'user2': 'Password2',
    'user3': 'Password3'
}


def check_password_requirements(password):
    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not password[-1].isdigit():
        return False
    return True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        
        if username in users and check_password_requirements(password):
            return redirect('/report?pass=1')
        else:
            return redirect('/report?pass=0')

    return render_template('index.html')


@app.route('/report')
def report():
    passed = request.args.get('pass')
    if passed == '1':
        message = "Password passed the requirements."
    else:
        message = "Password does not meet the requirements."

    return render_template('report.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
