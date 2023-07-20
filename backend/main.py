#uvicorn main:app
#uvicorn main:app --reload

# main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# custom function imports
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response, perform_reading
from functions.text_to_speech import convert_text_to_speech
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

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation reset"}    

@app.post("/post-audio/")
async def post_audio(file:UploadFile = File(...)):
    # Convert audio to text - production
    # Save the file temporarily
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure output
    if not message_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode audio")
    # get ChatGPT response 
    chat_response = get_chat_response(message_decoded)
    if not chat_response:
        raise HTTPException(status_code=400, details="failed to get chat response")

    store_messages(message_decoded, chat_response)

    #convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400, details="failed to get Eleven Labs audio response")
    
    # create a generator that yields chunks of data
    def iterfile():
        yield audio_output
    
    # return audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")

    #print(chat_response)
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

