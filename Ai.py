import openai

#in bellow you must put your Api key 
#website link:"https://platform.openai.com/api-keys"
openai.api_key = ""

def chat_gpt(promt):
    response = openai.chatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":promt}]
    )

    return response.choices[0].message.content.strip()

if __name__=="__main":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_gpt(user_input)
        print("chatbot", response)

    