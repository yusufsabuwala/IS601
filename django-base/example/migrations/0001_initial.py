# Generated by Django 3.1.1 on 2020-10-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BakedGood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=256)),
                ('good_type', models.CharField(choices=[('BG', 'Bagel'), ('BR', 'Bread'), ('CO', 'Cookie'), ('CA', 'CAKE'), ('PR', 'PRETZEL')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('recipe', models.TextField()),
            ],
        ),
    ]