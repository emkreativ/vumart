# Generated by Django 4.2.3 on 2023-11-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customuser_name_customuser_representer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='floor',
            new_name='note',
        ),
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
