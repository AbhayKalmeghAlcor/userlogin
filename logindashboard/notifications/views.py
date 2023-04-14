from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Notification
from .serializers import NotifiactionSerializer


class NotifiactionViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotifiactionSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(recipient=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(recipient=self.request.user)

    def perform_update(self, serializer):
        serializer.save(is_read=True)
