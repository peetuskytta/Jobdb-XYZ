from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_keywords', methods=['POST'])
def process_keywords():
    email = request.form.get('email')
    keywords = request.form.get('keywords').split(',')

    # add keyword processing logic here
    print("Email:", email)
    print("Keywords:", keywords)

    # You can send an email with the processed result here

    return "Keywords processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
