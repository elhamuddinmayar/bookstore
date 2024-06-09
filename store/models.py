from django.db import models
from django.core.validators import MinValueValidator

class Collection(models.Model):
    title=models.CharField(max_length=255)
    featured_product=models.ForeignKey('Bookstore',on_delete=models.SET_NULL,null=True,related_name="+")
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["title"]
class Bookstore(models.Model):
    title=models.CharField(max_length=255)
    author=models.TextField(null=False,blank=False)
    p_date=models.DateTimeField(auto_now=True)
    ISBN=models.IntegerField()
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    price=models.DecimalField(max_digits=6,decimal_places=2,validators=[MinValueValidator(1)])
    img=models.ImageField(upload_to="pics")
    def __str__(self):
        return self.title
    
        
    class Meta:
        ordering=["title"]
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,"برونز"),
        (MEMBERSHIP_SILVER,"نقره"),
        (MEMBERSHIP_GOLD,"طلایی")
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birh_data=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)