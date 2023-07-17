from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/guest', methods=["POST"])
def Guest():
    p=request.form["a"]
    #print(p)
    return render_template("index.html",y=p)


@app.route('/user')
def User():
    return'Hello User Welcome'

if __name__=='__main__':
    app.run(debug=False)