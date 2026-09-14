from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json
    expression = data["expression"]

    try:
        # Evaluación simple (controlada por frontend)
        result = eval(expression)

    except:
        result = "Error"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)