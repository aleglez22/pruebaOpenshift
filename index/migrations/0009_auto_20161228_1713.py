# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20161228_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Apellido',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Cedula',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Gasto_acumulado',
            field=models.DecimalField(max_digits=4, null=True, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Telefono1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Telefono2',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='Serial',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='Tipo',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Accesorios',
            field=models.CharField(null=True, max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Costo_reparacion',
            field=models.DecimalField(max_digits=4, null=True, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Costo_revision',
            field=models.DecimalField(max_digits=4, null=True, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Estado_inicial',
            field=models.CharField(null=True, max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Falla',
            field=models.CharField(null=True, max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Fecha_entrega',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Fecha_ofrecida',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Informe_tecnico',
            field=models.CharField(null=True, max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Limite_garantia',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='Notas',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='Apellido',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
    ]
