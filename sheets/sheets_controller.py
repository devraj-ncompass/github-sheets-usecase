from app import app
from flask import request, jsonify
from sheets.sheets_model import SheetsModel

sheets_model = SheetsModel()

@app.route("/sheets/update", methods=["POST"])
def update_sheet():
    try:
        # Get data from the request (assuming JSON format)
        data = request.json
        # Call the update_sheet method from SheetsModel
        sheets_model.update_sheet(data["column_values"])
        return jsonify({"message": "Sheet updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

