from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class PlansAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            title_search = request.query_params.get('title', None)
            data_order = request.query_params.get('data', None)
            plans = Plan.objects.filter(user=request.user)
            if title_search is not None:
                plans = plans.filter(title__icontains=title_search)
            if data_order is not None:
                if data_order == 'new':
                    plans = plans.order_by('-data_time')
                elif data_order == 'old':
                    plans = plans.order_by('data_time')
            serializer = PlanSerializer(plans, many=True)
            return Response(serializer.data, status=200)
        return Response(status=401)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = PlanSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        return Response(status=401)


class PlanAPIView(APIView):
    def get(self, request, pk):
        if request.user.is_authenticated:
            plan = get_object_or_404(Plan, pk=pk)
            if plan.user != request.user:
                return Response('Faqat userga tegishli plan chiqadi!', status=400)
            serializer = PlanSerializer(plan)
            return Response(serializer.data, status=200)
        return Response(status=401)


class PlanUpdateAPIView(APIView):
    def put(self, request, pk):
        if request.user.is_authenticated:
            plan = get_object_or_404(Plan, pk=pk)
            if plan.user != request.user:
                return Response("Faqat userga tegishli planni o'zgartirish mumkin!", status=400)
            serializer = PlanSerializer(plan, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response(status=401)


class PlanDeleteAPIView(APIView):
    def delete(self, request, pk):
        if request.user.is_authenticated:
            plan = get_object_or_404(Plan, pk=pk)
            if plan.user != request.user:
                return Response('Faqat userga tegishli plan ochiriladi!')
            plan.delete()
            return Response('Malumot ochirildi', status=204)
        return Response(status=401)
