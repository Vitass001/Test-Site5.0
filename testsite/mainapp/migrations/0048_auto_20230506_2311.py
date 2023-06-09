# Generated by Django 3.2.7 on 2023-05-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0047_legal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='confirm_video_recorded',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='firmware_up_to_date',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='property',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='sd_card_installed',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='set_up_pc_and_app',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='settings_optimized',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='train_staff',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
