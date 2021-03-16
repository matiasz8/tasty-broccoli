from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse(f"<html><p>Response Tasty OK</p></html>", status=201)
