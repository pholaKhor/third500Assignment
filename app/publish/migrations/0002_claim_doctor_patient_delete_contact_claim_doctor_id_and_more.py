# Generated by Django 4.1.7 on 2023-06-22 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('ssn', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('email', models.CharField(db_index=True, max_length=255)),
                ('phone', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='claim',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.doctor'),
        ),
        migrations.AddField(
            model_name='claim',
            name='ssn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.patient'),
        ),
    ]
