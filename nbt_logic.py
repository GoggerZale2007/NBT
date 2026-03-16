import time
import hmac
import hashlib
import json

class NBTValidator:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def analyze_telemetry(self, data):
        score = 0
        
        m_moves = data.get('m', 0)
        duration = data.get('d', 0)
        is_webdriver = data.get('v', False)

        if is_webdriver:
            return {"success": False, "type": "hard_challenge"}

        if m_moves > 5:
            score += 1
        
        if 0.8 < duration < 300:
            score += 1

        if score >= 2:
            token = self.generate_token()
            return {"success": True, "token": token}
        else:
            return {"success": False, "type": "visual_task"}

    def generate_token(self):
        payload = f"{time.time()}-{self.secret_key}"
        return hmac.new(
            self.secret_key.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()
        
