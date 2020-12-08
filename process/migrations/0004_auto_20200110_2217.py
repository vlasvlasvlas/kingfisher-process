# Generated by Django 3.0.1 on 2020-01-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0003_collection_expected_files_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionnote',
            name='stored_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddConstraint(
            model_name='collectionnote',
            constraint=models.UniqueConstraint(fields=('collection', 'note'), name='unique_collection_note_identifiers'),
        ),
    ]