#uvicorn main:app
#uvicorn main:app --reload

# main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# custom function imports
from functions.openai_requests import convert_audio_to_text, get_chat_response, perform_reading
from functions.tarot import draw_cards

#initiate app
app = FastAPI() 

#CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]

#CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )


@app.get("/health")
async def check_health():
    return {"message": "Healthy"}

@app.get("/post-audio-get/")
async def get_audio():
    #get saved audio
    audio_input = open("voice.mp3", "rb")

    #Decode audio
    message_decoded = convert_audio_to_text(audio_input)
    if not message_decoded:
        return HTTPException(status_code=400, details="failed to decode audio")
    # get ChatGPT response 
    chat_response = get_chat_response(message_decoded)

    print(chat_response)
    return "done"

@app.get("/tarot")
async def do_reading():
    drawn_cards = draw_cards()
    print(perform_reading(drawn_cards))
    return "done"


# Post bot response
# Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file:UploadFile = File(...)):
#     print("hello")

