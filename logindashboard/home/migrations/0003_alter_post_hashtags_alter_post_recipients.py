# Generated by Django 4.1.7 on 2023-04-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_post_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtags',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='recipients',
            field=models.TextField(),
        ),
    ]