import requests
from decouple import config
from gtts import gTTS
from io import BytesIO


ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):
  body = {
    "text": message,
    "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
    }
  }

  # voice_shaun = "mTSvIrm2hmcnOvb21nW2"
  voice_rachel = "21m00Tcm4TlvDq8ikWAM"
  # voice_antoni = "ErXwobaYiN019PkySvjV"

  # Construct request headers and url
  headers = { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
  endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

  try:
    response = requests.post(endpoint, json=body, headers=headers)
  except Exception as e:
     return

  if response.status_code == 200:
      # with open("output.wav", "wb") as f:
      #     f.write(audio_data)
      return response.content
  else:
    return
  

def convert_text_to_speech_google(message: str):
    try:
        tts = gTTS(text=message, lang='en') # Use the English language
        audio_io = BytesIO()
        tts.save(audio_io)
        audio_io.seek(0)  # Go back to the start of the BytesIO object
        return audio_io.read()
    except Exception as e:
        print(f"Exception while converting text to speech using gTTS: {str(e)}")
        return None

