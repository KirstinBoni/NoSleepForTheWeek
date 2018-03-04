from flask import Flask, render_template, request

from user import User

app = Flask(__name__)
user = User()


@app.route('/')
@app.route('/#')
def index():
    """Renders the home page."""
    return render_template(
        'index.html'
    )


@app.route('/user', methods=['GET', 'POST'])
def userSettings():
    """Renders the alarm settings page."""
    if request.method == 'POST':
        user = User(email=request.form['email'], age=request.form['age'])
    return render_template(
        'alarm-settings.html', username=user
    )


if __name__ == '__main__':
    app.run()
