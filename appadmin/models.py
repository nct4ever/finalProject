from django.db import models
from datetime import datetime


# Create your models here.

# User Information Model



class User(models.Model):
    username = models.CharField(max_length=50)  # user account
    password_hash = models.CharField(max_length=100)  # pwd
    password_salt = models.CharField(max_length=50)  # pwd salt
    status = models.IntegerField(default=1)  # user status
    reg_time = models.DateTimeField(default=datetime.now)  # user register time
    address = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'password_hash': self.password_hash, 'status': self.status,
                'reg_time': self.reg_time.strftime('%Y-%m-%d %H:%M:%S'), 'address': self.address, 'email': self.email}

    class Meta:
        db_table = "user"  # change table name


# product Information Model
class Product(models.Model):
    product_name = models.CharField(max_length=50)  # name
    product_info = models.CharField(max_length=255)  # information
    price = models.FloatField()
    picture = models.CharField(max_length=255)  # picture
    size = models.IntegerField()
    delivery = models.CharField(max_length=255)
    status = models.IntegerField(default=1)  # status
    category_id = models.IntegerField()  # category id
    sub_id = models.IntegerField(default=1)

    def toDict(self):
        return {'id': self.id, 'product_name': self.product_name, 'product_info': self.product_info,
                'price': self.price,
                'picture': self.picture, 'status': self.status,
                'category_id': self.category_id, 'size': self.size, 'delivery': self.delivery, 'sub_id': self.sub_id}

    class Meta:
        db_table = "product"


# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=255)  # category name

    def toDict(self):
        return {'id': self.id, 'category_name': self.category_name}

    class Meta:
        db_table = "category"  # change table name


# Size Model
class Size(models.Model):
    sizenum = models.CharField(max_length=50)  # category name

    def toDict(self):
        return {'id': self.id, 'sizenum': self.sizenum}

    class Meta:
        db_table = "sizeguide"  # change table name

class Orders(models.Model):
    member_id = models.IntegerField() #会员id
    money = models.FloatField()     #金额
    status = models.IntegerField(default=1)   #订单状态:1过行中/2无效/3已完成
    create_time = models.DateTimeField(default=datetime.now)  #创建时间

    class Meta:
        db_table = "orders"  # 更改表名


#订单详情模型
class OrderDetail(models.Model):
    order_id = models.IntegerField()  #订单id
    product_id = models.IntegerField()  #菜品id
    product_name = models.CharField(max_length=50) #菜品名称
    price = models.FloatField()     #单价
    quantity = models.IntegerField()  #数量
    status = models.IntegerField(default=1) #状态:1正常/9删除

    class Meta:
        db_table = "order_detail"  # 更改表名


# 支付信息模型
class Payment(models.Model):
    order_id = models.IntegerField()  #订单id号
    member_id = models.IntegerField() #会员id
    money = models.FloatField()     #支付金额
    type = models.IntegerField()      #付款方式：1会员付款/2收银收款
    bank = models.IntegerField(default=1) #收款银行渠道:1微信/2余额/3现金/4支付宝
    status = models.IntegerField(default=1) #支付状态:1未支付/2已支付/3已退款
    create_time = models.DateTimeField(default=datetime.now)  #创建时间

    class Meta:
        db_table = "payment"  # 更改表名

# Shipping Model
class Shipping(models.Model):
    user_id = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def toDict(self):
        return {'id': self.id, 'user_id': self.user_id,'address': self.address, 'city': self.city,
                'state': self.state, 'zipcode': self.zipcode}

    class Meta:
        db_table = "shipping"  # change table name


# subcategory Model
class Subcategories(models.Model):
    subname = models.CharField(max_length=255)  # category name
    cate_id = models.IntegerField(default=1)

    def toDict(self):
        return {'id': self.id, 'subname': self.subname, 'cate_id': self.cate_id}

    class Meta:
        db_table = "subcategories"  # change table name



class Rate(models.Model):
    reviews = models.CharField(max_length=500)
    rating = models.IntegerField(default=1)
    user_id = models.IntegerField(default=1)
    product_id = models.IntegerField(default=1)
    create_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.id, 'reviews': self.reviews,'rating': self.rating,'user_id': self.user_id, 'product_id': self.product_id,'create_time': self.create_time}

    class Meta:
        db_table = "rate"  # change table name


