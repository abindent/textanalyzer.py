# Generated by Django 4.0.4 on 2022-06-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_gist_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
