# Generated by Django 3.2.5 on 2021-07-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20210730_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]