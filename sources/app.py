from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_keywords', methods=['POST'])

def process_keywords():
    if request.method == 'POST':
        keywords = request.form.get('keywords').split(' ')

        
        # add your keyword processing logic here, check in the SQLite database
        #print("Keywords:", keywords)
        return jsonify(keywords)

    return "Keywords processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
