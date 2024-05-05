from pydub import AudioSegment


def combine_audio(
    output_path: str,
    left_audio_path: str = "",
    left_intro_path: str = None,
    right_audio_path: str = "",
    right_intro_path: str = None,
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
    length = max(left_audio.duration_seconds, right_audio.duration_seconds)
    left_audio = left_audio + AudioSegment.silent(
        duration=(length - left_audio.duration_seconds) * 1000, frame_rate=48000
    )
    right_audio = right_audio + AudioSegment.silent(
        duration=(length - right_audio.duration_seconds) * 1000, frame_rate=48000
    )

    print(left_audio.duration_seconds)
    print(right_audio.duration_seconds)
    audio = AudioSegment.from_mono_audiosegments(left_audio, right_audio)
    audio.export(output_path, "wav")
