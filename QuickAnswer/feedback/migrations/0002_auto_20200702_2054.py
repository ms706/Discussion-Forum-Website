# Generated by Django 3.0.7 on 2020-07-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfeedback',
            old_name='type',
            new_name='feedback_type',
        ),
        migrations.AddField(
            model_name='userfeedback',
            name='feedback_content',
            field=models.TextField(default='Blank'),
        ),
    ]
