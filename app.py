from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def predict1():
    return render_template('predict1.html')


if __name__ == "__main__":
    app.run(debug=False)
