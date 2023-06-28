import openai
from decouple import config
from functions.database import get_recent_message

openai.organization=config("OPEN_AI_ORG")
openai.api_key=config("OPEN_AI_KEY")

def convert_audio_to_text(audio_file):
    try:
        transcript=openai.Audio.transcribe("whisper-1",audio_file)
        message=transcript["text"]
        return message
    except Exception as e:
        print(e)
        return
    
#Open-AI
#Get response to our Messages

def get_chat_response(message_in_text):
    messages=get_recent_message()
    user_message={"role":"user","content":message_in_text}
    messages.append(user_message)
    print (messages)
    
    try:
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            
        )
        print(response)
        message_text=response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(e)
        return