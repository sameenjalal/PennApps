from django.db import models

# Create your models here.
class Consumable(models.Model):
    created_date = models.DateTimeField('Date Created')
    source = models.CharField(max_length=200)
    buzzword = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    data_blob = models.TextField()

    def pre_save(self):
        self.data_blob = pickle.dump(self.data_blob)
        return True

    def post_init(self):
        if(isinstance(self.data_blob,str)):
            self.data_blob = pickle.loads(self.data_blob)

