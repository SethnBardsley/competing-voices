from __future__ import annotations

from pydantic import BaseModel

from enum import Enum


class Answer(BaseModel):
    key: str
    text: str


class Question(BaseModel):
    key: str
    question: str
    prompt: str
    answers: list[Answer]
    correct_answer: Answer


class AudioFile(BaseModel):
    filename: str


class AudioPosition(str, Enum):
    LEFT = "left"
    RIGHT = "right"


class Trial(BaseModel):
    key: str
    question: Question
    play_audio_file: AudioFile
    attend_audio_file: AudioFile
    competing_audio_file: AudioFile
    competing_position: AudioPosition
    instructions: str


class Experiment(BaseModel):
    key: str
    name: str
    trials: list[Trial]


def load_experiment(experiment_name: str) -> Experiment:
    return Experiment(key="5", name="Ex", trials=[])
