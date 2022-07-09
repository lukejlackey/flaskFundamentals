from flask import Flask, render_template
app = Flask(__name__)

def displayGrid(x,y,mainColor='red', secondaryColor='black'):
    return render_template('index.html', x=x, y=y, mainColor=mainColor, secondaryColor=secondaryColor)

@app.route('/')
def d8x8():
    return displayGrid(8,8)

@app.route('/<mainColor>/<secondaryColor>')
def d8x8Color(mainColor, secondaryColor):
    return displayGrid(8,8,mainColor,secondaryColor)

@app.route('/4')
def d4x4():
    return displayGrid(4,4)

@app.route('/4/<mainColor>/<secondaryColor>')
def d4x4Color(mainColor, secondaryColor):
    return displayGrid(4,4,mainColor, secondaryColor)

@app.route('/<x>.<y>')
def dCustom(x, y):
    return displayGrid(int(x), int(y))

@app.route('/<x>.<y>/<mainColor>/<secondaryColor>')
def dCustomColor(x, y, mainColor, secondaryColor):
    return displayGrid(int(x), int(y), mainColor, secondaryColor)

if __name__=="__main__":
    app.run(debug=True)