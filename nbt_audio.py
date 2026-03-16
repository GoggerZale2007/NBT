from gtts import gTTS
import io

def generate_audio_challenge(text):
    tts = gTTS(text=f"Your code is {text}", lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp
  
