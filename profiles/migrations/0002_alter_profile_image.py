# Generated by Django 3.2.14 on 2022-08-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_zq8liz.jpg', upload_to='images/'),
        ),
    ]