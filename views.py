from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render

from .ml.predict import predict_student as predict_model
from .ml.train_model import train_model


# =====================================================
# Helper
# =====================================================

def load_dataset():
    csv_path = Path(__file__).resolve().parent / "ml" / "student-mat.csv"
    df = pd.read_csv(csv_path, sep=";")
    return csv_path, df


# =====================================================
# Dashboard
# =====================================================

def dashboard(request):

    csv_path, df = load_dataset()

    context = {
        "dataset_name": csv_path.name,
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "columns": df.columns.tolist(),
        "target_variable": "G3",
    }

    return render(request, "dashboard/dashboard.html", context)


# =====================================================
# Dataset Information
# =====================================================

def dataset_info(request):

    csv_path, df = load_dataset()

    context = {
        "dataset_name": csv_path.name,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "data_types": df.dtypes.items(),
        "preview": df.head(10).to_html(
            classes="table table-bordered table-striped table-hover",
            index=False
        ),
    }

    return render(request, "dataset/info.html", context)


# =====================================================
# Data Cleaning
# =====================================================

def data_cleaning(request):

    _, df = load_dataset()

    context = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().items(),
        "duplicate_rows": df.duplicated().sum(),
        "data_types": df.dtypes.items(),
        "summary": df.describe(include="all").to_html(
            classes="table table-bordered table-striped",
            border=0
        ),
    }

    return render(request, "analytics/cleaning.html", context)


# =====================================================
# Visualization
# =====================================================

def data_visualization(request):

    _, df = load_dataset()

    static_path = Path(__file__).resolve().parent / "static" / "images"
    static_path.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 4))
    plt.hist(df["G3"], bins=20)
    plt.title("G3 Distribution")
    plt.xlabel("Final Grade")
    plt.ylabel("Students")
    plt.tight_layout()
    plt.savefig(static_path / "g3_distribution.png")
    plt.close()

    plt.figure(figsize=(5, 5))
    df["sex"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%"
    )
    plt.ylabel("")
    plt.title("Gender Distribution")
    plt.tight_layout()
    plt.savefig(static_path / "gender_distribution.png")
    plt.close()

    return render(request, "analytics/visualization.html")


# =====================================================
# Train Model
# =====================================================

def train_model_view(request):

    result = None

    if request.method == "POST":

        try:
            result = train_model()

        except Exception as e:
            result = {
                "error": str(e)
            }

    return render(
        request,
        "ml/train_model.html",
        {
            "result": result
        }
    )


# =====================================================
# Prediction
# =====================================================

def predict_student(request):

    prediction = None

    if request.method == "POST":

        try:

            data = {
                "school": request.POST.get("school"),
                "sex": request.POST.get("sex"),
                "age": int(request.POST.get("age")),
                "studytime": int(request.POST.get("studytime")),
                "failures": int(request.POST.get("failures")),
                "absences": int(request.POST.get("absences")),
                "G1": int(request.POST.get("G1")),
                "G2": int(request.POST.get("G2")),
            }

            prediction = predict_model(data)

        except Exception as e:
            prediction = f"Error: {e}"

    return render(
        request,
        "prediction/predict.html",
        {
            "prediction": prediction
        }
    )


# =====================================================
# Reports
# =====================================================

def reports_view(request):

    metrics = None

    metrics_file = Path(__file__).resolve().parent / "ml" / "metrics.pkl"

    if metrics_file.exists():

        import joblib
        metrics = joblib.load(metrics_file)

    return render(
        request,
        "reports/reports.html",
        {
            "metrics": metrics
        }
    )