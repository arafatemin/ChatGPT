import openai
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import *

openai_api_key = 'input_api_key'
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    print(response)
    answer = response.choices[0].message.content.strip()
    return answer

@login_required(login_url='login')
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        print(message)
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'ChatBot/chatbot.html', {'chats': chats})





@login_required(login_url='login')
def index(request):
    return render(request, 'Home/index.html')
