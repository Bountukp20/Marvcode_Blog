# Generated by Django 4.0.4 on 2023-10-28 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_newsletter_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='pub_date',
        ),
    ]