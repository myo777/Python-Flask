from flask import Flask, render_template 
import PyPDF2 as p2
object = open('sample.pdf','rb')
reader = p2.PdfFileReader(object)
reader = p2.PdfFileReader(object)
page = reader.getPage(0)
page.extractText()
page = reader.getPage(1)
simple = page.extractText()



app = Flask(__name__)


@app.route("/")
def templates():
	
	return render_template("templates.html")


@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")
# @app.route("/")
# def index():
#     return "<h1>Hello, World!!!!</h1>"

# @app.route("/salvador")
# def salvador():
#     return "Hello, Salvador"

# @app.route("/about")
# def about():
#     return "This is about page!"

# @app.route("/Allpost")
# def Allpost():
#     return "This is post page"

# @app.route("/<string:name>")
# def hello(name):
#      name = name.capitalize()
#     return f"<h1>Hello, {name}!</h1>"



if __name__ == "__main__":
    app.run(debug=True)



