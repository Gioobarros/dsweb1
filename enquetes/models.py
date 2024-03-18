import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Pergunta(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data de publicação')
    def __str__(self):
        return '{} ({})'.format(self.texto, self.id)
    def publicada_recentemente(self):
        agora = timezone.now()
        return self.data_pub >= agora - datetime.timedelta(hours=24)

class Alternativa(models.Model):
    question = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return '{} ({})'.format(self.texto, self.id)