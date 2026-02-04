import vosk
import os
import wave
import json

AUDIO_PATH = '/Users/jacob/Desktop/84-121550-0003.wav'

def process_audio(audio_path, model_path = "vosk-model-small-fr-0.22"):
    model = vosk.Model(os.path.join(os.getcwd(), "models", model_path))
    recognizer = vosk.KaldiRecognizer(model, 16000)
    recognizer.SetWords(True)

    with wave.open(audio_path, 'rb') as wf:
        audio_data = wf.readframes(wf.getnframes())

    recognizer.AcceptWaveform(audio_data)
    result = json.loads(recognizer.Result())

    if 'result' in result:
        full_text = ""
        for item in result["result"]:
            print(item)
            full_text = full_text + item["word"] + " "
        print(full_text)
    else:
        return None

process_audio(AUDIO_PATH, "vosk-model-small-en-us-0.15")