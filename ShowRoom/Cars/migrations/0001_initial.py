# Generated by Django 4.1.1 on 2022-09-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarName', models.CharField(max_length=20)),
                ('mpg', models.DecimalField(decimal_places=1, max_digits=5)),
                ('cyl', models.IntegerField()),
                ('disp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('hp', models.IntegerField()),
                ('drat', models.DecimalField(decimal_places=1, max_digits=5)),
                ('wt', models.DecimalField(decimal_places=1, max_digits=5)),
                ('qsec', models.DecimalField(decimal_places=1, max_digits=5)),
                ('vs', models.IntegerField()),
                ('am', models.IntegerField()),
                ('gear', models.IntegerField()),
                ('carb', models.IntegerField()),
            ],
        ),
    ]
