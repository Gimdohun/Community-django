# Generated by Django 3.2.14 on 2022-07-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='issueName',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='community',
            name='issueProf',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='community',
            name='issueRoom',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='community',
            name='issueTime',
            field=models.TimeField(default=' '),
        ),
    ]
