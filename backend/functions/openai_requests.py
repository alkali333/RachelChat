import openai
from decouple import config

from functions.database import get_recent_messages

#retrieve env variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

#Open AI - Whisper
#Convert Audio To Text

def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)

# Chat GPT
# Get Response To Our Message
def get_chat_response(message_input):
    messages = get_recent_messages()
    user_message = {"role":  "user",
                    "content": message_input}
        
    # Add the new message
    messages.append(user_message)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        message_text = response["choices"][0]["message"]["content"]   
        return message_text
    except Exception as e:
        print(e)
        return
    
def perform_reading(drawn_cards):
    
    prompt = f"You are a fictional tarot card reader, give a reading based on the following cards {drawn_cards}. Explain the significance of each one and what they all mean together. Use spiritual language and refer to the user in an affectionate way, like 'Oh Noble Seeker' or similar."
    
    # This needs to be an array of dictionaries, even though we are just sending a single message
    learn_instruction = [{
        "role": "user",
        "content": prompt
    }]

    # print("Prompt Sent: " + prompt)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=learn_instruction
        )
        message_text = response["choices"][0]["message"]["content"]   
        return message_text
    except Exception as e:
        print(e)
    return
