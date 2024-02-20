from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create your views here.

bot = ChatBot('Samuel',read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])

list_to_train = [
    "hi",
    "hi, there",
    "What's your name?",
    "I'm just a chatbot",
    "What is your fav food?",
    "I like burger"
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request,"blog/index.html")

def specific(request):
    return HttpResponse("specific")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)