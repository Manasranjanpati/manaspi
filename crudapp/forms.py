from django import forms
from .models import Applicant


class ApplicantForm(forms.ModelForm):

    class Meta:
        model = Applicant
        fields = ('first_name', 'last_name', 'email',
                  'mobile', 'designation', 'reference_name_and_email')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',

            'reference_name_and_email': 'Reference Name & Email'
        }

    def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args, **kwargs)
        self.fields['designation'].empty_label = "Select"
        self.fields['reference_name_and_email'].required = False
