from flask import Flask, render_template, request, jsonify

# Point Flask to your 'Templets' folder where index.html is located
app = Flask(__name__, template_folder='Templets')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Returns default forecast if called
    return jsonify({"prediction": -1.06})

if __name__ == "__main__":
    app.run(debug=True, port=5000)