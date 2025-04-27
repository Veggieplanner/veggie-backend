from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/generate-plan", methods=["GET"])
def generate_plan():
    return jsonify({"message": "VeggiePlanner API funktioniert!"})
