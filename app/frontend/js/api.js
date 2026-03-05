const API_BASE = "http://127.0.0.1:8000";

async function predictGoal(minute, shots, xg, side){

const url = `${API_BASE}/predict?current_minute=${minute}&cumulative_shots=${shots}&cumulative_xG=${xg}&side=${side}`;

const response = await fetch(url);

return await response.json();

}
