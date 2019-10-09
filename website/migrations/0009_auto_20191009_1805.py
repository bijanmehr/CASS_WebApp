# Generated by Django 2.0.3 on 2019-10-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20191007_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosesession',
            name='game_algorithm_judgement',
            field=models.CharField(default='NA', max_length=64),
        ),
        migrations.AddField(
            model_name='diagnosesession',
            name='toycar_algorithm_judgement',
            field=models.CharField(default='NA', max_length=64),
        ),
        migrations.AddField(
            model_name='diagnosesession',
            name='voice_screening_judgement',
            field=models.CharField(default='NA', max_length=64),
        ),
        migrations.AlterField(
            model_name='diagnosesession',
            name='expertsystem_judgement',
            field=models.CharField(default='NA', max_length=64),
        ),
    ]