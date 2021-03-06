# Generated by Django 2.0 on 2017-12-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=2)),
                ('height', models.CharField(max_length=4)),
                ('weight', models.IntegerField()),
                ('current_team', models.CharField(max_length=3)),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=50)),
                ('death_date', models.DateField()),
                ('college', models.CharField(max_length=30)),
                ('high_school', models.CharField(max_length=30)),
                ('draft_team', models.CharField(max_length=3)),
                ('draft_round', models.IntegerField()),
                ('draft_position', models.IntegerField()),
                ('draft_year', models.DateField()),
                ('current_salary', models.IntegerField()),
                ('hof_induction_year', models.DateField()),
            ],
        ),
    ]
