import json
import random

#get recent message

def get_recent_message():
    file_name="stored_data.json"
    learn_instruction={
        "role":"system",
        "content":"You are a seasoned interviewer with expertise in HR and technical rounds,Your name is Chatbell You have extensive knowledge in computer science and engineering with 10 years of experience. You can conduct an effective interview for a junior position, tailored to the user's field of interest.You will not ask more than one question at a time. You will ask concise and impactful questions to the user.Keep the questions short and crisp.You usually ask for short introduction before conducting the interview"
    }
    messages=[]
    
    #Add a random element
    
    x=random.uniform(0,1)
    if  x<0.5:
        learn_instruction["content"]=learn_instruction["content"]+" Your Response will include some dry humor"
    if x>0.8:
        learn_instruction["content"]=learn_instruction["content"]+" Rather ask challenging questions."
    
    #Appending message to Intruction
    messages.append(learn_instruction)
    
    try:
        with open(file_name)as user_file:
            data=json.load(user_file)
            if data:
                if len(data)<5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass
    #Return 
    return messages

def store_messages(request_message,response_message):
    file_name="stored_data.json"
    messaged=get_recent_message()[1:]
    user_messages={"role":"user","content":request_message}
    assistant_messages={"role":"assistant","content":response_message}
    messaged.append(user_messages)
    messaged.append(assistant_messages)
    
    
    #save the uploaded file
    with open(file_name,"w")as f:
        json.dump(messaged,f)

def reset_messages():
    open("stored_data.json","w")