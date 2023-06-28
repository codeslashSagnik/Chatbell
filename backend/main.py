#uvicorn main:app
#uvicorn main:app --reload

from fastapi import FastAPI,File,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
from functions.openai_requests import convert_audio_to_text,get_chat_response
from functions.database import store_messages,reset_messages
from functions.text_speech import convert_text_to_speech
app = FastAPI()

#CORS_ORGIN
origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
    
]

#CORS-Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return{"message":"Conversation Reset"}


@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # Convert audio to text - production
    # Save the file temporarily
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")
    message_in_text=convert_audio_to_text(audio_input)
    if not message_in_text:
        return HTTPException(status_code=400,detail= "Failed to decode the audio")
    
    chat_response=get_chat_response(message_in_text)
    if not chat_response:
        return HTTPException(status_code=400,detail= "Failed to decode the chat_response")
    store_messages(message_in_text,chat_response)
    print(chat_response)
    audio_output=convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400,detail= "Failed to get the audio")
    def interfile():
        yield audio_output
    return StreamingResponse(interfile(),media_type="application/octet-stream")
    return "Done"





