from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index_helios_W_r24.html")

if __name__ == "__main__":
    app.run(debug=True)
