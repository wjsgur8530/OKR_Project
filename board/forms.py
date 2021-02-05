from django.forms import ModelForm
from .models import *
from django import forms


class ContextForm(ModelForm):
    num = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center; width:70px;'}))
    task = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align:center; '
                                                                                              'width:200px;'}))
    context = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '300', 'style': 'text-align:center; width:300px;'}))
    expect = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align:center; '
                                                                                                'width:75px;'}))
    startdate = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'text-align:center; width:180px;', 'id': 'datepicker'}))
    enddate = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'text-align:center; width:180px;', 'id': 'datepicker1'}))
    time = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align:center; width:65px;'}))
    problem = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center; width:150px;'}))
    result = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align:center; width:70px;'}))
    solution = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center; width:100px;'}))
    team = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center; width:100px;'}))
    level = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center; width:65px;'}))

    class Meta:
        model = Board
        fields = (
        'num', 'task', 'context', 'expect', 'startdate', 'enddate', 'time', 'problem', 'result', 'solution', 'team',
        'level')


class CompanyForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '30', 'style': 'text-align:center;'}))
    context = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '35', 'style': 'text-align:center;'}))

    class Meta:
        model = Company
        fields = ('title', 'context')


class DepartmentForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center;'}))
    context = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '50', 'style': 'text-align:center;'}))

    class Meta:
        model = Departmentgoal
        fields = ('title', 'context')


class PersonalgoalForm(ModelForm):
    person = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '15', 'style': 'text-align:center;'}))
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center;'}))
    context = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '50', 'style': 'text-align:center;'}))

    class Meta:
        model = Personalgoal
        fields = ('person', 'title', 'context')


class ClassificationForm(ModelForm):
    num = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align:center'}))
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '20', 'style': 'text-align:center;'}))

    class Meta:
        model = Classification
        fields = ['num', 'title']
