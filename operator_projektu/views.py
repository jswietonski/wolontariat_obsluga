from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import OperatorProjektu, Kategoria, Inicjatywa, Uczestnik
from .serializers import OperatorProjektuSerializer , KategoriaSerializer, InicjatywaSerializer,  UczestnikSerializer
from rest_framework import status
from rest_framework import serializers
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Szukaj po kategorii': '/?category=category_name',
        'Dodaj operatora': 'operator/create',
        'Aktualizuj': 'operator/update/pk',
        'Usun': 'operator/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_operator(request):
    operator = OperatorProjektuSerializer(data=request.data)

    if OperatorProjektu.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Istnieje taki operator projektu')

    if operator.is_valid():
        operator.save()
        return Response(operator.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_operator(request):
    if request.query_params:
        operator = OperatorProjektu.objects.filter(**request.query_params.dict())
    else:
        operator = OperatorProjektu.objects.all()

    if operator:
        data = OperatorProjektuSerializer(operator, many=True).data   #Przy zwracaniu wielu wynikow musi byc atr many=True
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_operator(request, pk):
    item = OperatorProjektu.objects.get(pk=pk)
    data = OperatorProjektuSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_operator(request, pk):
    operator = get_object_or_404(OperatorProjektu, pk=pk)
    operator.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#Category endpoints

@api_view(['POST'])
def add_category(request):
    kategoria = KategoriaSerializer(data=request.data)

    if Kategoria.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Istnieje taka kategoria')

    if kategoria.is_valid():
        kategoria.save()
        return Response(kategoria.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])

def view_category(request):
    if request.query_params:
        kategoria = Kategoria.objects.filter(**request.query_params.dict())
    else:
        kategoria = Kategoria.objects.all()

    if kategoria:
        data = KategoriaSerializer(kategoria, many=True).data   #Przy zwracaniu wielu wynikow musi byc atr many=True
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_category(request, pk):
    item = Kategoria.objects.get(pk=pk)
    data = KategoriaSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_category(request, pk):
    kategoria = get_object_or_404(Kategoria, pk=pk)
    kategoria.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#Initiative endpoints

@api_view(['POST'])
def add_initiative(request):
    inicjatywa = InicjatywaSerializer(data=request.data)

    if Inicjatywa.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Istnieje taka inicjatywa')

    if inicjatywa.is_valid():
        inicjatywa.save()
        return Response(inicjatywa.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_initiative(request):
    if request.query_params:
        inicjatywa = Inicjatywa.objects.filter(**request.query_params.dict())
    else:
        inicjatywa = Inicjatywa.objects.all()

    if inicjatywa:
        data = InicjatywaSerializer(inicjatywa, many=True).data   #Przy zwracaniu wielu wynikow musi byc atr many=True
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_initiative(request, pk):
    item = Inicjatywa.objects.get(pk=pk)
    data = InicjatywaSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_initiative(request, pk):
    inicjatywa = get_object_or_404(Inicjatywa, pk=pk)
    inicjatywa.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


#Uzytkownik endpoints

# @api_view(['POST'])
# def add_user(request):
#     uzytkownik = UzytkownikSerializer(data=request.data)
#
#     if Uzytkownik.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('Istnieje taka kategoria')
#
#
#     if uzytkownik.is_valid():
#         uzytkownik.save()
#         return Response(uzytkownik.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET'])
# def view_user(request):
#     if request.query_params:
#         uzytkownik = Uzytkownik.objects.filter(**request.query_params.dict())
#     else:
#         uzytkownik = Uzytkownik.objects.all()
#
#     if uzytkownik:
#         data = UzytkownikSerializer(uzytkownik, many=True).data   #Przy zwracaniu wielu wynikow musi byc atr many=True
#         return Response(data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def update_user(request, pk):
#     item = Uzytkownik.objects.get(pk=pk)
#     data = UzytkownikSerializer(instance=item, data=request.data)
#
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['DELETE'])
# def delete_user(request, pk):
#     uzytkownik = get_object_or_404(Uzytkownik, pk=pk)
#     uzytkownik.delete()
#     return Response(status=status.HTTP_202_ACCEPTED)


#Uczestnik endpoints


@api_view(['POST'])
def add_participant(request):
    uczestnik = UczestnikSerializer(data=request.data)
    #print(uczestnik)
    #print(request.data)
    if Uczestnik.objects.filter(**request.data).exists():
        #print("nie dziala2")
        raise serializers.ValidationError('Istnieje taki uczestnik')


    if uczestnik.is_valid():
        uczestnik.save()
        return Response(uczestnik.data)
    else:
        print("nie dziala")
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_participant(request):
    if request.query_params:
        uczestnik = Uczestnik.objects.filter(**request.query_params.dict())
    else:
        uczestnik = Uczestnik.objects.all()

    if uczestnik:
        data = UczestnikSerializer(uczestnik, many=True).data   #Przy zwracaniu wielu wynikow musi byc atr many=True
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_participant(request, pk):
    item = Uczestnik.objects.get(id=pk)
    print(item)
    data = UczestnikSerializer(instance=item, data=request.data)
    print("tu wpada")
    print(request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        print("blad")
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def accept_participant(request, pk):
    item = Uczestnik.objects.get(id=pk)
    item.zaakceptowany = True
    print("tu wpada accept")

    item.save()
    return Response(UczestnikSerializer(item).data)


@api_view(['DELETE'])
def delete_participant(request, pk):
    uczestnik = get_object_or_404(Uczestnik, pk=pk)
    uczestnik.delete()
    return Response(status=status.HTTP_202_ACCEPTED)



