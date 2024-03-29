# Generated by Django 4.2 on 2023-04-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WineQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_acidity', models.FloatField()),
                ('volatile_acidity', models.FloatField()),
                ('citric_acid', models.FloatField()),
                ('residual_sugar', models.FloatField()),
                ('chlorides', models.FloatField()),
                ('free_sulfur_dioxide', models.FloatField()),
                ('total_sulfur_dioxide', models.FloatField()),
                ('density', models.FloatField()),
                ('pH', models.FloatField()),
                ('sulphates', models.FloatField()),
                ('alcohol', models.FloatField()),
                ('quality', models.IntegerField()),
                ('lr_pred', models.IntegerField()),
                ('xgb_pred', models.IntegerField()),
            ],
        ),
    ]
