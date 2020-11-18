from django.db import models


class Designation(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    reference_name_and_email = models.CharField(
        max_length=200, null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
