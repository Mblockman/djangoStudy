from django.contrib import admin
from .models import Choice, Question

# Register your models here.
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [

        ('Date information', {'fields': ['pub_date']}),
        ('Text information',               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
#admin.site.register(Question)
