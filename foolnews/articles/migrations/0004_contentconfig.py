# Generated by Django 2.2.7 on 2019-12-04 01:19

from django.db import migrations, models

#this initializes the main-article-slug to be 10-promise
def initialize_slug(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    ContentConfig = apps.get_model('articles', 'ContentConfig')
    content_config = ContentConfig(
        key = 'main-article-slug',
        value = '10-promise'
    )
    content_config.save()

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20191203_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),        
        migrations.RunPython(initialize_slug),
    ]
