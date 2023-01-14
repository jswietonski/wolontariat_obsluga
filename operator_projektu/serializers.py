from django.db.models import fields
from rest_framework import serializers
from .models import OperatorProjektu, Kategoria, Inicjatywa,  Uczestnik


class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class OperatorProjektuSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperatorProjektu
        fields = '__all__'


class KategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kategoria
        fields = '__all__'


class InicjatywaSerializer(serializers.ModelSerializer):
    kategoria = RelatedFieldAlternative(queryset=Kategoria.objects.all(), serializer=KategoriaSerializer)
    operator = RelatedFieldAlternative(queryset=OperatorProjektu.objects.all(), serializer=OperatorProjektuSerializer)

    class Meta:
        model = Inicjatywa
        fields = '__all__'
        depth = 1


# class UzytkownikSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Uzytkownik
#         fields = '__all__'


class UczestnikSerializer(serializers.ModelSerializer):
    #uzytkownik = RelatedFieldAlternative(queryset=Uzytkownik.objects.all(), serializer=UzytkownikSerializer)
    inicjatywa = RelatedFieldAlternative(queryset=Inicjatywa.objects.all(), serializer=InicjatywaSerializer)
    class Meta:
        model = Uczestnik
        fields = '__all__'
        depth = 2
