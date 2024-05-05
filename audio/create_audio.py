from pyt2s.services import stream_elements
from pydub import AudioSegment
from typing import Literal
import os

# USING StreamElements for TTS

valid_speakers = {
    "M": "en-AU-Wavenet-B",
    "F": "en-AU-Wavenet-C",
}


def create_audio(transcript_path: str, output_path: str, speaker: Literal["M", "F"]):
    speaker = valid_speakers[speaker]
    with open(transcript_path, "r") as file:
        transcript = file.read()
    obj = stream_elements.StreamElements()
    data = obj.requestTTS(transcript, speaker)
    temp_file = ".\\temp.mp3"
    with open(temp_file, "+wb") as file:
        file.write(data)
    audio: AudioSegment = AudioSegment.from_file(temp_file, "mp3")
    audio.export(output_path, "wav")
    os.remove(temp_file)


if __name__ == "__main__":
    import sys

    print(sys.argv)
    if len(sys.argv) != 4:
        raise Exception(
            "create_audio.py requires 3 positional arguments, transcript_file, output_file, speaker_number"
        )
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    speaker = sys.argv[3]
    create_audio(input_file, output_file, speaker)
