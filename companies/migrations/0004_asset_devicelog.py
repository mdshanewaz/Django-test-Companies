# Generated by Django 4.1.7 on 2023-03-16 02:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_employee_email_alter_employee_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_out_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('checked_in_date', models.DateTimeField(blank=True, null=True)),
                ('checked_out_condition', models.CharField(max_length=100)),
                ('checked_in_condition', models.CharField(blank=True, max_length=100, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.employee')),
            ],
        ),
    ]
