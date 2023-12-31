# Generated by Django 4.2.7 on 2023-11-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organ_app', '0008_rename_patient_age_organrequest_donor_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organrequest',
            name='patient_age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organrequest',
            name='patient_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='organrequest',
            name='patient_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
