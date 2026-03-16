from flask import Flask, request, jsonify
from nbt_logic import NBTValidator

app = Flask(__name__)
validator = NBTValidator(secret_key="ROCKETEER_PRIVATE_KEY")

@app.route('/nbt-verify', methods=['POST'])
def verify():
    data = request.json
    if not data:
        return jsonify({"success": False, "type": "error"}), 400

    result = validator.analyze_telemetry(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
