# Generated by Django 2.1.5 on 2020-01-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_complain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='matric_number',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]