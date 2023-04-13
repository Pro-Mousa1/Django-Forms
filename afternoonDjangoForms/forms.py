from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()


class TeacherForm(forms.Form):
    name = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=1)
    salary = forms.FloatField()
    age = forms.IntegerField()


class StudentForm(forms.Form):
    name = forms.CharField(max_length=25)
    admission_no = forms.IntegerField()
    dormitory = forms.CharField()
    stream = forms.CharField()
    age = forms.CharField()
