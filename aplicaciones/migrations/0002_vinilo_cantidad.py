# Generated by Django 4.2.1 on 2023-05-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinilo',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]