NBT.triggerChallenge = function(type) {
    const modal = document.createElement('div');
    modal.id = 'nbt-modal-overlay';
    modal.style = "position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);display:flex;justify-content:center;align-items:center;z-index:9999;";
    
    modal.innerHTML = `
        <div style="background:#fff;padding:20px;border-radius:8px;width:320px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.3);">
            <h3 style="margin:0 0 15px 0;font-family:sans-serif;">Verify Identity</h3>
            <div id="nbt-task-container">
                <img id="nbt-task-img" src="/nbt-image-task" style="width:100%;border:1px solid #ddd;">
                <input type="text" id="nbt-ans" style="width:90%;margin:15px 0;padding:8px;border:1px solid #ccc;">
                <div style="display:flex;justify-content:space-around;">
                    <button onclick="NBT.submitTask()">Verify</button>
                    <button onclick="NBT.playAudio()">Listen</button>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
};

NBT.submitTask = async function() {
    const ans = document.getElementById('nbt-ans').value;
    const res = await fetch('/nbt-check-task', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ answer: ans })
    });
    
    const data = await res.json();
    if (data.success) {
        document.getElementById('nbt-modal-overlay').remove();
        this.verify();
    }
};
