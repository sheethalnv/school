# Generated by Django 4.2.4 on 2023-12-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='email',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
