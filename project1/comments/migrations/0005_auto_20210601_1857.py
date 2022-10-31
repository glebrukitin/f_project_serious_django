# Generated by Django 3.2.3 on 2021-06-01 15:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_new_date_created'),
        ('comments', '0004_delete_subcomment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('user', 'text', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'text', 'place')},
        ),
    ]
