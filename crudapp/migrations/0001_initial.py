# Generated by Django 3.1.3 on 2020-11-18 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('reference_name_and_email', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.designation')),
            ],
        ),
    ]
