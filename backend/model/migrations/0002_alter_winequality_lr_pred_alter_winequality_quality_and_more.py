# Generated by Django 4.2 on 2023-04-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winequality',
            name='lr_pred',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='winequality',
            name='quality',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='winequality',
            name='xgb_pred',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
