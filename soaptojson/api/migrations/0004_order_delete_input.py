# Generated by Django 4.2 on 2023-04-30 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_input_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='input',
        ),
    ]
