from django import forms

class StudentForm(forms.Form):
    names = forms.CharField(label="Имена учеников", widget=forms.Textarea(attrs={'rows': 4}))
    grades = forms.CharField(label="Оценки", widget=forms.Textarea(attrs={'rows': 4}))