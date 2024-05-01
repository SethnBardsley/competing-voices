from fastapi import FastAPI

from experiment import Experiment, Trial
from stream import stream_trial


def create_experiment_app(experiment: Experiment, subject: str, experiment_date: str):
    app = FastAPI(
        allow_origins=["*", "localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    print("Python:Starting Server")

    @app.get("/experiment", response_model=Experiment)
    def get_experiment():
        return experiment

    @app.get("/start-trial/{key}")
    def start_trial(*, key: str):
        return stream_trial(key, subject, experiment, experiment_date)

    return app
