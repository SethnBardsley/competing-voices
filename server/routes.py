from fastapi import FastAPI

from experiment import Experiment, Trial


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

    @app.get("/start-trial/{key}", response_class=bool)
    def start_trial(*, key: str):
        pass

    @app.get("/trial-status", response_class=bool)
    def trial_status(*, key: str):
        return False

    return app
