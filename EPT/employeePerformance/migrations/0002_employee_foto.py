# Generated by Django 5.0.4 on 2024-06-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeePerformance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='foto',
            field=models.ImageField(default='/static/images/blank profile pic.png', upload_to='images/'),
            preserve_default=False,
        ),
    ]
