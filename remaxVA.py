import random
import os
from datetime import datetime
import webbrowser


responses = {
    "greeting": ["Hello!", "Hey there!", "Yea bro"],

    "quotes": ["Never give up", "Keep learning every day", "Small progress is still progress", "Consistency beats talent"], 

    "how_are_you": ["I'm doing great", "All Good! What about you?", "Feeling awesome today"],

    "name": ["I'm your Python Chatbot","Just a simple bot ", "You can call me Pybot"],

    "joke": ["Why do programmers love Python? Because it's easy to snake through code",
             "Why did the bug go to school? To improve its debugging skills"],

    "bye": ["Goodbye!", "See you later!", "Bye"],

    "unknown": ["I' don't understand", "Can you rephrase?", "Hmm... not sure"]
}
def speak(text):
    print("🤖 Chatbot:", text)
    
    escaped_text = text.replace("'", "")

    os.system(f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\' {escaped_text}\')"')

def save_chat(message):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")

speak("Hello, I am your Python assistant Author by Remax Meetei! Type bye to exit.")

while True:

    user = input("You: ").lower()
     
    save_chat("You: " + user)
    
    if "hello" in user or "hi" in user:
        reply = random.choice(responses["greeting"])

    elif "motivate me" in user:
        reply = random.choice(responses["quotes"])

    elif "how are you" in user:
         reply = random.choice(responses["how_are_you"])

    elif "add" in user:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        
        result = num1 + num2
        reply = f"The answer is {result}"
        
    elif "subtract" in user:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        
        result = num1 - num2
        reply = f"The answer is {result}"

    elif "multiply" in user:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        
        result = num1 * num2
        reply = f"The answer is {result}"

    elif "divide" in user:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        
        result = num1 / num2
        reply = f"The answer is {result}"

    elif "percentage" in user:
        total = float(input("Enter total marks/number:"))
        obtained = float(input("Enter obtained marks/number: "))

        percent = (obtained / total) * 100

        reply = f"Percentage = {percent}%"

    elif "date" in user:
        current_date = datetime.now().strftime("%m-%d-%Y")
        reply = f"Today's date is {current_date}"

    elif "history" in user:
        with open("chat_history.txt", "r", encoding="utf-8") as file:

            history = file.read()
            
            print(history)

    elif "your name" in user or "name" in user:
         reply = random.choice(responses["name"])

    elif "time" in user:
        reply = "Current time is " + datetime.now().strftime("%H:%M:%S")


    elif "open youtube" in user or "open yt" in user:
        reply = "Opening Youtube for you."
        webbrowser.open("https://www.youtube.com")
        
        
    elif "open google" in user:
        reply = "Opening Google for you."
        webbrowser.open("https://www.google.com")
       
    elif "joke" in user:
         reply = random.choice(responses["joke"])

    elif "bye" in user:
         reply = random.choice(responses["bye"])

         speak(reply)
         save_chat("Bot: " + reply)
         break

    else: 
         reply = random.choice(responses["unknown"])

    if reply:
         speak(reply)
         save_chat("Bot: " + reply)

    reply = ""
    
