from django.db import models
from django.db.models import Q
i=-1
 #Create your models here.
class Question(models.Model):
   question_text=models.CharField(max_length=60)
   pub_date=models.DateTimeField()
   que=models.Manager()
   def __str__(self):
       return self.question_text
   class Meta:
       ordering=['pub_date']
       db_table='Polls App'

class Choice(models.Model):
    choice=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choice')
    result=models.CharField(max_length=30)
    votes=models.IntegerField(default=0)
    def __str__(self):
            return self.result
class Answer(models.Model):
    que=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='Answer')
    Answer_ques=models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.Answer_ques
    
