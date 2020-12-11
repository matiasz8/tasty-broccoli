from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse(
        f"<html><p>Response Ok</p></html>", status=201)


