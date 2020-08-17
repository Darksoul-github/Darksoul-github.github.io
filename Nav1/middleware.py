from telusko.settings import *
from django.urls import reverse
from django.shortcuts import redirect

#class ResultRedirectMiddleware:
 #   def __init__(self,get_response):
  #      self.get_response=get_response
   # def __call__(self,request):
    #    response=self.get_response(request)
     #   return response
   # def process_view(self,request,view_func,view_args,view_kwargs):
    #    path=request.path_info
     #  
      #  if path==reverse('result'):
       #     print('Hi this is logout page')
        #    return redirect (reverse('rev-result'))