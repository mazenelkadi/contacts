# Generated by Django 3.2.12 on 2023-09-16 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, max_length=30, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('sur_name', models.CharField(blank=True, max_length=30, null=True)),
                ('suffix', models.CharField(blank=True, max_length=30, null=True)),
                ('company_name', models.CharField(blank=True, max_length=40, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_type', models.CharField(blank=True, choices=[('Mobile', 'Mobile'), ('Work', 'Work'), ('Home', 'Home'), ('Office', 'Office')], default='M', max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('email_type', models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home'), ('Personal', 'Personal')], default='W', max_length=10)),
                ('address', models.TextField(blank=True, max_length=150, null=True)),
                ('address_type', models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home'), ('Personal', 'Personal')], default='W', max_length=10)),
                ('occasion_date', models.DateField(blank=True, null=True)),
                ('occasion', models.CharField(blank=True, choices=[('Birthday', 'Birthday'), ('Anniversary', 'Anniversary')], max_length=15, null=True)),
                ('relation', models.CharField(blank=True, choices=[('Assistant', 'Assistant'), ('Brother', 'Brother'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Father', 'Father'), ('Mother', 'Mother'), ('Friend', 'Friend'), ('Manager', 'Manager'), ('Partner', 'Partner'), ('Sister', 'Sister'), ('Spouse', 'Spouse'), ('Relative', 'Relative')], max_length=15)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
