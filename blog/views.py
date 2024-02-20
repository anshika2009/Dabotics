from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
# Create your views here.

bot = ChatBot('Samuel',read_only=False,logic_adapters=[
    {
        'import_path':'chatterbot.logic.MathematicalEvaluation',        #BestMatch',
        'default_respone':'Sorry, I am unaware of that',
        'maximun_similarity_respone':0.90
        }
    ])

list_to_train = [
    "hi",
    "hi, there",
    "What's your name?",
    "I'm just a chatbot, but you can call me Samuel",
    "What is your fav food?",
    "I like burger",
    "What is your fav sport?",
    "I like basketball",
    "Where do you live",
    "As a software I don't have a physical address"
]

# chatterbotCorpusTrainer=ChatterBotCorpusTrainer(bot)
# chatterbotCorpusTrainer.train('chatterbot.corpus.english')
# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

def index(request):
    return render(request,"blog/index.html")

def specific(request):
    return HttpResponse("specific")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)