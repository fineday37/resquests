# Generated by Django 3.2.10 on 2022-02-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_contact_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publish', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
