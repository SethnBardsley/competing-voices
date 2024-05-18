# Experiment.py, file for defining experiment datastructure and loading in from json files in the ./experiments/ directory.
from __future__ import annotations

from pydantic import BaseModel


# Define Validated Datastructures using pydantic
class Answer(BaseModel):
    key: str
    text: str


class Question(BaseModel):
    question: str
    prompt: str
    answers: list[Answer]
    correct_answer: Answer


class Trial(BaseModel):
    key: str
    question: Question
    attend_position: str
    instructions: str
    single_speaker: bool


class Experiment(BaseModel):
    name: str
    trials: list[Trial]


# Load in experiment using experiment name.
def load_experiment(experiment_name: str) -> Experiment:
    # Get filepath
    filename = f"./experiments/{experiment_name}.json"

    # Open file and read contents into pydantic object
    with open(filename, "r") as f:
        experiment = Experiment.model_validate_json(f.read())

    # Return pydantic object defined by file contents
    return experiment
