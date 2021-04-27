# Generated by Django 3.1.7 on 2021-04-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=32)),
                ('result', models.CharField(choices=[('gn_bbbl', 'General Bubble'), ('gn_bx_chrt', 'General Box Chart'), ('scat_mtrx', 'Scatter Matrix'), ('pie_chrt', 'Pie Chart'), ('ht_map', 'Heat Map')], max_length=16)),
            ],
        ),
    ]
