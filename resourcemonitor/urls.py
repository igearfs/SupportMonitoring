# Import necessary Django modules
from django.urls import path  # Import path() function to define URL routes
from . import views  # Import views module to link views to URL routes

# Define URL patterns for the application
urlpatterns = [
    # The root URL pattern, maps to the dashboard view
    path('', views.dashboard, name='dashboard'),

    # The 'refresh' URL pattern, maps to the refresh_data view
    path('refresh/', views.refresh_data, name='refresh_data'),

    # The 'sftp-history' URL pattern, maps to the sftp_history_page view
    path("sftp-history/", views.sftp_history_page, name="sftp_history_page"),

    # The 'sftp-history-data' URL pattern, maps to the sftp_history_data view
    path("sftp-history-data/", views.sftp_history_data, name="sftp_history_data"),
]
