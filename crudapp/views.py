from django.shortcuts import render, redirect
from .forms import ApplicantForm
from .models import Applicant

# Create your views here.


def applicant_list_view(request):
    context = {'applicant_list': Applicant.objects.all()}
    return render(request, "applicant_list.html", context)


def applicant_form_view(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ApplicantForm()
        else:
            applicant = Applicant.objects.get(pk=id)
            form = ApplicantForm(instance=applicant)
        return render(request, "applicant_form.html", {'form': form})
    else:
        if id == 0:
            form = ApplicantForm(request.POST)
        else:
            applicant = Applicant.objects.get(pk=id)
            form = ApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
        return redirect('/list')


def applicant_delete_view(request, id):
    applicant = Applicant.objects.get(pk=id)
    applicant.delete()
    return redirect('/list')
