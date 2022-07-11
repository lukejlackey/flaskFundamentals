
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'l0Lc@n+HacKm3'

results = {}

@app.route('/')
def displaySurvey():
    return render_template('survey.html')


@app.route('/result')
def displayResults():
    return render_template('results.html', results=results)


@app.route('/process', methods=['POST'])
def processResults():
    for item in ['name','loc','favLang','comment']:
        for (data, grp) in [(session, request.form), (results, session)]:
            data[item] = grp[item]
            print(data[item])
    return redirect('/result')



if __name__=="__main__":
    app.run(debug=True)