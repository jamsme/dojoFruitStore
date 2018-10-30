from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    sberry = int(request.form['strawberry'])
    rberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    sum = sberry + rberry + apple
    print('Total', sum)
    return render_template("checkout.html", anything = sum)

if __name__=="__main__":   
    app.run(debug=True)    