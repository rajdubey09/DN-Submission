from flask import Flask, render_template, request
from dataneuron_submission import *

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')

    else:
        sentence1 = str(request.form['sentence1'])
        sentence2 = str(request.form['sentence2'])
        sim_res = siml(sentence1,sentence2)

        return render_template('form.html', sim_score=int(sim_res))

if __name__=="__main__":
    app.run(debug=True)