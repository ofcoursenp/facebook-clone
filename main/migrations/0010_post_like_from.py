# Generated by Django 4.1.2 on 2023-02-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_defineuser_user_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_from',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]