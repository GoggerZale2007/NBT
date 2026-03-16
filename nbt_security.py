import hmac
import hashlib
import time
import base64

class NBTSecurity:
    def __init__(self, private_key):
        self.key = private_key

    def sign_success(self, session_id):
        timestamp = str(int(time.time()))
        message = f"{session_id}:{timestamp}"
        signature = hmac.new(
            self.key.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        
        token = base64.b64encode(f"{message}:{signature}".encode()).decode()
        return token

    def verify_token(self, token, max_age=300):
        try:
            decoded = base64.b64decode(token).decode()
            message, timestamp, signature = decoded.rsplit(':', 2)
            
            if int(time.time()) - int(timestamp) > max_age:
                return False

            expected = hmac.new(
                self.key.encode(),
                f"{message}:{timestamp}".encode(),
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(expected, signature)
        except:
            return False
          
