from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/std', methods=['GET'])
def get_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/std/<student_id>', methods=['GET'])
def get_specific_person(student_id):
    with open("data.json", "r") as f:
        data = json.load(f)
        for person in data["student"]:
            if person["roll_no"] == int(student_id):
                return jsonify(person)
        return jsonify({"message": "Person not found"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
