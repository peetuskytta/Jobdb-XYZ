from flask import Flask, render_template, request, jsonify
from dbsearch import *
import logging
import datetime

app = Flask(__name__)
log_file = 'app.log'
handler = logging.FileHandler(log_file)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_keywords', methods=['POST'])

def process_keywords():
    if request.method == 'POST':
        data = request.get_json()
        keywords = data.get('keywords')
        keywords = keywords.split()
        #keywords = list(map(str.lower, keywords))
        db_name = open_database("database/jobs.db")

        #client_ip = request.remote_addr
        #current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #app.logger.info(f'Received request at {current_time} from {client_ip}')

        if db_name != None:
            results = search_database(db_name, keywords)
            return jsonify(results)

@app.route('/contacts.html')
def contacts():
    # Renders the "contacts.html" template when About link is clicked
    return render_template('contacts.html')

#@app.route('/project')
#def project():
    #Renders the "project.html" template when project link is clicked
    #return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
