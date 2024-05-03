from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from experiment import Experiment, Trial
from stream import begin_stream


# Create a basic HTTP webserver with two routes to run the experiment with
def create_experiment_app(experiment: Experiment, subject: str, experiment_date: str):
    # Create router
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*", "localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Setup labstream layer
    stream_trial = begin_stream(subject, experiment, experiment_date)

    print("Python:Starting Server")

    # Route to return experiment details to the client
    @app.get("/experiment", response_model=Experiment)
    def get_experiment():
        return experiment

    # Route to start the trial, returns True when trial is finished
    @app.get("/start-trial/{key}")
    def start_trial(*, key: str):
        return stream_trial(key)

    # Route to start the trial, returns True when trial is finished
    @app.get("/answer-question/{trial_key}/{answer_key}")
    def answer_question(*, trial_key: str, answer_key: str):
        with open(
            f"./logs/{experiment_date}_Subject_{subject}_Experiment_{experiment.name}.txt",
            "a",
        ) as f:
            f.write(f"Answer to trial {trial_key}:{answer_key}\n")

    # Return app to be run via uvicorn
    return app
