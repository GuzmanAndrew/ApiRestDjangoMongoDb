from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.urls import reverse

from Alumnos.models import Facultades, Alumnos
from Alumnos.serializers import FacultadesSerializer, AlumnosSerializer

# Vistas de la API

@csrf_exempt
def facultadesApi(request, id=0):
    if request.method == 'GET':
        facultades = Facultades.objects.all()
        facultades_serializer = FacultadesSerializer(facultades, many=True)
        return JsonResponse(facultades_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        facultades_serializer = FacultadesSerializer(data=data)
        if facultades_serializer.is_valid():
            facultades_serializer.save()
            return JsonResponse("La facultad se agrego con exito", safe=False)
        return JsonResponse("Error al guardar facultad", safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        facultad = Facultades.objects.get(FacultadId=data['FacultadId'])
        facultades_serializer = FacultadesSerializer(facultad, data=data)
        if facultades_serializer.is_valid():
            facultades_serializer.save()
            return JsonResponse("La facultad se actualizo con exito", safe=False)
        return JsonResponse("Error al actualizar")
    elif request.method == 'DELETE':
        facultad = Facultades.objects.get(FacultadId=id)
        facultad.delete()
        # facultades = Facultades.objects.all()
        return JsonResponse("La facultad se elimino con exito", safe=False)

@csrf_exempt
def alumnosApi(request, id=0):
    if request.method == 'GET':
        alumnos = Alumnos.objects.all()
        alumnos_serializer = AlumnosSerializer(alumnos, many=True)
        return JsonResponse(alumnos_serializer.data, safe=False)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            alumnos_serializer = AlumnosSerializer(data=data)
            if alumnos_serializer.is_valid():
                alumnos_serializer.save()
                return JsonResponse("alumno agregado", safe=False)
            return JsonResponse("Error al guardar alumno", safe=False)
        except Exception as e:
            print(str(e))
            return JsonResponse(f"Error al guardar alumno: {str(e)}", safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        alumno = Alumnos.objects.get(AlumnoId=data['AlumnoId'])
        alumnos_serializer = AlumnosSerializer(alumno, data=data)
        if alumnos_serializer.is_valid():
            alumnos_serializer.save()
            return JsonResponse("alumno actualizado", safe=False)
        return JsonResponse("Error al actualizar")
    elif request.method == 'DELETE':
        alumno = Alumnos.objects.get(AlumnoId=id)
        alumno.delete()
        return JsonResponse("alumno eliminado", safe=False)
