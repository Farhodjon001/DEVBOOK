from django.db import models
class Genre(models.Model):
    type_genre=models.CharField(max_length=100)

    def __str__(self):
        return self.type_genre

    class Meta:
        db_table = 'genre'
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField(null=True,blank=True)
    country = models.CharField(max_length=200,default='Uzbekistan')
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,default='')
    bio = models.TextField(default='')
    image = models.ImageField(upload_to='authors/',blank=True,null=True)


    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name


    class Meta:
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    year = models.DateField()
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,default='')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    bio= models.TextField(default='')
    image = models.ImageField(upload_to='books/',blank=True,null=True)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'books'