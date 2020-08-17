from django.shortcuts import render,redirect
from Nav1.models import *
from Nav1.forms import *
from django.http import HttpResponse,HttpRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
y={}
length=0
@login_required
def home(request):
    y.clear()
    a=reverse(question,args=(1,))
    context={'question':a}
    return render(request,'test\home.html',context)

@login_required
def question(request,question_id):
     c=int(question_id)
     if (int(question_id)<=(len(Question.objects.all()))):
        rev_que=int(question_id)-1
        rev_ques=reverse(question,args=(rev_que,))
        output=Question.objects.get(id=question_id)
        lsit1=[1]
        qeustion_id=int(question_id)+1
        nex_que=reverse(question,args=(qeustion_id,))
        ch=Choice.objects.filter(choice=Question.objects.get(id=question_id))
        print(str(ch))
        context={'output':output,'question_id':int(question_id),'list':lsit1,'rev_que':rev_ques,'next':nex_que,'choice':ch}
        if request.method=="POST":
                answer=request.POST.get('choices')         
                if (str(answer)==str(Answer.objects.get(que=Question.objects.get(id=question_id)))):
                    global length
                    y[int(question_id)]=str(answer)
                    length=len(y)
                return redirect(reverse('question',args=(qeustion_id,)))
     else:
          
          return redirect(reverse('Logout'))
     return render(request,'test\question.html',context)

def result(request,score1=length):
         context={'score':length}
         return render(request,'test\\results.html',context)
def rev_result(request):
    return HttpResponse('Hi You had logged out successfully Page')
    


    
