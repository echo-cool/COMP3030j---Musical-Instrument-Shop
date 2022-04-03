import django_filters
from django.contrib.auth.models import User
from django.db.models import Q, QuerySet
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app import settings
from chat.models import MessageModel
from shop.models import Instrument, Category, Order, Review, Profile, InstrumentDetail, Cart, Wishlist
from .serializers import InstrumentSerializer, CategorySerializer, OrderSerializer, ReviewSerializer, ProfileSerializer, \
    InstrumentDetailSerializer, UserSerializer, CartSerializer, WishlistSerializer, MessageModelSerializer, \
    UserModelSerializer
from rest_framework import viewsets, permissions


class InstrumentsViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = InstrumentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', "name", 'posted_by']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', "name", ]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', "user", 'instrument', 'shopper_confirmed', 'delivery_confirmed']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ReviewSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProfileSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user']


class InstrumentDetailViewSet(viewsets.ModelViewSet):
    queryset = InstrumentDetail.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = InstrumentDetailSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', "instrument", ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['username', 'email', 'id']

    def list(self, request, *args, **kwargs):
        chat = self.request.query_params.get('chat', None)
        if chat is not None and chat == "true":
            messages = MessageModel.objects.filter(Q(recipient=request.user) |
                                                   Q(user=request.user))
            user_set = set()
            user_set.add(request.user.id)
            for message in messages:
                if message.user_id == request.user.id:
                    user_set.add(message.recipient_id)
                else:
                    user_set.add(message.user_id)
            self.queryset = self.queryset.filter(id__in=user_set)
        return super(UserViewSet, self).list(request, *args, **kwargs)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = WishlistSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication scheme used by DRF. DRF's SessionAuthentication uses
    Django's session framework for authentication which requires CSRF to be
    checked. In this case we are going to disable CSRF tokens for the API.
    """

    def enforce_csrf(self, request):
        return


class MessagePagination(PageNumberPagination):
    """
    Limit message prefetch to one page.
    """
    page_size = settings.MESSAGES_TO_LOAD


class MessageModelViewSet(ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS')
    authentication_classes = (CsrfExemptSessionAuthentication,)
    pagination_class = MessagePagination

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(Q(recipient=request.user) |
                                             Q(user=request.user))
        target = self.request.query_params.get('target', None)
        if target is not None:
            self.queryset = self.queryset.filter(
                Q(recipient=request.user, user__username=target) |
                Q(recipient__username=target, user=request.user))
        return super(MessageModelViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        msg = get_object_or_404(
            self.queryset.filter(Q(recipient=request.user) |
                                 Q(user=request.user),
                                 Q(pk=kwargs['pk'])))
        serializer = self.get_serializer(msg)
        return Response(serializer.data)

# class UserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#     allowed_methods = ('GET', 'HEAD', 'OPTIONS')
#     pagination_class = None  # Get all user
#
#     def list(self, request, *args, **kwargs):
#         # Get all users except yourself
#         self.queryset = self.queryset.exclude(id=request.user.id)
#         return super(UserModelViewSet, self).list(request, *args, **kwargs)
