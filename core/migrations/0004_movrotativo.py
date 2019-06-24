# Generated by Django 2.2.1 on 2019-05-21 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_parametros'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovRotativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pago', models.BooleanField(default=False)),
                ('veiculo', models.ForeignKey(on_delete=False, to='core.Veiculo')),
            ],
        ),
    ]
