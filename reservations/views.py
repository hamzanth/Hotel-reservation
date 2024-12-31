from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class HotelListView(APIView):
	def get(self, resquest):
		resp = {"message": "The list of endpoints are shown here"}
		return Response(resp, 200)

