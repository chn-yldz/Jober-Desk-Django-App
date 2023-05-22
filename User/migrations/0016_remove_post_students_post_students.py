# Generated by Django 4.0.1 on 2022-08-01 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_business_gmail_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='students',
        ),
        migrations.AddField(
            model_name='post',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.student'),
        ),
    ]