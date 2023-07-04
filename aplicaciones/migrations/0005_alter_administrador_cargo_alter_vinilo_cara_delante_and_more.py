# Generated by Django 4.2.1 on 2023-06-19 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0004_carrito_cliente_delete_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='cargo',
            field=models.CharField(choices=[('Encargado ventas', 'Encargado ventas'), ('Administrador de usuarios', 'Administrador de usuarios'), ('Administrador de cuentas', 'Administrador de cuentas'), ('Encargado pagina web', 'Encargado pagina web')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vinilo',
            name='cara_delante',
            field=models.ImageField(upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='vinilo',
            name='cara_detras',
            field=models.ImageField(upload_to='productos'),
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=500)),
                ('monto', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicaciones.cliente')),
            ],
        ),
    ]