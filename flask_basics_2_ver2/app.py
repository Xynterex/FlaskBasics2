from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

valid_animals = ["chickens", "ducks", "pandas"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chickens")
def chicken_info():
    return render_template("chickens.html")

@app.route("/ducks")
def duck_info():
    return render_template("ducks.html")

@app.route("/pandas")
def panda_info():
    return render_template("pandas.html")

'''
# store directory as a new variable
@app.route("/<animal>")
def animal_info(animal):
    if animal in valid_animals:
        return render_template(f"{animal}.html")
    else:
        return redirect(url_for("home"))
'''

if __name__ == "__main__":
    app.run(debug=True, port=12345)
