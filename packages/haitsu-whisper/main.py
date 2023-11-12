import json
from openai import OpenAI
client = OpenAI()

audio_file= open("audios/haitsu.MP3", "rb")
# audio_file= open("audios/haitsu_short.MP3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcript)

with open("transcript.txt", "w") as text_file:
    text_file.write(transcript.text)