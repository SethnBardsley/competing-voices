from __future__ import annotations

from pydantic import BaseModel

from enum import Enum


class Answer(BaseModel):
    key: str
    text: str


class Question(BaseModel):
    question: str
    prompt: str
    answers: list[Answer]
    correct_answer: Answer


class AudioPosition(str, Enum):
    LEFT = "left"
    RIGHT = "right"


class Trial(BaseModel):
    key: str
    question: Question
    play_audio_file: str
    attend_audio_file: str
    competing_audio_file: str
    attend_position: str
    instructions: str


class Experiment(BaseModel):
    name: str
    trials: list[Trial]


def load_experiment(experiment_name: str) -> Experiment:
    filename = f"./experiments/{experiment_name}.json"

    with open(filename, "r") as f:
        experiment = Experiment.model_validate_json(f.read())

    return experiment
