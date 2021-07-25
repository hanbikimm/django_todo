from django import forms
from todo.models import Todo
class TodoForm(forms.Form):
    class Meta:
        model = Todo #사용할 모델
        fields = ['title', 'contents'] # QuestionForm에서 사용할 Question 모델 속성