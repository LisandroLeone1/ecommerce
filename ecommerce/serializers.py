from rest_framework import serializers
from .models import (
    TalleIndumentaria, TalleCalzado, TalleAccesorio, 
    Marca, Categoria, Color, Producto
)

# Serializers para modelos básicos
class TalleIndumentariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalleIndumentaria
        fields = '__all__'

class TalleCalzadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalleCalzado
        fields = '__all__'

class TalleAccesorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalleAccesorio
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

# Serializer de Producto con datos completos
class ProductoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    categoria = CategoriaSerializer()
    colores = ColorSerializer(many=True)
    talles_indumentaria = TalleIndumentariaSerializer(many=True)
    talles_calzado = TalleCalzadoSerializer(many=True)
    talles_accesorios = TalleAccesorioSerializer(many=True) # many quiere decir que un producto puede tener varios talles

    class Meta:
        model = Producto
        fields = '__all__'
