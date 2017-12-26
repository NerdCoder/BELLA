from chatterbot import ChatBot

bot = ChatBot(
    'Bella',
    trainer = 'chatterbot.trainers.ListTrainer',
    #trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer',
    

)

#bot.train("chatterbot.corpus.english.conversations")

bot.train([
    "Hi",
    "Hello",
    "Who are you?",
    "I'm Bella"
])


while True:
	
    try:
    	q = input()
    	bot_ans = bot.get_response(q)
    	print(bot_ans)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
