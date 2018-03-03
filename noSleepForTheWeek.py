from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'layout.html'
    )


if __name__ == '__main__':
    app.run()
