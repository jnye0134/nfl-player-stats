# Generated by Django 2.0 on 2017-12-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl_data', '0007_auto_20171217_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='death_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hof_induction_year',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
