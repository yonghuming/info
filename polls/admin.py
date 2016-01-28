#coding=utf-8
from django.contrib import admin

from .models import UserAdmin,Choice, Question, QuestionSort,Poll,User,UserPoll


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class PollUserAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'poll_id')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll)
admin.site.register(User,UserAdmin)
admin.site.register(UserPoll,PollUserAdmin)
