# Generated by Django 4.1.7 on 2023-04-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'company', 'verbose_name_plural': 'companies'},
        ),
        migrations.RenameField(
            model_name='account',
            old_name='date_created',
            new_name='created_date',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avtar',
            field=models.ImageField(blank=True, upload_to='photos/users'),
        ),
    ]
