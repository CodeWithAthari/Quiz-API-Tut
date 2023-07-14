from flask import Flask, jsonify, request
import core_database

app = Flask(__name__)


@app.route('/get_all_cat')
def get_all_cat():
    result = core_database.get_categories()
    return jsonify({"status": True, "message": "Found", "data": result})



@app.route('/get_quizes')
def get_quizes():
    cat_id = request.args.get("cat_id")
    if not cat_id:
        return jsonify({"status": False, "message": "No Cat Id", "data": None})

    if not cat_id.isdigit():
        return jsonify({"status": False, "message": "Invalid cat id", "data": None})

    cat_id = int(cat_id)
    result = core_database.get_quiz_by_cat(cat_id)
    if result:
        return jsonify({"status": True, "message": "Found", "data": result})
    return jsonify({"status": False, "message": "No Data Found", "data": None})


if __name__ == '__main__':
    app.run(debug=True)
