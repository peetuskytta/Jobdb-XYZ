from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        keywords = request.form.get('keywords').split(',')

        # add your keyword processing logic here
        print("Email:", email)
        print("Keywords:", keywords)
        # You can send an email with the processed result here

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
