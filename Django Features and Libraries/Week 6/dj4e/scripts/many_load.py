from unesco.models import Category, States, Region, Iso, Site

import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load



def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name	description	justification	year	longitude	latitude	area_hectares	category	states	region	iso

    for row in reader:
        # print(row)

        category, created = Category.objects.get_or_create(name=row[7])
        states, created = States.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        name = row[0]
        description = row[1]
        justification = row[2]

        try:
            year = int(row[3])
        except:
            year = None

        try:
            longitude = float(row[4])
        except:
            longitude = None

        try:
            latitude = float(row[5])
        except:
            latitude = None

        try:
            area_hectares = float(row[6])
        except:
            area_hectares = None

        site = Site.objects.create(
            name = name,
            description = description,
            justification = justification,
            year = year,
            longitude = longitude,
            latitude = latitude,
            area_hectares = area_hectares,

            category = category,
            states = states,
            region = region,
            iso = iso,
        )
        site.save()

    print("Finished")