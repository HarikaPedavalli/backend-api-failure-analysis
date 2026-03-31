from flask import Blueprint, jsonify, request
from services import get_all_reports, create_report

report_routes = Blueprint("report_routes", __name__)

@report_routes.route("/reports", methods=["GET"])
def get_reports():
    data = get_all_reports()
    if not data:
        return jsonify({"message": "No reports found", "reports": []}), 200
    return jsonify({"reports": data}), 200

@report_routes.route("/reports", methods=["POST"])
def add_report():
    result, status = create_report(request.json or {})
    if status != 201:
        return jsonify(result), status
    return jsonify({"message": "Report created successfully", "report": result}), status
