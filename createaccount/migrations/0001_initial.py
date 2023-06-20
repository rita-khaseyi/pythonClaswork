# Generated by Django 4.2.1 on 2023-06-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Default Name', max_length=32)),
                ('userId', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('dateofbirth', models.DateField()),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]
