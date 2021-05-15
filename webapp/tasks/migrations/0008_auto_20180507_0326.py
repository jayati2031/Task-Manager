

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20180506_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('adanger', 'Priority 1'), ('bwarning', 'Priority 2'), ('csuccess', 'Priority 3'), ('dprimary', 'Priority 4')], default='Select Priority', max_length=30),
        ),
    ]
