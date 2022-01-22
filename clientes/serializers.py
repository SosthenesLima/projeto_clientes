from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF Inválido!"})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números nesse Campo!"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O Rg deve ter 9 dígitos!"})
    
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O Número do celular deve seguir este modelo 63 99204-4419, (respeitando os espaços e traço)"})
        
        return data
    
    