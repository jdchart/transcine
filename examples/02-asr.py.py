from transcine import process_audio

AUDIO_PATH = '/Users/jacob/Downloads/LibriSpeech/dev-clean/84/121123/84-121123-0000.wav'

result_vosk = process_audio(AUDIO_PATH, "vosk", "vosk-model-small-fr-0.22")
result_whisper = process_audio(AUDIO_PATH, "whisper")

print(result_vosk)
print(result_whisper)