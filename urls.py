from django.urls import path
from . import views

urlpatterns = [

    # =====================================
    # Dashboard
    # =====================================
    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    # =====================================
    # Dataset Information
    # =====================================
    path(
        'dataset/',
        views.dataset_info,
        name='dataset_info'
    ),

    # =====================================
    # Data Cleaning
    # =====================================
    path(
        'cleaning/',
        views.data_cleaning,
        name='data_cleaning'
    ),

    # =====================================
    # Data Visualization
    # =====================================
    path(
        'visualization/',
        views.data_visualization,
        name='data_visualization'
    ),

    # =====================================
    # Train Machine Learning Model
    # =====================================
    path(
        'train-model/',
        views.train_model_view,
        name='train_model'
    ),

    # =====================================
    # Predict Student Performance
    # =====================================
    path(
        'predict/',
        views.predict_student,
        name='predict_student'
    ),

    # =====================================
    # Reports
    # =====================================
    path(
        'reports/',
        views.reports_view,
        name='reports'
    ),

]