from flask import Flask, request, jsonify, render_template
from models import insert_feedback, get_all_feedback

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    username = data.get("username")
    message = data.get("message")
    insert_feedback(username, message)
    return jsonify({"message": "Feedback submitted successfully!"}), 201

@app.route("/feedback", methods=["GET"])
def view_feedback():
    feedbacks = get_all_feedback()
    return jsonify(feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
