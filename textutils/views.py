from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    print(djtext)

    rempun = request.POST.get('rempun','off')
    capall = request.POST.get('capall','off')
    newlineremover = request.POST.get('newlineremover','off')
    sparem = request.POST.get('sparem','off')
    charcount = request.POST.get('charcount','off')

    if rempun == "on":
        punctuations = '''!()-[]{};:'|'"\,"<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations',
                  'analyzed_text':analyzed}
        djtext = analyzed
    
    if (capall=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

            params = {'purpose':'Changed to Uppercase',
                  'analyzed_text':analyzed}
            djtext = analyzed
    
    if (newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose':'Removed New Lines',
                  'analyzed_text':analyzed}
        djtext = analyzed
    
    if (sparem=='on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose':'Remove Space',
                  'analyzed_text':analyzed}
        djtext = analyzed
    
    if (charcount=='on'):
        analyzed = str(len(djtext))

        params = {'purpose':'Character Count',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if (rempun!='on' and newlineremover!='on' and sparem!='on' and capall!='on' and charcount!='on'):
        return HttpResponse ("Error")
    
    return render(request,'analyze.html',params)