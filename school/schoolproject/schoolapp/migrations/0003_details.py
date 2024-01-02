# Generated by Django 4.2.4 on 2023-12-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('purpose', models.CharField(max_length=200)),
            ],
        ),
    ]
