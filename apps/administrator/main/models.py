from django.db import models

# class User(models.Model):
#     ADMIN = 'admin'
#     NORMAL = 'normal'
#     ROLES = [
#         [ADMIN, 'Administrador'],
#         [NORMAL, 'Normal'],
#     ]
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=50)
#     login = models.CharField(max_length=20)
#     password = models.CharField(max_length=200)
#     role = models.CharField(max_length=100, choices=ROLES)
#     active = models.BooleanField(default=True)
#
#     def __unicode__(self):
#         return self.name
