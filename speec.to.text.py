
---

## Exemplo simplificado do script `speech_to_text.py`

```python
import sys
import os
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig
from dotenv import load_dotenv

load_dotenv()

def transcrever_audio(caminho_audio):
    speech_key = os.getenv("AZURE_SPEECH_KEY")
    service_region = os.getenv("AZURE_SPEECH_REGION")

    speech_config = SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = AudioConfig(filename=caminho_audio)
    recognizer = SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = recognizer.recognize_once()
    if result.reason == result.Reason.RecognizedSpeech:
        print(f"Transcrição: {result.text}")
        return result.text
    else:
        print("Falha na transcrição.")
        return ""

if __name__ == "__main__":
    arquivo_audio = sys.argv[1]
    texto = transcrever_audio(arquivo_audio)
    with open("resultados/transcricao.txt", "w", encoding="utf-8") as f:
        f.write(texto)
