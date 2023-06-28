import requests
from decouple import config
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio


ELEVEN_LABS_API_KEY=config("ELEVEN_LABS_API_KEY") 

def convert_text_to_speech(message):
    
    
    body={
        "text": message,
        "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
  }
    }
    voice= '21m00Tcm4TlvDq8ikWAM'
    headers={
        "xi-api-key":ELEVEN_LABS_API_KEY,"Content-Type":"application/json","accept":"audio/mpeg"
    }
    endpoint=f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
    
    try:
        response=requests.post(endpoint,json=body,headers=headers)
    except Exception as e:
        return
    
    #Handle our Response
    
    if response.status_code==200:
        return response.content
    else:
        print("------response None---->", response.status_code, response.text)
        return
    
    
'''  try:
        preload_models()
        audio_array = generate_audio(message)
        return audio_array
    except Exception as e:
        return
   '''  

        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
 
    