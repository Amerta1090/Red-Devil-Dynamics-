# Red Devil Dynamics

Red Devil Dynamics is a small AI experiment built by a Manchester United fan to estimate the probability that Manchester United will score within the next 10 minutes of a match.

The idea comes from a familiar moment for every United supporter: the pressure builds, shots accumulate, the expected goals number rises, and everyone senses that a goal might be coming. This project attempts to quantify that moment using a simple machine learning model.

Live demo:  
https://red-devil-dynamics.abdulmajidr708.workers.dev/

---

## Project Overview

The system predicts the probability that Manchester United will score in the next 10 minutes based on a small set of match features.

Inputs used by the model:

- **current_minute** – current match time  
- **cumulative_shots** – total shots taken by Manchester United  
- **cumulative_xG** – accumulated expected goals  
- **side** – match location (home or away)

These variables provide a rough signal of attacking momentum during a match.

---

## How It Works

User inputs match statistics through the web interface.  
The frontend sends a request to the prediction API, which runs a trained model and returns a probability score.

Pipeline:

User Input → Frontend → API Request → Machine Learning Model → Probability Output

The output represents:

```

Probability that Manchester United scores within the next 10 minutes

```

---

## Survival Analysis Concept

The prediction logic is inspired by **survival analysis**, a statistical framework used to model the **time until an event occurs**.

In medicine, survival analysis is often used to estimate the time until a patient experiences an event (for example recovery or death).  
In this project, the same concept is applied to football:

```

Event = Manchester United scoring a goal
Time = match minute

```

One key function in survival analysis is the **Survival Function**.

### Survival Function

The survival function describes the probability that the event **has not yet happened by time t**.

```

S(t) = P(T > t)

```

Where:

- **T** = time when the event happens  
- **t** = current time

In this context:

```

S(t) = probability that Manchester United has NOT scored yet at minute t

```

From the survival function we can derive the probability that the goal will occur in a future time window.

This project estimates the **goal intensity** using a **Poisson regression model**, then converts that intensity into a probability using the exponential survival formulation:

```

P(goal in next Δt minutes) = 1 − exp(−λΔt)

```

Where:

- **λ** = predicted goal rate (from the model)
- **Δt** = prediction window (10 minutes)

This equation is closely related to the survival function of a **Poisson process**, which assumes events occur randomly but with a measurable rate.

---

## Example API Request

Endpoint:

```

POST /predict

````

Example request:

```json
{
  "current_minute": 75,
  "cumulative_shots": 12,
  "cumulative_xG": 1.45,
  "side": 1
}
````

Example response:

```json
{
  "probability_goal_next_10_min": 0.27
}
```

This indicates a **27% probability** that Manchester United scores within the next ten minutes.

---

## Tech Stack

Frontend

* HTML
* TailwindCSS
* JavaScript

Backend

* Python
* FastAPI
* Uvicorn

Deployment

* Frontend: Cloudflare Workers
* Model API: HuggingFace Spaces

---

## Limitations

This model is intentionally simple. It does not include many variables that influence real football matches such as:

* player lineups
* possession statistics
* passing networks
* defensive pressure
* tactical systems

Football is a complex system, and this project captures only a small portion of it.

---

## Disclaimer

This project is not affiliated with Manchester United Football Club.
It is a fan-made analytics experiment created for learning and exploration in sports analytics and machine learning.
