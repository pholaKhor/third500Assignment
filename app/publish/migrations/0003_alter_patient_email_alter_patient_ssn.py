# Generated by Django 4.1.7 on 2023-06-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0002_claim_doctor_patient_delete_contact_claim_doctor_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ssn',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
