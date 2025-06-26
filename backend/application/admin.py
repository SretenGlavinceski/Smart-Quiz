from django.contrib import admin
from .models import *


class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerOptionInline, ]


admin.site.register(AnswerOption)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Section)