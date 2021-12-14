from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#from django.utils.datastructures import MultiValueDictKeyError

arr=['Java','Python','Cplusplus','C','DotNET','JavaScript','PHP','Swift','SQL','Ruby','Delphi','Objective-C','Go','Assemblylanguage','VisualBasic','D','R','Perl','MATLAB']
globalcnt=dict()

def index(request):
    mydictionary={
        'arr': arr
    }
    return render(request,'index.html',context=mydictionary)

# def getquery(request):
#     if 'q' in request.GET:
#         q = request.GET['languages']
#         return HttpResponse(q)
#         #print(q)
#     else:
#         q = False
#         #return HttpResponse(q)
        
def getquery(request):
    q=request.GET['languages']  
    if q in globalcnt:
        #if already exist then increment the value
        globalcnt[q]=globalcnt[q]+1
    else:
        #First Occurrence
        globalcnt[q]=1
    mydictionary={
        'arr': arr,
        'globalcnt': globalcnt
    }
    return render(request,'index.html',context=mydictionary)
    # try:
    #     mydictionary={
    #         'q':q
    #     }
    #     print(q)
        # return render(request,'index.html',context=mydictionary)

    # except:
    #     mydictionary = {
    #         'error':True
    #     }
    #     return render(request,'index.html',content=mydictionary)
# def languages(request):

def sortdata(request):
    global globalcnt
    globalcnt =dict(sorted(globalcnt.items(),key=lambda x:x[1], reverse=True))
    mydictionary={
        'arr': arr,
        'globalcnt': globalcnt
    }
    return render(request,'index.html',context=mydictionary)