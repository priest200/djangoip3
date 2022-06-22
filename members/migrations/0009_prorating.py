

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_profile_profile_pic_alter_project_project_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prorating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('creativity', models.IntegerField(default=0)),
                ('developer', models.IntegerField(default=0)),
                ('pro_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.project')),
            ],
        ),
    ]
