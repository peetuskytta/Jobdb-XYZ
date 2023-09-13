from flask import Flask, render_template, request, jsonify
from dbsearch import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_keywords', methods=['POST'])

def process_keywords():
    if request.method == 'POST':
        keywords = request.form.get('keywords').split(' ')

        db_name = open_database("database/jobs.db")
        results = search_database(db_name, keywords)

        # add your keyword processing logic here, check in the SQLite database
        #print("Keywords:", keywords)
        return jsonify(results)

    #return "Keywords processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
