from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View

# Create your views here.
class HotelListView(APIView):
	def get(self, resquest):
		resp = {"message": "The list of endpoints are shown here"}
		return Response(resp, status=200)

class DocumentationView(View):
	def get(self, request):
		return render(request, "documentation.html")