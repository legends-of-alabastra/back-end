# Generated by Django 3.0.2 on 2020-01-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piratestwo', '0005_merchant_weapons_power'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerWeapons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField(default=0)),
                ('name', models.CharField(default='DEFAULT ITEM', max_length=255)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=255)),
                ('weapons_power', models.CharField(default='DEFAULT DESCRIPTION', max_length=255)),
            ],
        ),
    ]
