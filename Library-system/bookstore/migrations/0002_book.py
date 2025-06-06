

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('uploaded_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('pdf', models.FileField(upload_to='bookapp/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='bookapp/covers/')),
            ],
        ),
    ]
