from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializers = RegisterSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message': 'User registered successfully'},status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message': 'Hello, this is a public endpoint'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello {request.user.username}, this is a private endpoint"})

