

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_rename_creativity_prorating_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prorating',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
