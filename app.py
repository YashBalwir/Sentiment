from flask import *  
import pandas
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("index.html")  
 

@app.route('/visualize', methods = ['POST'])
def Stocks():
    if request.method == 'POST':  
        f = request.files['file']  
        f.save('data.csv') 
    filename = 'data.csv'
    data = pandas.read_csv(filename, header=0)
    stocklist = list(data.values)
    return render_template('visualize.html', name = f.filename, stocklist=stocklist)

if __name__ == '__main__':  
    app.run(debug = True)  