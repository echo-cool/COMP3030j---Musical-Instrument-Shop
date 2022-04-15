from django.urls import path
from rest_framework import routers
from .api import InstrumentsViewSet, CategoryViewSet, OrderViewSet, ReviewViewSet, InstrumentDetailViewSet, \
    ProfileViewSet, UserViewSet, CartViewSet, WishlistViewSet, MessageModelViewSet, PostViewSet, BlogCategoryViewSet
from .view import login, logout, rank_user_list, add_wishlist, add_cart, all_read, revenue_month

app_name = 'api'

router = routers.DefaultRouter()
router.register('instruments', InstrumentsViewSet, 'instruments')
router.register('category', CategoryViewSet, 'category')
router.register('order', OrderViewSet, 'order')
router.register('review', ReviewViewSet, 'review')
router.register('instrumentDetail', InstrumentDetailViewSet, 'instrumentDetail')
router.register('profile', ProfileViewSet, 'profile')
router.register('user', UserViewSet, basename='user')

# router.register('user_chat', UserModelViewSet, basename='user_chat')

router.register('cart', CartViewSet, 'cart')
router.register('wishlist', WishlistViewSet, 'wishlist')
router.register('message', MessageModelViewSet, 'message')
router.register('post', PostViewSet, 'post')
router.register('blog_category', BlogCategoryViewSet, 'blog_category')
# print(router.urls)
urlpatterns = router.urls + [
    path('login/', login, name='index'),
    path('logout/', logout, name='logout'),
    path('rank_user_list/', rank_user_list, name='rank_user'),
    path('add_wishlist/', add_wishlist, name='add_wishlist'),
    path('add_cart/', add_cart, name='add_cart'),
    path('all_read/', all_read, name='all_read'),
    path('revenue_month/', revenue_month, name='revenue_month'),
]
