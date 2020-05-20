from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    headline = "First Web"
    return render_template("homepage.html", headline=headline)

@app.route("/graphic1")
def graphic1():
    headline = "Graphic"
    return render_template("graphic1.html", headline=headline)
@app.route("/graphic2")
def graphic2():
    headline = "Graphic2"
    return render_template("graphic2.html", headline=headline)
@app.route("/graphic3")
def graphic3():
    headline = "Graphic3"
    return render_template("graphic3.html", headline=headline)
@app.route("/graphic4")
def graphic4():
    headline = "Graphic4"
    return render_template("graphic4.html", headline=headline)
@app.route("/graphic5")
def graphic5():
    headline = "Graphic5"
    return render_template("graphic5.html", headline=headline)
@app.route("/graphic6")
def graphic6():
    headline = "Graphic6"
    return render_template("graphic6.html", headline=headline)

if __name__=="__main__":
    app.run()