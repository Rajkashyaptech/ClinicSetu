from django.urls import path
from .views import (
    doctor_queue,
    consultation_detail,
    complete_consultation,
    consultation_history,
    consultation_view,
    consultation_pdf,
    consultation_session_pdf,  # ✅ ADD THIS
)

urlpatterns = [
    path("doctor/", doctor_queue, name="doctor_queue"),

    path(
        "consult/<int:session_id>/",
        consultation_detail,
        name="consultation_detail"
    ),

    path(
        "consult/<int:session_id>/complete/",
        complete_consultation,
        name="complete_consultation"
    ),

    path(
        "history/",
        consultation_history,
        name="consultation_history"
    ),

    path(
        "history/<int:visit_id>/",
        consultation_view,
        name="consultation_view"
    ),

    # VISIT-LEVEL PDF (all sessions)
    path(
        "history/<int:visit_id>/pdf/",
        consultation_pdf,
        name="consultation_pdf"
    ),

    # SESSION-LEVEL PDF (single consultation)
    path(
        "session/<int:session_id>/pdf/",
        consultation_session_pdf,
        name="consultation_session_pdf"
    ),
]
