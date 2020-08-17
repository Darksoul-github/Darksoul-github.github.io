from . import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('question/<str:question_id>/',views.question,name='question'),
    path('results/',views.result,name='result'),
    path('home1',views.rev_result,name='Home1'),
    path('Login/',LoginView.as_view(),name='Login'),
    path('logout/',LogoutView.as_view(),name='Logout'),
    path('home/',views.home,name='Home'),
    ]


#from django.urls import path

#from . import views

#urlpatterns = [
 #   path('', views.index, name='index'),
#]