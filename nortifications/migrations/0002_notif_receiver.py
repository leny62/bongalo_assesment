# Generated by Django 4.0.2 on 2022-02-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nortifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notif',
            name='receiver',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
    ]
