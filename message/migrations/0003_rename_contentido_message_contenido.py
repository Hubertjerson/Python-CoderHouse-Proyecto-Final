# Generated by Django 4.0.4 on 2022-07-24 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_rename_content_message_contentido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='contentido',
            new_name='contenido',
        ),
    ]