6

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='country',
            field=models.CharField(default='No specified', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='posted_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
