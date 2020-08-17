from django.contrib import admin

# Register your models here.
from Nav1.models import Question,Choice,Answer

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=4
class AnswerInline(admin.StackedInline):
    model=Answer
    extra=1

class ModelAdmin(admin.ModelAdmin):
    fieldsets=[('Question',{'fields':['question_text']}
        ),
        ('Date Information',{'fields':['pub_date']}
            )]
    list_display=['question_text','pub_date']
    inlines=[ChoiceInline,AnswerInline]

admin.site.register(Question,ModelAdmin)