from pydub import AudioSegment


def combine_audio(
    output_path: str,
    left_output_path: str,
    right_output_path: str,
    left_audio_path: str = "",
    left_intro_path: str = None,
    right_audio_path: str = "",
    right_intro_path: str = None,
    attend_left: bool = None,
):

    intro_duration = 1.0
    if left_intro_path:
        left_intro: AudioSegment = AudioSegment.from_file(
            left_intro_path, "wav"
        ).split_to_mono()[0]
        intro_duration = left_intro.duration_seconds
    if right_intro_path:
        right_intro: AudioSegment = AudioSegment.from_file(
            right_intro_path, "wav"
        ).split_to_mono()[0]
        intro_duration = right_intro.duration_seconds
    if not left_intro_path:
        left_intro: AudioSegment = AudioSegment.silent(
            duration=intro_duration * 1000, frame_rate=48000
        )
    if not right_intro_path:
        right_intro: AudioSegment = AudioSegment.silent(
            duration=intro_duration * 1000, frame_rate=48000
        )

    left_audio: AudioSegment = AudioSegment.from_file(
        left_audio_path, "wav"
    ).split_to_mono()[0]
    right_audio: AudioSegment = AudioSegment.from_file(
        right_audio_path, "wav"
    ).split_to_mono()[0]

    left_audio: AudioSegment = (
        left_intro + AudioSegment.silent(300, frame_rate=48000) + left_audio
    )
    right_audio: AudioSegment = (
        right_intro + AudioSegment.silent(300, frame_rate=48000) + right_audio
    )
    if attend_left is None:
        length = max(left_audio.frame_count(), right_audio.frame_count())
    elif attend_left:
        length = left_audio.frame_count()
    else:
        length = right_audio.frame_count()

    if left_audio.frame_count() < length:
        data = b"\0\0" * int(length - left_audio.frame_count())
        left_audio = left_audio + AudioSegment(
            data,
            metadata={
                "channels": 1,
                "sample_width": 2,
                "frame_rate": 48000,
                "frame_width": 2,
            },
        )
    if left_audio.frame_count() > length:
        left_audio = left_audio.get_sample_slice(0, int(length))
    if right_audio.frame_count() < length:
        data = b"\0\0" * int(length - right_audio.frame_count())
        right_audio = right_audio + AudioSegment(
            data,
            metadata={
                "channels": 1,
                "sample_width": 2,
                "frame_rate": 48000,
                "frame_width": 2,
            },
        )
    if right_audio.frame_count() > length:
        right_audio = right_audio.get_sample_slice(0, int(length))
    audio = AudioSegment.from_mono_audiosegments(left_audio, right_audio)
    audio.export(output_path, "wav")
    left_audio.export(left_output_path, "wav")
    right_audio.export(right_output_path, "wav")


def combine_audio_single(
    output_path: str,
    audio_path: str = "",
    intro_path: str = None,
):
    if intro_path:
        intro: AudioSegment = AudioSegment.from_file(intro_path, "wav").split_to_mono()[
            0
        ]
    audio: AudioSegment = AudioSegment.from_file(audio_path, "wav").split_to_mono()[0]

    if intro_path:
        audio: AudioSegment = intro + AudioSegment.silent(300, frame_rate=48000) + audio

    audio.export(output_path, "wav")
