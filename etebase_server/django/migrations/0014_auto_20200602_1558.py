# Generated by Django 3.0.3 on 2020-06-02 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_etebase", "0013_collectionmemberremoved"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userinfo",
            old_name="encryptedSeckey",
            new_name="encryptedContent",
        ),
    ]