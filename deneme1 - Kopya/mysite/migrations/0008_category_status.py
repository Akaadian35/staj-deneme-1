# Generated by Django 3.2.5 on 2021-08-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('Build', 'Build'), ('RiotPoints', 'RiotPoints'), ('ValoPoints', 'ValorantPoints'), ('GUİDE', 'Rehber'), ('HEROS', 'Şampiyonlar')], default='Buildler', max_length=10),
        ),
    ]
