from django.db import models


class ClassName(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = models.PositiveIntegerField(null=False)
    email = models.EmailField(null=False)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
