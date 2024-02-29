

from django.shortcuts import render
from .models import Node, Edge

def index(request):
    nodes = Node.objects.all()
    edges = Edge.objects.all()
    return render(request, 'network_app/index.html', {'nodes': nodes, 'edges': edges})