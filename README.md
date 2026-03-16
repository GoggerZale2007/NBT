NBT (No Bots Test) v1.0
​A modular, privacy-first bot detection engine. This repository contains the core logic, security protocols, and task generation needed to implement an invisible human-verification system.
​File Overview
​app.py – The main entry point and local API for the NBT engine.
index.html – The frontend demonstration and implementation page.
nbt.js & nbt_modal.js – Frontend scripts handling telemetry and UI interactions.
nbt.css – Styling for the NBT widget and modal interface.
nbt_logic.py – The core behavioral analysis algorithms.
nbt_security.py – Handles HMAC signing and cryptographic token validation.
nbt_tasks.py & nbt_audio.py – Generates visual and audio challenges for suspicious users.
​Implementation Guide
​1. Deployment
Copy all files to your server directory. Ensure you have Flask installed to run the backend components.
​2. Frontend Setup
Include nbt.css, nbt.js, and nbt_modal.js in your HTML. The system uses a simple initialization:
NBT.init('#your-element-id')
​3. Server-Side Verification
The app.py uses nbt_security.py to sign every successful human verification. To verify a user on your own routes, import the validator logic from nbt_security.py and check the submitted token using your private key (Format: NBTabcd1234...).
​Security Architecture
​Behavioral Analysis
The nbt_logic.py file analyzes mouse movements and timing to distinguish between human users and automated scripts without using cookies.
​Cryptographic Integrity
nbt_security.py ensures that once a user is verified, the resulting token is tamper-proof and time-bound (valid for 600 seconds).
​Multi-Modal Challenges
If telemetry is inconclusive, nbt_tasks.py and nbt_audio.py provide fallback challenges to ensure accessibility while maintaining high security.
