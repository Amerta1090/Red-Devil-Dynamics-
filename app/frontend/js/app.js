function setSide(val, el) {

    document.getElementById('side').value = val;

    document.querySelectorAll('.btn-side').forEach(btn => {
        btn.classList.remove('active');
    });

    el.classList.add('active');

}


async function calculateGoal() {

    const btn = document.querySelector('.glitch-btn');
    const loader = document.getElementById('loader');
    const resultUi = document.getElementById('result-ui');
    const probText = document.getElementById('prob-value');

    const minute = Number(document.getElementById('minute').value);
    const shots = Number(document.getElementById('shots').value);
    const xg = Number(document.getElementById('xg').value);
    const side = Number(document.getElementById('side').value);

    if ([minute, shots, xg, side].some(Number.isNaN)) {
        alert("Invalid input values.");
        return;
    }

    btn.innerText = "CALCULATING...";
    resultUi.classList.add('opacity-20');
    loader.classList.remove('hidden');

    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 5000);

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            signal: controller.signal,
            body: JSON.stringify({
                current_minute: minute,
                cumulative_shots: shots,
                cumulative_xG: xg,
                side: side
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        const prob = (data.probability_goal_next_10_min * 100).toFixed(1);

        if (probText) {
            probText.innerHTML = `${prob}<span class="text-4xl">%</span>`;
        }

        if (typeof updateBars === "function") {
            updateBars(prob);
        }

    } catch (err) {

        console.error("Request error:", err);

        if (err.name === "AbortError") {
            alert("Request timeout. API took too long.");
        } else {
            alert("API request failed.");
        }

    } finally {

        clearTimeout(timeout);

        loader.classList.add('hidden');
        resultUi.classList.remove('opacity-20');

        btn.innerText = "INITIATE ATTACK";
    }
}
