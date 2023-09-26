from flask import Flask, render_template, request, jsonify
from dbsearch import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_keywords', methods=['POST'])

def process_keywords():
    if request.method == 'POST':
        keywords = request.form.get('keywords')
        keywords = keywords.split(' ')
        keywords = list(map(str.lower, keywords))
        db_name = open_database("/opt/database/jobs.db")
        if db_name != None:
            results = search_database(db_name, keywords)
            # create a dict with the results?
            return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)