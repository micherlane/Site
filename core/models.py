from django.db import models

class ItemAgenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    titulo = models.CharField('titulo',max_length=100)
    descricao = models.TimeField('descriçao')

    def __str__(self):
        return '{}-{}-{}'.format(
            self.data,self.hora,self.titulo
        )

    class Meta:
        verbose_name = 'itens agendados'
        ordering = ['-data']

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('data publicada')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text