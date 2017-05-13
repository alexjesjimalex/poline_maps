from flask import Flask, request, render_template, jsonify
# usar pyodbc => sql server
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# API: Endpoint - GET
@app.route("/api/routes")
def show_routes():
    # consulta y manejar una estructura de lista -> diccionario
    routes = [
        {"lat": -10.0464108, "lng": -74.7593884},
        {"lat": -10.0464108, "lng": -74.7593884},
        {"lat": -10.0464108, "lng": -74.7593884},
        {"lat": -10.0464108, "lng": -74.7593884},
        {"lat": -10.0464108, "lng": -74.7593884},
    ]

    return jsonify({"routes": routes})

# curl -i -X POST localhost:5000/routes
@app.route("/api/routes", methods=["POST"])
def update_routes():
    print(request.form)
    return "Rutas actualizadas"

if __name__ == "__main__":
    app.run(debug=True)
