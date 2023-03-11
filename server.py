from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "dojosecretfruitthatisnotsecretatall"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/order', methods=['POST', 'GET'])         
def order():
    print(request.form)
    # looping through lists reduces work when inventory changes
    total_qty = 0
    fruit = ['apple','blackberry','raspberry','strawberry']
    for item in fruit:
        session[item] = request.form[item]
        total_qty += int(session[item]) # we can go ahead and total the order in the loop as well
    customer = ['first_name','last_name','student_id']
    for item in customer:
        session[item] = request.form[item]
    print(f"Charging {session['first_name']} {session['last_name']}'s account for {total_qty} fruit")
    return redirect('/checkout')

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    