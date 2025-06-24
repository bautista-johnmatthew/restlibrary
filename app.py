from flask import Flask, request, jsonify, render_template
from flask_flatpages import FlatPages
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'templates'

app = Flask(__name__)
app.config.update(
    FLATPAGES_EXTENSION=FLATPAGES_EXTENSION,
    FLATPAGES_ROOT=FLATPAGES_ROOT,
    FLATPAGES_AUTO_RELOAD=True
)
PAGES = FlatPages(app)

@app.route('/', methods=['GET'])
def index():
    """Render the main page and documentation"""
    return render_template('index.html', pages = PAGES)

if __name__ == '__main__':
    app.run(debug=True)



