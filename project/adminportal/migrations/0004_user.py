# Generated by Django 4.0.2 on 2022-02-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0003_remove_safeambassador_email_region_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('should_ban', models.BooleanField()),
            ],
        ),
    ]
