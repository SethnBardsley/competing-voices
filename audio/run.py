from __future__ import annotations

from pydantic import BaseModel
from typing import Literal
import os

from create_audio import create_audio
from process_audio import process_audio
from combine_audio import combine_audio


attend_m = ".\\processed_audio_files\\attend_M.wav"
attend_f = ".\\processed_audio_files\\attend_F.wav"


class Trial(BaseModel):
    key: str
    attend: Literal["left", "right"]
    left_transcript: str
    left_speaker: Literal["M", "F"]
    right_transcript: str
    right_speaker: Literal["M", "F"]


class Trials(BaseModel):
    trials: list[Trial]


with open(".\\trials.json", "r") as f:
    trials = Trials.model_validate_json(f.read()).trials


def get_processed_audio(transcript: str, speaker: str):
    transcript_path = f".\\transcripts\\{transcript}"
    audio_path = f".\\raw_audio_files\\{transcript}_{speaker}.wav"
    processed_path = f".\\processed_audio_files\\{transcript}_{speaker}.wav"
    if not os.path.isfile(audio_path):
        create_audio(transcript_path, audio_path, speaker)
    if not os.path.isfile(processed_path):
        process_audio(audio_path, processed_path)
    return processed_path


for trial in trials:
    if trial.attend == "left":
        left_intro = attend_m if trial.left_speaker == "M" else attend_f
        right_intro = None
    else:
        left_intro = None
        right_intro = attend_m if trial.right_speaker == "M" else attend_f
    left_audio = get_processed_audio(trial.left_transcript, trial.left_speaker)
    right_audio = get_processed_audio(trial.right_transcript, trial.right_speaker)
    combine_audio(
        f".\\combined_audio_files\\{trial.key}.wav",
        left_audio,
        left_intro,
        right_audio,
        right_intro,
    )
