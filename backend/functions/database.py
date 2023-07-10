import json
import random

# Get Recent Messages
def get_recent_messages():

    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing me for a job as a cat sitter. Ask short questions that are relevant to the junior position. Your name is Rachel. The user is called Jake. Keep your answers to under 30 words."
    }

    # intialise messages
    messages =[]

    # add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humour and cat puns."
    else:    
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include a very challenging question."
 
    messages.append(learn_instruction)

    # get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append the last 5 items of data
            if data:
                if len(data) <5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)        
    except Exception as e:
        print(e)
        pass

    return messages

# get last messages
def store_messages():
    pass