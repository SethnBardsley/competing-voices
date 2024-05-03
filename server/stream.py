from pylsl import StreamInfo, StreamOutlet, local_clock, IRREGULAR_RATE, cf_float32
from psychopy import prefs, sound, core, event
import psychtoolbox
from time import sleep

prefs.hardware["audioLib"] = "PTB"
prefs.hardware["audioLatencyMode"] = 4

from experiment import Experiment


def begin_stream(subject: int, experiment: Experiment, experiment_date: str):

    events = StreamInfo(
        name=f"EventStream_{experiment.name}_S{subject}_{experiment_date}",
        type="Markers",
        channel_count=1,
        nominal_srate=IRREGULAR_RATE,
        channel_format="string",
        source_id=f"cv-event-{experiment.name}-S{subject}-{experiment_date}",
    )
    events_outlet = StreamOutlet(events)

    audio = StreamInfo(
        name=f"AudioStream_{experiment.name}_S{subject}_{experiment_date}",
        type="Audio",
        channel_count=1,
        nominal_srate=48000,
        channel_format=cf_float32,
        source_id=f"cv-audio-{experiment.name}-S{subject}-{experiment_date}",
    )
    audio_outlet = StreamOutlet(audio)

    attended_audio = StreamInfo(
        name=f"AttendedStream_{experiment.name}_S{subject}_{experiment_date}",
        type="Audio",
        channel_count=1,
        nominal_srate=48000,
        channel_format=cf_float32,
        source_id=f"cv-attended-{experiment.name}-S{subject}-{experiment_date}",
    )
    attended_audio_outlet = StreamOutlet(attended_audio)

    competing_audio = StreamInfo(
        name=f"CompetingStream_{experiment.name}_S{subject}_{experiment_date}",
        type="Audio",
        channel_count=1,
        nominal_srate=48000,
        channel_format=cf_float32,
        source_id=f"cv-competing-{experiment.name}-S{subject}-{experiment_date}",
    )
    competing_audio_outlet = StreamOutlet(competing_audio)

    def stream_trial(trial_key: str):
        trial = [trial for trial in experiment.trials if trial.key == trial_key][0]

        audio_file = trial.play_audio_file
        audio_sound = sound.Sound(f"./audio/{audio_file}")

        start_sample_time = psychtoolbox.GetSecs() + 0.5
        audio_sound.play(when=start_sample_time)

        events_outlet.push_sample(["Start"], start_sample_time)

        sleep(20)

        audio_sound.stop()

        events_outlet.push_sample(["End"], psychtoolbox.GetSecs())

        return True

    return stream_trial
