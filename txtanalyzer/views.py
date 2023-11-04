from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzer(request):
    text = request.POST.get('text','default')
    rempunc = request.POST.get('rempunc','off')
    capital = request.POST.get('capital','off')
    oneline = request.POST.get('oneline','off')
    remspace = request.POST.get('remspace','off')
    
    analyze = text
    if rempunc=='on':
        analyze = ''
        punc = '''~`!@#$%^&*()_+=-[]{}<>,./?'";:'''
        for char in text:
            if char  not in punc:
                analyze = analyze + char
    
    if capital=='on':
        analyze = analyze.upper()
    
    

    if remspace =='on':
        analyze = ''
        for i in range(len(text)):
            
            if text[i] ==" " and text[i+1]==" ":
                pass
            else:
                analyze +=text[i]
    

    
    params = {
        'text':text,
        'rempunc':rempunc,
        'capital':capital,
        'oneline':oneline,
        'remspace':remspace,
        'analyze': analyze
    }
    return render(request,'analyzer.html',params)