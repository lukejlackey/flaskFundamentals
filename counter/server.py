from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'l0Lc@n+HacKm3'

@app.route('/')
def displayCounter():
    if 'visits' in session:
        session['visits'] += 1
        session['actual_visits'] +=1
    else:
        session['visits'] = 1
        session['actual_visits'] = 1
    return render_template('index.html', visits=session['visits'], actual_visits=session['actual_visits'])

@app.route('/add_count', methods=['POST'])
def addToCounter():
    if request.form['i'] != '':
        session['visits'] += int(request.form['i']) - 1
    return redirect('/')

@app.route('/destroy_session')
def resetCounter():
    session['visits'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)