# Generated by Django 2.2.4 on 2019-09-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial1', '0002_auto_20190925_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofilesinventory',
            name='File1',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]