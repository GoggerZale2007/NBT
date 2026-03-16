const NBT = {
    _m: 0,
    _t: Date.now(),
    _status: 'ready',

    init: function(selector) {
        const target = document.querySelector(selector);
        if (!target) return;

        target.innerHTML = `
            <div class="nbt-container">
                <div class="nbt-checkbox-area" id="nbt-anchor">
                    <div class="nbt-spinner" id="nbt-s"></div>
                    <div class="nbt-check-icon" id="nbt-c">✔</div>
                </div>
                <div class="nbt-label">I'm not a robot</div>
                <div class="nbt-logo-box">
                    <img src="nbt-logo.png" alt="">
                    <div class="nbt-brand-text">NBT</div>
                </div>
            </div>
        `;

        document.addEventListener('mousemove', () => this._m++);
        document.addEventListener('touchstart', () => this._m += 5);
        document.getElementById('nbt-anchor').addEventListener('click', () => this.verify());
    },

    verify: async function() {
        if (this._status !== 'ready') return;

        const s = document.getElementById('nbt-s');
        const c = document.getElementById('nbt-c');
        const a = document.getElementById('nbt-anchor');

        this._status = 'loading';
        s.style.display = 'block';
        
        const payload = {
            m: this._m,
            d: (Date.now() - this._t) / 1000,
            v: window.navigator.webdriver || false
        };

        try {
            const res = await fetch('/nbt-verify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            const result = await res.json();

            if (result.success) {
                s.style.display = 'none';
                c.style.display = 'block';
                a.style.borderColor = '#00ad45';
                this._status = 'complete';
                if(window.onNBTSuccess) window.onNBTSuccess(result.token);
            } else {
                this.triggerChallenge(result.type);
            }
        } catch (e) {
            s.style.display = 'none';
            this._status = 'ready';
        }
    },

    triggerChallenge: function(type) {
        console.log('NBT: Challenge Required - ' + type);
    }
};
