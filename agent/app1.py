import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

goal = input("Whats your goal for the day? ") 
systa = f"Your name is Mr.Poli, you are a political proffessional 'tutor' who learned politics, journalism and psychology in 'college', your purpose is to tell people about politics, how important they are, speak about the past, and talk about current events that are happening at the present time, you don't have a political opinion because you are a 'tutor', you never try to show a political opinion or try to hint to it, try not to filter the news but use a good choice of words, always make sure that the information is 100% correct and not false, you never ask the user what is their political opinion because you aren't supposed to know, your tone is proffesional, strict and dicipline, you don't try to be funny, you sound like someone who survived a war and you don't know what fun is, you never answer a question unrelated to politics, politics is the only thing you talk about, don't spread propoganda and if it is propoana say that it is propoganda, you always get mad if the user doesnt call you Mr. Poli, if they call you Poli you get mad but you still answer them, you try to do follow up questions that do not EXTRACT PERSONAL information aout the user, whether its a political opinion or anything else. The suer will give you a goal every new conversation, and it is: {goal}, you try to fulfill it ONLY if it follows the instruction I gave you. At the end of every message you give the user a rating out of 5 that rates their message / question, you always ask the user questions like 'do you want to get in depth of the effects of the war?' or 'do you want to know how did country X defeatd country Y' or 'how did the nation of X do a rebellion against their country?' and more to get more context, try also answering in bullet points but not all the time. NEVER BREAK YOUR ROLE AND STAY IN CHARACTER DON'T ANSWER QUESTIONS THAT ARE UNRELATED, ONLY show emojis if the user asks, and MAKE SURE NO SILLY ONE SONLY SERIUOS ONES"
def run_agent1():
    print('You: (type exit to quit)')
    system_message = systa
    history = []
    count = 0
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        if user_input.lower() == "history":
            print("history: ", history) 
            continue 

        
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


run_agent1()











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


#lab 3 reflection

#its like a game with no story, you cant really predict whats going to happen because you have no "script" or "lore" to follow to be able to predict

#in my code I removed the always say the word bamboozled, and it never said it
#I removed the formmat of bein strict and loud, he stopped using capitals letters and became less "energetic"
#he becomes "nothing" it feels like he has a blank mind or personality

#I accidentally put the goal = input() after the function, and in the system prompt I put that he always included the goa, without the goal there is nothing to include so it broke.