# Generated by Django 3.2.15 on 2022-08-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebServiceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('headers', models.TextField()),
                ('ip', models.CharField(max_length=50)),
                ('payload', models.TextField()),
                ('method', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=600)),
                ('status_code', models.CharField(max_length=100)),
                ('status_msg', models.CharField(max_length=100)),
                ('response', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Web Service Logs',
                'ordering': ['-created_on'],
            },
        ),
    ]
