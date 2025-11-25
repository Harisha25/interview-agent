from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_agent(query):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an interview practice partner. Ask questions, follow-up questions, and give feedback."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return response.choices[0].message.content

print("Interview Practice Agent Started. Type 'exit' to quit.")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Agent:", ask_agent(user))

