# Generated by Django 2.0.3 on 2019-09-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190904_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontEnd_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prestart_help', models.CharField(default='محتویات این فیلد را میتوانید در صفحه ادمین ویرایش کنید.', max_length=8192)),
            ],
        ),
        migrations.DeleteModel(
            name='SiteProperty',
        ),
    ]