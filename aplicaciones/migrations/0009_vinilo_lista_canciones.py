# Generated by Django 4.2.1 on 2023-06-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0008_remove_vinilo_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinilo',
            name='lista_canciones',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]