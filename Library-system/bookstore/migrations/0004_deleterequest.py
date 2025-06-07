

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_request', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
