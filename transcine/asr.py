# https://github.com/openai/whisper
# pip install openai-whisper

import vosk
import os
import wave
import json
import whisper

def process_audio(audio_path, method = "whisper", model = "turbo"):
    if method == "whisper":
        return process_audio_whisper(audio_path, model)
    elif method == "vosk":
        return process_audio_vosk(audio_path, model)
    else:
        return process_audio_whisper(audio_path)

def process_audio_vosk(audio_path, model_path = "vosk-model-small-fr-0.22"):
    model_path = os.path.join(os.getcwd(), "models", model_path)
    if os.path.isdir(model_path) == True:
        try:
            model = vosk.Model(os.path.join(os.getcwd(), "models", model_path))
            recognizer = vosk.KaldiRecognizer(model, 16000)
            recognizer.SetWords(True)

            with wave.open(audio_path, 'rb') as wf:
                audio_data = wf.readframes(wf.getnframes())

            recognizer.AcceptWaveform(audio_data)
            result = json.loads(recognizer.Result())

            if 'result' in result:
                full_text = ""
                words = []
                for item in result["result"]:
                    full_text = full_text + item["word"] + " "
                    words.append(item)
                return {
                    "full_text" : full_text[:-1],
                    "words" : words   
                }
            else:
                return None
        except:
            return None
    else:
        return None
    
def process_audio_whisper(audio_path, model_path = "turbo"):
    
    try:
        model = whisper.load_model(model_path)

        result = model.transcribe(
            audio_path,
            word_timestamps = True
        )

        words = []
        for segment in result["segments"]:
            for word in segment["words"]:
                words.append({
                    "word" : word['word'],
                    "start" : float(word['start']),
                    "end" : float(word['end']),
                    "conf" : float(word['probability'])
                })

        return {
            "full_text" : result["text"],
            "words" : words
        }
    
    except:
        return None