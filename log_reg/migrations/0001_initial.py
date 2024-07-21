# Generated by Django 5.0.6 on 2024-07-21 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vegitable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('typee', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_sel', models.DateField(auto_now_add=True)),
                ('mavsum', models.CharField(max_length=50)),
            ],
        ),
    ]
