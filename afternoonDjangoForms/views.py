from django.shortcuts import render
from .forms import UserForm, TeacherForm, StudentForm


def register(request):
    submit_button = request.POST.get('submit')
    name = ''
    email = ''
    password = ''

    form = UserForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
    context = {'form': form, 'name': name, 'email': email,
               'password': password, 'submit_button': submit_button}
    return render(request, 'register.html', context)


def teacherReg(request):
    submit_button = request.POST.get("t-submit")
    name = ''
    gender = ''
    salary = ''
    age = ''
    mwalimu_form = TeacherForm(request.POST or None)
    if mwalimu_form.is_valid():
        name = mwalimu_form.cleaned_data.get("name")
        gender = mwalimu_form.cleaned_data.get("gender")
        salary = mwalimu_form.cleaned_data.get("salary")
        age = mwalimu_form.cleaned_data.get("age")
    context = {'mwalimu_form': mwalimu_form, 'name': name, 'gender': gender,
               'salary': salary, 'age': age, 'submit_button':submit_button}

    return render(request, 'teacher_reg.html', context)


def student(request):
    submit_button = request.POST.get("s-submit")
    name = ''
    admission_no = ''
    dormitory = ''
    stream = ''
    age = ''
    studente_form = StudentForm(request.POST or None)
    if studente_form.is_valid():
        name = studente_form.cleaned_data.get("name")
        admission_no = studente_form.cleaned_data.get("admission_no")
        dormitory = studente_form.cleaned_data.get("dormitory")
        stream = studente_form.cleaned_data.get("stream")
        age = studente_form.cleaned_data.get("age")
    context = {'studente_form': studente_form, 'name': name, 'admission_no': admission_no,
               'dormitory': dormitory, 'stream': stream, 'age': age,
               'submit_button': submit_button}
    return render(request, 'student.html', context)
