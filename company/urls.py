from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name ='companyHome'),
    path('manage', HomePageView.as_view(), name='home'),

    path('manage/product/', ProductView.as_view(), name='product'),
    path('manage/product/new', ProductCreateView.as_view(), name="product-create"),
    path('manage/product/<int:pk>/delete/', ProductDeleteView.as_view(), name="product-delete"),

    path('manage/classification', ClassificationListView.as_view(), name="classification"),
    path('manage/classification/new', ClassificationCreateView.as_view(), name="classification-create"),
    path('manage/classification/<int:pk>/delete/', ClassificationDeleteView.as_view(), name="classification-delete"),

    path('manage/city', CityListView.as_view(), name="city"),
    path('manage/city/new', CityCreateView.as_view(), name="city-create"),
    path('manage/city/<int:pk>/delete/', CityDeleteView.as_view(), name="city-delete"),

    path('manage/inventory', InventoryListView.as_view(), name="inventory"),
    path('manage/inventory/new', InventoryCreateView.as_view(), name="inventory-create"),
    path('manage/inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name="inventory-delete"),

    path('manage/inventoryProduct', InventoryProductListView.as_view(), name="inventoryProduct"),
    path('manage/inventoryProduct/new', InventoryProductCreateView.as_view(), name="inventoryProduct-create"),
    path('manage/inventoryProduct/<int:pk>/delete/', InventoryProductDeleteView.as_view(), name="inventoryProduct-delete"),

    path('manage/order', OrderListView.as_view(), name="order"),
    path('manage/order/<int:pk>/update/', OrderUpdateView.as_view(), name="order_update"),
    path('manage/order/<int:pk>/delete/', OrderDeleteView.as_view(), name="order_delete"),

    path('', UserProductListView.as_view(), name='adminpannel'),
    path('userOrder/<int:pk>', userOrderSubmitView, name="userOrder"),
    path('orderList', UserOrderListView.as_view(), name='orderList'),

    path('manage', HomeView.as_view(), name='admin'),

    path('shop/', ShopView.as_view(), name ='shop'),
    path('shop/AjilMakhloot/', AjilMakhlootView.as_view(), name='ajilMakhloot'),
    
    path('career/',CareerView.as_view(),name='career'),

    path('career/offer', OfferListView.as_view(), name='offer'),
    path('career/offer/new/', OfferCreateView.as_view(), name='offer_new'),
    path('career/offer/<int:pk>/', OfferDetailView.as_view(), name='offer_detail'),
    path('career/offer/<int:pk>/edit/', OfferUpdateView.as_view(), name='offer_edit'), 
    path('career/offer/<int:pk>/delete/', OfferDeleteView.as_view(), name='offer_delete'),

    path('about-us/', AboutUsView.as_view(), name ='about-us'),

    path('contact-us', ContactUsView.as_view(), name ='contact-us'),
]