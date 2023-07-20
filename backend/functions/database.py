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

#reset messages
def reset_messages():

    #Overwrite current file with nothing
    open("stored_data.json", "w")

# get last messages
def store_messages(request_message, response_message):
    # define the file name
    file_name = "stored_data.json"

    # ignore the first one becasue it is added anyway by get_recent_messages
    messages = get_recent_messages()[1:]
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}  
    messages.append(user_message)
    messages.append(assistant_message)

    #save the updated file 3.28
    with open(file_name, "w") as f:
        json.dump(messages, f)

