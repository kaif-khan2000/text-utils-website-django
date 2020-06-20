# I have created this file - kaif
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyse(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    analysed = ""
    punctuation = '''~`!@#$%^&*()-{}[]:";'<>\,.?/*'''
    params = {
        "purpose":"",
        "analysed_text": analysed
    }
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuation:
                analysed = analysed + char
        djtext = analysed  
        params['analysed_text'] = analysed    
        params['purpose'] += 'remove punctuaion, '

    if newlineremover == 'on':
        analysed = ''
        for char in djtext:
            if char !='\n' and char!='\r':
                analysed += char
        djtext = analysed
        params['purpose'] += 'newline remover, '
        params['analysed_text'] = analysed

    if extraspaceremover == 'on':
        analysed = ''
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index-1] == " ":
                continue
            analysed += char
        djtext = analysed
        params['purpose'] += 'Extra Space Remover, '
        params['analysed_text'] = analysed

    if fullcaps == 'on':
        analysed = djtext.upper()
        params['purpose'] += "capitalise, "
        params['analysed_text'] = analysed    
    
    
    return render(request,'analyse.html',params)

def about(request):
    return render(request,'about.html')
