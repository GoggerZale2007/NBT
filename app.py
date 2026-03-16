from flask import Flask, request, jsonify, session
from nbt_logic import NBTValidator
from nbt_tasks import NBTTaskEngine
from nbt_security import NBTSecurity
import uuid

app = Flask(__name__)
app.secret_key = "ROCKETEER_FLASK_SESSION"

validator = NBTValidator(secret_key="NBT_PRIVATE_SHIELD_2026")
task_engine = NBTTaskEngine(asset_path="./assets")
nbt_sec = NBTSecurity(private_key="NBT_PRIVATE_SHIELD_2026")

@app.route('/nbt-verify', methods=['POST'])
def initial_verify():
    data = request.json
    session['sid'] = str(uuid.uuid4())
    
    result = validator.analyze_telemetry(data)
    
    if result["success"]:
        token = nbt_sec.sign_success(session['sid'])
        return jsonify({"success": True, "token": token})
    
    question, answer = task_engine.generate_math_challenge()
    session['nbt_ans'] = answer
    return jsonify({"success": False, "type": "visual_task", "question": question})

@app.route('/nbt-check-task', methods=['POST'])
def check_visual_task():
    user_ans = request.json.get('answer')
    actual_ans = session.get('nbt_ans')

    if actual_ans and user_ans == actual_ans:
        token = nbt_sec.sign_success(session.get('sid'))
        return jsonify({"success": True, "token": token})
    
    return jsonify({"success": False, "error": "Invalid response"})

@app.route('/submit', methods=['POST'])
def final_handler():
    token = request.form.get('nbt-response')
    if nbt_sec.verify_token(token):
        return "Human Verified: Form Processed."
    return "Verification Failed.", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
