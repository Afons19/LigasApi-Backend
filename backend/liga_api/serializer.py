from .models import Liga, Equipa, Jogador, Jogo
from rest_framework import serializers

class LigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = '__all__'

    def clean(self, data):
        if self.data['data_fim'] < self.data['data_inicio']:
            raise serializers.ValidationError('A data do fim de torneio não pode ser anterior à data de início.')
        return data


class EquipaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipa
        fields = '__all__'

    def validate_ano_fundacao(self, value):
        if value < 1850:
            raise serializers.ValidationError("Ano de fundação inválido.")
        return value

class JogadorSerializer(serializers.ModelSerializer):
    equipa_nome = serializers.CharField(source='equipa.nome', read_only=True)
    class Meta:
        model = Jogador
        fields = '__all__'
    
    def validate_idade(self, value):
        if value < 15 or value > 50:
            raise serializers.ValidationError('Idade do jogador inválida.')
        return value
        
class JogoSerializer(serializers.ModelSerializer):
    equipa_casa_nome = serializers.CharField(source='equipa_casa.nome', read_only=True)
    equipa_visitante_nome = serializers.CharField(source='equipa_visitante.nome', read_only=True)
    class Meta:
        model = Jogo
        fields = '__all__'

    def validate(self, data):
        if data['equipa_casa'] == data['equipa_visitante']:
            raise serializers.ValidationError("As equipas devem ser diferentes.")

        if (
            data['equipa_casa'].liga != data['liga']
            or data['equipa_visitante'].liga != data['liga']
        ):
            raise serializers.ValidationError(
                "As equipas devem pertencer à mesma liga do jogo."
            )

        return data