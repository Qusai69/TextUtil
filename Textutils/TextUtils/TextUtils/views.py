
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    djtext = request.POST.get('text','default')
    removepunc  = request.POST.get('removepunc','off')
    Cap  = request.POST.get('Capfirst','off')
    NewLR  = request.POST.get('NLR','off')
    SpaceR  = request.POST.get('SR','off')
    CharC  = request.POST.get('CC','off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if (Cap =='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            'analyzed_text':analyzed,
            'purpose':'Capitalized Letters'
        }
        djtext = analyzed
    
    if (NewLR == 'on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
        params = {
            'analyzed_text':analyzed,
            'purpose':'New Line Remover'
        }
        djtext = analyzed
    
    if (SpaceR == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {
            'analyzed_text':analyzed,
            'purpose':'Extra Space Remover'
        }
        djtext = analyzed
    
    if (CharC == 'on'):
        analyzed = 0
        for char in djtext:
            if char!= " ":
                analyzed = analyzed + 1
        params = {
            'analyzed_text':analyzed,
            'purpose':'Character Counter'
        }
        djtext = analyzed
    if(removepunc != "on" and NewLR!="on" and SpaceR!="on" and CharC!="on" and Cap!="on" ):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
    
        
