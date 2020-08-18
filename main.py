from chatterbot import ChatBot
import logging
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

logging.basicConfig(level=logging.INFO)
my_bot= ChatBot(name='Boris', read_only=False,
logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                'chatterbot.logic.BestMatch'])

trainer = UbuntuCorpusTrainer(my_bot)
trainer.train()
while True:
    a=str(input("Denis:"))
    response=my_bot.get_response(a)
    print("Boris:",response)
                    
"""small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)
"""