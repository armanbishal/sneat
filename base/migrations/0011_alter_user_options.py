# Generated by Django 4.0.4 on 2022-06-05 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_user_created_at_user_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
    ]
