# Generated by Django 5.0.6 on 2024-05-31 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('Book_issued', models.CharField(max_length=100)),
                ('Date_issued', models.DateField()),
                ('Date_return', models.DateField(null=True)),
            ],
        ),
    ]