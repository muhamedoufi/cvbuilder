# Generated by Django 3.2.2 on 2021-06-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0007_auto_20210619_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='Competence',
            field=models.ManyToManyField(blank=True, to='sections.Competence'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='Experiences',
            field=models.ManyToManyField(blank=True, related_name='experiences', to='sections.Experience'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='Formations',
            field=models.ManyToManyField(blank=True, to='sections.Formation'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='Langues',
            field=models.ManyToManyField(blank=True, to='sections.Langue'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='Refferances',
            field=models.ManyToManyField(blank=True, to='sections.Réfférence'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='interet',
            field=models.ManyToManyField(blank=True, to='sections.Interet'),
        ),
    ]
