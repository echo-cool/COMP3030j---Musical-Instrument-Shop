from django.urls import path

from . import views

app_name = 'management'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index_new, name='index'),
    # path('new', views.new, name='new'),
    path('order_management/all/new', views.order_management_all_new, name='order_management_all_new'),
    path('instrument_management/new', views.instrument_management_new, name='instrument_management_new'),
    path('order_management/all/', views.order_management_all, name='order_management_all'),
    path('order_management/placed/', views.order_management_placed, name='order_management_placed'),
    path('order_management/accepted/', views.order_management_accepted, name='order_management_accepted'),
    path('order_management/packed/', views.order_management_packed, name='order_management_packed'),
    path('order_management/shipped/', views.order_management_shipped, name='order_management_shipped'),
    path('order_management/delivered/', views.order_management_delivered, name='order_management_delivered'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('order_item_management/<int:order_id>/', views.order_item_management, name='order_item_management'),
    path('update_order_item/<int:order_item_id>/', views.update_order_item, name='update_order_item'),
    path('instrument_management/', views.instrument_management, name='instrument_management'),
    path('update_instrument/<int:instrument_id>/', views.update_instrument, name='update_instrument'),
    path('add_instrument/', views.add_instrument, name='add_instrument'),
    path('instrument_category_management/', views.instrument_category_management, name='instrument_category_management'),
    path('update_instrument_category/<int:category_id>/', views.update_instrument_category, name='update_instrument_category'),
    path('add_instrument_category/', views.add_instrument_category, name='add_instrument_category'),
    path('add_order/', views.add_order, name='add_order'),
    path('profile/', views.profile, name='profile'),
    path('review_management/', views.review_management, name='review_management'),
    path('update_review/<int:review_id>/', views.update_review, name='update_review'),
    path('add_review/', views.add_review, name='add_review'),
    path('order_state/<order_id>', views.order_state, name='order_state'),
    path('post_management/', views.post_management, name='post_management'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('blog_category_management/', views.blog_category_management, name='blog_category_management'),
    path('update_blog_category/<int:category_id>/', views.update_blog_category, name='update_blog_category'),
    path('add_blog_category/', views.add_blog_category, name='add_blog_category'),
    path('cart_management/', views.cart_management, name='cart_management'),
    path('update_cart/<int:cart_id>/', views.update_cart, name='update_cart'),
    path('add_cart/', views.add_cart, name='add_cart'),
    path('wishlist_management/', views.wishlist_management, name='wishlist_management'),
    path('update_wishlist/<int:wishlist_id>/', views.update_wishlist, name='update_wishlist'),
    path('add_wishlist/', views.add_wishlist, name='add_wishlist'),
    path('view_log', views.view_log, name='view_log'),
]
