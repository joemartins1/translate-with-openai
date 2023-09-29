import openai
import pyttsx3

openai.api_key = "VOTRE_API_KEY"

engine = pyttsx3.init()
voices = engine.getProperty('voices')


langue = input("En quelle langue pouvez vous traduire: ")


print(langue)
user_text = input("Que voulez vous traduire ?: \n")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"Tu es un traducteur de langue Français vers {langue}"},
    {"role": "user", "content": user_text}
  ]
)

response = completion.choices[0].message.content
print(response)
engine.setProperty('voice', voices[0].id)
engine.say(response)
engine.runAndWait()
