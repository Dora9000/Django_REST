from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Shipment
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse('Hello world')


@api_view(['GET', 'POST', 'DELETE'])
def create_shipment(request):
    return HttpResponse('add shipment')


def get_shipment(request):
    return HttpResponse('get shipment')


def get_all_shipment(request):
    shipments = Shipment.objects.all()
    return HttpResponse('get all shipment')


def update_shipment(request):
    return HttpResponse('update shipment')


def delete_shipment(request):
    return HttpResponse('update shipment')