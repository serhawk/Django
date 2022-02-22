from django.db import models

class category(models.Model):
    productcategory = models.CharField(max_length=30,null=True)
    productsubcategory = models.CharField(max_length=30,null=True)
    stockfield = models.CharField(max_length=30,null=True)
    categoryclass=models.IntegerField(null=True)

    class Meta:
        db_table = "category"
      
        def __str__(self):
            return (self.productcategory, self.productsubcategory, self.stockfield,self.categoryclass)

class product(models.Model):
    order = models.ManyToManyField(category)
    name  = models.CharField(max_length=30,verbose_name="Product Name",null=True)
    genre = models.CharField(max_length=30,null=True,blank=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    picture  =models.ImageField(upload_to= "upload/", default="/p3.png" )
    date=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"

        def __str__(self):
            return (self.name, self.genre, self.price, self.quantity)






# Create your models here.
