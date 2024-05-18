from pydub.silence import split_on_silence
from pydub import AudioSegment, effects
from scipy.io import wavfile
import numpy


def remove_silence(input_path: str, output_path: str) -> None:
    # Method adapted from
    # https://onkar-patil.medium.com/how-to-remove-silence-from-an-audio-using-python-50fd2c00557d
    audio: AudioSegment = AudioSegment.from_file(input_path, "wav")

    audio_chunks = split_on_silence(
        audio, min_silence_len=300, silence_thresh=-18.0, keep_silence=0
    )
    all_audio_chunks = []
    for i, audio_chunk in enumerate(audio_chunks):
        audio_chunk.set_frame_rate(48000)
        if i != 0:
            all_audio_chunks.append(AudioSegment.silent(duration=100, frame_rate=48000))
        all_audio_chunks.append(audio_chunk)
    print(audio_chunks)
    audio: AudioSegment = sum(all_audio_chunks)
    audio.export(output_path, "wav")


def normalize_sound(input_path: str, output_path: str, rms_level: float = 10.0) -> None:
    # rms_level is in db
    rate, data = wavfile.read(input_path)
    # Method adapted from
    # https://superkogito.github.io/blog/2020/04/30/rms_normalization.html
    # linear rms level and scaling factor
    r = 10 ** (rms_level / 10.0)

    timestep = 2.5
    start_index = 0
    for i in range(0, int(len(data) / rate / timestep) + 1):
        end_index = int(min(start_index + (rate * timestep), len(data)))
        print(f"Normalising {start_index} - {end_index}")
        factor = numpy.sqrt(
            (len(data[start_index:end_index]) * r**2)
            / numpy.sum(data[start_index:end_index] ** 2)
        )
        data[start_index:end_index] = factor * data[start_index:end_index]
        start_index = end_index

    wavfile.write(output_path, rate=int(rate), data=data.astype(numpy.int16))


def process_audio(input_path: str, output_path: str, speaker_db: float):
    remove_silence(input_path, output_path)
    normalize_sound(input_path, output_path, speaker_db)


if __name__ == "__main__":
    import sys

    print(sys.argv)
    if len(sys.argv) != 3:
        raise Exception(
            "process_audio.py requires 2 positional arguments, input_file and output_file"
        )
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_audio(input_file, output_file)
