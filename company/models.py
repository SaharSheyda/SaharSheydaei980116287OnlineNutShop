from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length = 80,verbose_name=" نام محصول")
    price = models.IntegerField(verbose_name=" قیمت هر کیلوگرم به تومان")
    quantity = models.DecimalField(max_digits=6, decimal_places=2,verbose_name=" مقدار به کیلوگرم")
    classification = models.ForeignKey("Classification", on_delete=models.CASCADE, verbose_name="دسته بندی")
    pic = models.ImageField(verbose_name="تصویر محصول")
    supplier = models.ManyToManyField('Supplier', verbose_name="تامین کننده")
    grade = models.CharField(max_length = 20,verbose_name="کیفیت", choices= [('a','درجه یک'),('b','درجه دو')], default= ('a','درجه یک'))

    def __str__(self):
        return self.name

class Classification(models.Model):
    title = models.CharField(max_length = 100, verbose_name="دسته بندی")
    
    def __str__(self):
        return self.title
    
class City(models.Model):
    name = models.CharField(max_length = 100, verbose_name="نام شهر")
        
    def __str__(self):
        return self.name
        
class Inventory(models.Model):
    city = models.ForeignKey("City", on_delete = models.CASCADE, verbose_name="شهر انبار")
        
    def __str__(self):
        return str(self.city)

class InventoryProduct(models.Model):
    name = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name=" نام محصول")
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE, verbose_name="انبار")
    quantity = models.PositiveIntegerField(blank=False, verbose_name="مقدار به کیلوگرم")

    def __str__(self):
        return self.name.name


class Supplier(models.Model):
    name = models.CharField(max_length=80, verbose_name="نام تامین کننده")
    email = models.EmailField(verbose_name="ایمیل")
    phone_regex  = RegexValidator(regex=r'^\+?98?\d{9,15}$', message="Phone number must be entered in the format: '+989123456789'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True , default="+989123456789",verbose_name="تلفن همراه")
    
    def __str__(self):
        return self.name
        
from accounts.models import CustomUser
    
class Order(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="سفارش دهنده")
    product = models.ForeignKey(InventoryProduct, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(blank=False, verbose_name="تعداد")

    SUBMITTED = 'ثبت شد'
    READY_TO_SEND = 'آماده ارسال'
    STATUS_CHOICES = [
        (SUBMITTED, 'ثبت شد'),
        (READY_TO_SEND, 'آماده ارسال'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SUBMITTED, verbose_name="وضعیت")

    def __str__(self):
        return str ('{name} ({prod} * {quan})'.format(name=self.username.username, prod=self.product, quan=self.quantity))


class JobOffer(models.Model): 
    job_title    = models.CharField(default="فروشنده ی خشکبار تهران", max_length=70)
    first_name   = models.CharField(max_length=20)  
    last_name    = models.CharField(max_length=30) 
    age          = models.IntegerField()
    Years_of_WorkExperience = models.IntegerField(default="2")
    phone_number = models.CharField(max_length=11, blank=True , default="09192999154") # Validators should be a list 
    email      = models.EmailField(max_length=50)
    skills    = models.CharField(max_length=500, default="توانایی مذاکره و روابط عمومی بالا") 
    previous_jobs = models.CharField(max_length=400, default="شغلی نداشته ام")
    Parvane_Kasb = models.IntegerField(default="402349034")


    def __str__(self):
        return self.job_title
    
    def get_absolute_url(self):
        return reverse('offer_detail', args=[str(self.id)])
