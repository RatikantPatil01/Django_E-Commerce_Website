from django.db import models

STATE_CHOICES=(
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Solapur','Solapur'),
    ('Vijapur','Vijapur'),
    ('Suregaon','Suregaon')  ,
)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    locality=models.CharField(max_length=200,null=True,default='Solapur')
    city=models.CharField(max_length=50,null=True,default='Solapur')
    state=models.CharField(choices=STATE_CHOICES,max_length=50,null=True,default='Solapur')


    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False