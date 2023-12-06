from django.shortcuts import render, HttpResponse

def index(request):
    #return HttpResponse("HELLO I am ANAN !")
    context = {
        'var' : "(Hehe I am variable)"
    }
    return render(request, 'index.html',context)
def home(request):
    return HttpResponse("This is my home full of sadness and despair. Welcome to my misery")
def meow(request):
    return HttpResponse("Hey why are you meowing are you a cat. No meow. My cat died a while ago I loved him more than myself")


