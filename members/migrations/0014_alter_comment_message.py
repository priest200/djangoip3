

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(),
        ),
    ]
