# Generated by Django 3.1.1 on 2020-09-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0039_auto_20200924_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='under_eighteen_requirments',
            field=models.TextField(blank=True, null=True, verbose_name='Special under 18 requirements'),
        ),
    ]