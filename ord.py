import os
import sys
if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day71.settings")
    import django
    django.setup()
    from app01 import models
    ret=models.Employee.objects.all().values("id","dept")
    print(ret)
    from django.db.models import Avg
    ret=models.Employee.objects.values("dept").annotate(avg=Avg("salary")).values("dept","avg")
    print(ret)
    ret=models.Employee2.objects.values("dept").annotate(avg=Avg("salary")).values("dept__name","avg")
    print(ret)
    ret=models.Author.objects.select_related().values("name","books__title")
    print(ret)
    objs=[models.Book(title="沙河{}".format(i)) for i in range(100)]
    models.Book.objects.bulk_create(objs,10)











