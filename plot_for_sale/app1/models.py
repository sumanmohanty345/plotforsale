from django.db import models
class PlotModel(models.Model):
    plotno=models.IntegerField(primary_key=True)
    road_no=models.IntegerField()
    survey_no=models.IntegerField()
    cost_persqryrd=models.IntegerField()
    otherexpense=models.IntegerField()
    boundry=models.DecimalField(max_digits=5,decimal_places=2)
    facing=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    property_image=models.ImageField(upload_to='property_image/')
    total_cost=models.IntegerField(default=False)


class EmployeeModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    mail=models.EmailField()
    location=models.CharField(max_length=30)
    DOJ=models.DateField()
    designsation=models.CharField(max_length=30)
    qualification=models.CharField(max_length=40)
    remark=models.CharField(max_length=40)

class AppartmentModel(models.Model):
    Appartmentno = models.IntegerField(primary_key=True)
    road_no = models.IntegerField()
    survey_no = models.IntegerField()
    cost_perbhk = models.IntegerField()
    otherexpense = models.IntegerField()
    BHK = models.CharField(max_length=20)
    facing = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    Appartment_image = models.ImageField(upload_to='appartment_image/')
    totalcost=models.IntegerField(default=False)

