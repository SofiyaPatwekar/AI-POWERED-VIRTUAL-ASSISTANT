from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
key=os.getenv("key")
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",  
    api_key=key,                    
)
messages=[]
    
def chat(message):
    global messages
    messages.append(
        {
            "role":"user",
            "content": message
        }
    )
    response = client.chat.completions.create(
    model="openai/gpt-oss-120b",           
    messages=messages 
    )

    assistant_message={
            "role":"assistant",
            "content": response.choices[0].message.content
        }
    messages.append(assistant_message)
    print(f"Assistant: {assistant_message['content']}")

    
if __name__=="__main__":
    print("Hello I'm your Assistant, How may I help you? (Enter 'quit' to end the conversation)")
    while True:
        user_question=input("user: ")
        if user_question=="quit":
            break
        else:
            chat(user_question)

