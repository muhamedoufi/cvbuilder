# Generated by Django 3.2.2 on 2021-06-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidat', '0003_auto_20210615_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='Image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]