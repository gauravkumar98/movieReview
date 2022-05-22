from flask import Flask, render_template, request
import pickle

#loading machine learning module for predicting the review is positive or negative
def sentiment_review(review):
    if review is None or review == "":
        return "Try again"
    with open("model.pickle",'rb') as f:
        pkl = pickle._Unpickler(f)
        pkl.encoding = 'latin1'
        model = pkl.load()
        cv = pkl.load()
    pred = model.predict(cv.fit_transform([review]))
    if pred[0] == 0:
        return "Negative"
    else:
        return "Positive"
app = Flask(__name__)

#index page
@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

#results page
@app.route('/results.html',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        print(request.form['result'])
        prediction = sentiment_review(request.form['result'])
        if prediction=='Positive':
            linker = "static/thumb-up.png"
        else:
            linker = "static/thumb-down.png"
        return render_template('results.html', value=prediction, linker=linker)

#main
if __name__ == "_main_":
    app.run(debug=True)
