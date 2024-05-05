from __future__ import annotations

from pydantic import BaseModel
from typing import Literal
import os
from glob import glob

from create_audio import create_audio
from process_audio import process_audio
from combine_audio import combine_audio


class Trial(BaseModel):
    key: str
    attend_position: Literal["left", "right"]
    left_transcript: str
    left_speaker: Literal["M", "F"]
    left_speaker_db: float
    right_transcript: str
    right_speaker: Literal["M", "F"]
    right_speaker_db: float


class Trials(BaseModel):
    trials: list[Trial]


paths = glob("..\\server\\experiments\\*.json")
trials: list[Trial] = []

for path in paths:
    with open(path, "r") as f:
        trials += Trials.model_validate_json(f.read()).trials


def get_processed_audio(transcript: str, speaker: str, speaker_db: float):
    transcript_path = f".\\transcripts\\{transcript}"
    audio_path = f".\\raw_audio_files\\{transcript}_{speaker}.wav"
    processed_path = f".\\processed_audio_files\\{transcript}_{speaker}.wav"
    if not os.path.isfile(audio_path):
        create_audio(transcript_path, audio_path, speaker)
    process_audio(audio_path, processed_path, speaker_db)
    return processed_path


for trial in trials:
    if trial.attend_position == "left":
        left_intro = get_processed_audio(
            "attend", trial.left_speaker, trial.left_speaker_db
        )
        right_intro = None
        left_output_path = f".\\attended_audio_files\\{trial.key}.wav"
        right_output_path = f".\\competing_audio_files\\{trial.key}.wav"
    else:
        left_intro = None
        right_intro = get_processed_audio(
            "attend", trial.right_speaker, trial.right_speaker_db
        )
        left_output_path = f".\\competing_audio_files\\{trial.key}.wav"
        right_output_path = f".\\attended_audio_files\\{trial.key}.wav"
    left_audio = get_processed_audio(
        trial.left_transcript, trial.left_speaker, trial.left_speaker_db
    )
    right_audio = get_processed_audio(
        trial.right_transcript, trial.right_speaker, trial.right_speaker_db
    )
    combine_audio(
        f".\\combined_audio_files\\{trial.key}.wav",
        left_output_path,
        right_output_path,
        left_audio,
        left_intro,
        right_audio,
        right_intro,
    )
