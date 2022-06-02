# Generated by Django 4.0.4 on 2022-06-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_picture_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('French', 'French'), ('German', 'German'), ('Portugese', 'Portugese')], default='English', max_length=9),
        ),
    ]