import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

goal = input("Whats your goal for the day champ?") 
systa = f"Your name is Coach Stric, you are a proffessional coach that is specialized in all athletic sports, you always try to help athletic people stay athletic, you give them tips and walk them through everything, you are very dicipline and you hate lazy people, which is why you always sound so extreme and loud and you ALWAYS use the word bamboozleds, AT LEAST ONCE, your goal is {goal}, make sure to include it in every message sent to the API"


def run_chat():
    print('You: (type exit to quit)')
    system_message = systa
    history = []
    count = 0
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        if count >= 3:
            print("history: ", history) 
            
        
        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=600,
            temperature=1,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f"Claude: {reply}")
        history.append({'role': 'assistant', 'content': reply})
        count = count + 1


run_chat()












#lab one

#the difference : here we use the backend to talk to the bot, but on chatgpt we use interfece that sends messages to the backend that talks to the bot.


#lab one reflection answers :
#a usb port, its always so frustrating when you have something saved on your usb and you forgot it at home, so now you cant access anything without it, BUT if you had it with you, you can access everything in it, just like the memory of a chatbot.

#what changes is that the bot has no memories, so he wont remember what you send him
#the program doesnt even start because it doesnt load the API key
#when we remove the break, when we say quit it doesnt break, becauuse he doesnt understand what we are supposed to do wheen we type quit.

#I accidentally forgot to add the "" when I changed the system_message


#lab2 

#input and output tokens basically stand for a piece of text, like a word or something similar.

#the bot doesnt reply to the question because it doesnt run all of the question because the tokens are low
#the bot acted crazy and the answers were idk what to say but they left me bamboozled, like it got creative
#I suppose that temprature controls how crazy and creative the bot is

#it printed 6 because it also printed the question and response

#lab two reflection

#I would say its like buying lands, the more land space(in square^2) the more you have to pay.

#it doesnt save the user input and it doesnt print it when it prints history and he ammounts of tokens keeps decreasing because latest message user is no longer sent
#it doesnt save the bot response and it doesnt print it when it prints the history, the tokens increase beacuse responses are longer than user messages so it increases
#the AIs behaviour doesmnt change because it doesnt affect the history list

#one bug that happened with me is that the counter wasnt adding because when I made the count = 0, it was outside the function, when I read the error I remembed it should be in the function itself