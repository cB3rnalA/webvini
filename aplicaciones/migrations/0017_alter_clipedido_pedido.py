# Generated by Django 4.2.1 on 2023-06-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0016_alter_clipedido_cliente_alter_clipedido_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipedido',
            name='pedido',
            field=models.IntegerField(max_length=2000),
        ),
    ]
