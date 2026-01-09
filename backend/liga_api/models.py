from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Liga(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    pais = models.CharField(max_length=50, blank=False)
    epoca = models.CharField(max_length=9)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f'{self.nome} - {self.epoca}'
    
class Equipa(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    treinador = models.CharField(max_length=100)
    ano_fundacao = models.PositiveIntegerField()
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, related_name='equipas')

    def __str__(self):
        return f'{self.nome} - {self.cidade}'
    
class Jogador(models.Model):
    POSICOES = [
        ('GR', 'Guarda-Redes'),
        ('DEF', 'Defesa'),
        ('MED', 'Médio'),
        ('AV', 'Avançado'),
    ]

    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=3, choices=POSICOES)
    numero = models.PositiveIntegerField()
    idade = models.PositiveIntegerField()
    equipa = models.ForeignKey(Equipa, on_delete=models.CASCADE, related_name='jogadores')

    class Meta:
        unique_together = ('equipa', 'numero')

    def __str__(self):
        return f'{self.nome} - {self.numero}'

class Jogo(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, related_name='jogos')
    equipa_casa = models.ForeignKey(
        Equipa, on_delete=models.CASCADE, related_name='jogos_casa'
        )
    equipa_visitante = models.ForeignKey(
        Equipa, on_delete=models.CASCADE, related_name='jogos_visitante'
        )
    data = models.DateField()
    golos_casa = models.PositiveIntegerField(default=0)
    golos_fora = models.PositiveIntegerField(default=0)

    def clean(self):
        if (self.equipa_casa == self.equipa_visitante):
            raise ValidationError('As equipas devem ser difrentes!')
        
        if self.equipa_casa.liga != self.liga or self.equipa_visitante.liga != self.liga:
            raise ValidationError('As devem pertencer à mesma liga do jogo!')
        
    def __str__(self):
        return f'{self.equipa_casa} vs {self.equipa_visitante}'
