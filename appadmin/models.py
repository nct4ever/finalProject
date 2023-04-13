from django.db import models
from datetime import datetime
# Create your models here.

#User Information Model
class User(models.Model):
    username = models.CharField(max_length=50)  # user account
    password_hash = models.CharField(max_length=100)  # pwd
    password_salt = models.CharField(max_length=50)  # pwd salt
    status = models.IntegerField(default=1) #user status
    reg_time = models.DateTimeField(default=datetime.now) #user register time
    address = models.CharField(max_length=255,default="")
    email = models.CharField(max_length=255,default="")

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'password_hash': self.password_hash, 'status': self.status,
                'reg_time': self.reg_time.strftime('%Y-%m-%d %H:%M:%S'),'address': self.address,'email': self.email}

    class Meta:
        db_table = "user"  # change table name


#product Information Model
class Product(models.Model):
    product_name = models.CharField(max_length=50)  #  name
    product_info = models.CharField(max_length=255)  # information
    price = models.FloatField()
    picture = models.CharField(max_length=255)  # picture
    size = models.IntegerField()
    delivery = models.CharField(max_length=255)
    status = models.IntegerField(default=1)  #status
    category_id = models.IntegerField()  # category id


    def toDict(self):
        return {'id': self.id, 'product_name': self.product_name, 'product_info': self.product_info, 'price': self.price,
                'picture': self.picture, 'status': self.status,
                'category_id': self.category_id, 'size': self.size,'delivery': self.delivery}

    class Meta:
        db_table = "product"



#Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=255)  # category name


    def toDict(self):
        return {'id': self.id, 'category_name': self.category_name}

    class Meta:
        db_table = "category"  # change table name



#Size Model
class Size(models.Model):
    sizenum = models.CharField(max_length=50)  # category name


    def toDict(self):
        return {'id': self.id, 'sizenum': self.sizenum}

    class Meta:
        db_table = "sizeguide"  # change table name