# Generated by Django 3.2.7 on 2023-03-08 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20230308_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content1',
        ),
    ]