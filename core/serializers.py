from rest_framework import serializers
from .models import Game, Offset, Pointer, Trainer

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class OffsetSerializer(serializers.ModelSerializer):
    game = serializers.StringRelatedField()
    
    class Meta:
        model = Offset
        fields = '__all__'

class PointerSerializer(serializers.ModelSerializer):
    game = serializers.StringRelatedField()
    
    class Meta:
        model = Pointer
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    game = serializers.StringRelatedField()
    
    class Meta:
        model = Trainer
        fields = '__all__'