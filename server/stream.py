from pylsl import (
    StreamInfo,
    StreamOutlet,
    local_clock,
    IRREGULAR_RATE,
    cf_float32,
    cf_int16,
)
from psychopy import prefs, sound, core, event
import psychtoolbox
from scipy.io import wavfile
from time import sleep

prefs.hardware["audioLib"] = "pyo"
prefs.hardware["audioLatencyMode"] = 3

from experiment import Experiment


def begin_stream(subject: int, experiment: Experiment, experiment_date: str):

    events = StreamInfo(
        name=f"EventStream",
        type="Markers",
        channel_count=1,
        nominal_srate=IRREGULAR_RATE,
        channel_format="string",
        source_id=f"cv-event",
    )
    events_outlet = StreamOutlet(events)

    audio = StreamInfo(
        name=f"AudioStream",
        type="Audio",
        channel_count=2,
        nominal_srate=48000,
        channel_format=cf_int16,
        source_id=f"cv-audio",
    )
    audio_outlet = StreamOutlet(audio, max_buffered=600)

    attended_audio = StreamInfo(
        name=f"AttendedStream",
        type="Audio",
        channel_count=1,
        nominal_srate=48000,
        channel_format=cf_int16,
        source_id=f"cv-attended",
    )
    attended_audio_outlet = StreamOutlet(attended_audio, max_buffered=600)

    competing_audio = StreamInfo(
        name=f"CompetingStream",
        type="Audio",
        channel_count=1,
        nominal_srate=48000,
        channel_format=cf_int16,
        source_id=f"cv-competing",
    )
    competing_audio_outlet = StreamOutlet(competing_audio, max_buffered=600)

    # TODO - fix stuttering stream

    def stream_trial(trial_key: str):
        trial = [trial for trial in experiment.trials if trial.key == trial_key][0]

        play_audio_file = f"../audio/combined_audio_files/{trial_key}.wav"
        competing_audio_file = f"../audio/competing_audio_files/{trial_key}.wav"
        attended_audio_file = f"../audio/attended_audio_files/{trial_key}.wav"

        audio_sound = sound.Sound(play_audio_file)

        start_sample_time = psychtoolbox.GetSecs() + 1.0

        events_outlet.push_sample(["Start"], start_sample_time)

        audio_sound.play(when=start_sample_time)

        while audio_sound.isPlaying:
            pass

        audio_sound.stop()

        events_outlet.push_sample(["End"], psychtoolbox.GetSecs())

        sr, play_data = wavfile.read(play_audio_file)
        if sr != 48000:
            raise Exception("Invalid Sample Rate")
        sr, competing_data = wavfile.read(competing_audio_file)
        if sr != 48000:
            raise Exception("Invalid Sample Rate")
        sr, attended_data = wavfile.read(attended_audio_file)
        if sr != 48000:
            raise Exception("Invalid Sample Rate")
        audio_outlet.push_chunk(play_data.tolist(), start_sample_time)
        competing_audio_outlet.push_chunk(competing_data, start_sample_time)
        attended_audio_outlet.push_chunk(attended_data, start_sample_time)

        return True

    return stream_trial
