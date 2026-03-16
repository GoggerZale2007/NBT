import random
import os
from PIL import Image, ImageDraw, ImageFont

class NBTTaskEngine:
    def __init__(self, asset_path):
        self.asset_path = asset_path

    def generate_math_challenge(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        op_char = random.choice(list(ops.keys()))
        
        answer = ops[op_char](a, b)
        question = f"What is {a} {op_char} {b}?"
        
        return question, str(answer)

    def create_distorted_image(self, text):
        img = Image.new('RGB', (250, 100), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        
        for i in range(100):
            d.point((random.randint(0, 250), random.randint(0, 100)), fill=(0, 0, 0))
            
        for i in range(5):
            d.line((random.randint(0, 250), 0, random.randint(0, 250), 100), fill=(128, 128, 128))

        f = ImageFont.load_default()
        d.text((50, 40), text, fill=(0, 0, 0), font=f)
        
        return img
      
