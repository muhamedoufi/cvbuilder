# Generated by Django 3.2.2 on 2021-06-17 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_auto_20210617_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='Declaration',
        ),
        migrations.AddField(
            model_name='cv',
            name='Declaration',
            field=models.ManyToManyField(to='sections.DeclarationPerson'),
        ),
    ]
