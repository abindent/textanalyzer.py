# Generated by Django 4.0.4 on 2022-07-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timeStamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
