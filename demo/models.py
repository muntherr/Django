from django.db import models


# Create your models here.
class Book(models.Model):
    status = {
        (0, 'Unkown'),
        (1, 'processed'),
        (2, 'paid')
    }
    title = models.CharField(max_length=36, blank=False, unique=True)  # ,null=True,, default='',
    # choices=status ) #Simple text String
    # We need to create migrate to apply the migration file to update the data base
    # By using  : python3 manage.py create migrations
    # All inputs from this object will store  in the database
    # Define some arguments to the CharField func

    description = models.TextField(max_length=256, blank= True)

    price = models.DecimalField(default=0, max_digits=20 , decimal_places=2)
           #models.AnynumberTypes
    published = models.DateField(blank=True, null=True, default= None)
    #auto_now : Save the date for current date when the book is saved on
    # publishedTime = models.TimeField(auto_now=True, auto_now_add=True)
    #Use just the time for the data base
    # publishedTimeDate = models.DateTimeField(auto_now=True, auto_now_add=True)
    #Date and time are used for it

    isPublished = models.BooleanField(default=False)

    cover = models.FileField(upload_to='covers/', blank=True) #Will allow us to add a file for this specific book
    # Image = models.ImageField(upload_to='covers/') #Will allow us to add a images for this specific book


    def __str__(self): # Convert the object to string and show it in the admin site
        return  self.title