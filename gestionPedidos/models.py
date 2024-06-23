from django.db import models

# Create your models here.
class Clients(models.Model):
  name = models.CharField(max_length=30, verbose_name="Nombre del Cliente", default='Sin Nombre')
  direction = models.CharField(max_length=50 , verbose_name = "Dirección")
  email = models.EmailField(blank = True, null = True, verbose_name="Correo Electronico") # Optional
  telephone = models.CharField(max_length=9, verbose_name = "Número de Teléfono")

  def __str__(self):
    return "El Usuario %s con direccion %s , email %s y con telefono %s" % (self.name, self.direction, self.email, self.telephone)

class Articles(models.Model):
  name = models.CharField(max_length = 30)
  section = models.CharField(max_length = 20)
  price = models.IntegerField(verbose_name="Precio")

  def __str__(self):
    return f"Nombre: {self.name}, Sección: {self.section}, Precio: {self.price}"

class Orders(models.Model):
  number = models.IntegerField()
  date = models.DateField()
  delivered = models.BooleanField()