from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/routes")
def show_routes():

    data = open("data.json").read()
    json_data = json.loads(data)

    return jsonify(json_data)


@app.route("/api/routes", methods=["POST"])
def update_routes():
    print(request.form)
    return "Rutas actualizadas"


if __name__ == "__main__":
    app.run(debug=True)
