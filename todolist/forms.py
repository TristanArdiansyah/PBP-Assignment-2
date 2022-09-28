from cProfile import label
from turtle import title
from django import forms

class TaskList(forms.Form):
    titleField = forms.CharField(label='Title', max_length=100)
    descriptionField = forms.CharField(label='Description', max_length=100)