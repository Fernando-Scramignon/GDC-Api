from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
        
        (
            "companies",
            "0002_comapany_description_comapany_name_comapany_segment_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comapany",
            new_name="Company",
        ),
    ]
