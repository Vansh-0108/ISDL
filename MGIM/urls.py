from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_gate_inventory_manager, name='main-gate-inventory-manager'),
    path('inventory/', views.inventory, name='MGIM-inventory'),
    path('entry-details/', views.entry_details, name='entry-details'),
    path('exit-details/', views.exit_details, name='exit-details'),
]
