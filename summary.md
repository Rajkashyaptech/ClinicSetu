# ClinicSetu Project Summary

## Project Overview

ClinicSetu is a comprehensive Django-based clinic management system designed to streamline operations in a hospital or clinic environment. It supports multiple user roles including hospital administrators, doctors, receptionists, and medical staff, enabling efficient management of patient visits, consultations, prescriptions, and pharmacy dispensing. The system incorporates role-based access control, audit logging, and REST API endpoints for integration.

### Key Features
- **User Authentication and Role-Based Access**: Secure login with different roles (Super Admin, Hospital Admin, Doctor, Receptionist, Medical Staff).
- **Patient Management**: Store and manage patient records including demographics and contact information.
- **Visit Tracking**: Create patient visits with vital signs recording and doctor assignment.
- **Consultation Management**: Doctors can view queues, conduct consultations, and manage prescription items.
- **Prescription System**: Create and manage prescriptions with medicine items, dosages, and durations.
- **Pharmacy Operations**: Track prescription printing and dispensing status.
- **Audit Logging**: Maintain logs of system activities.
- **REST API**: Programmatic access to core functionalities.
- **Responsive Web Interface**: User-friendly dashboards for each role.

## Project Structure

```
clinicsetu/
├── manage.py                          # Django management script
├── db.sqlite3                          # SQLite database file
├── README.md                           # Project documentation
├── summary.md                          # This summary file
├── apps/                               # Custom Django applications
│   ├── __init__.py
│   ├── accounts/                       # User management and authentication
│   │   ├── __init__.py
│   │   ├── admin.py                    # Django admin configuration
│   │   ├── apps.py                     # App configuration
│   │   ├── models.py                   # User model with roles
│   │   ├── tests.py                    # Unit tests
│   │   ├── urls.py                     # URL patterns
│   │   ├── views.py                    # Login, logout, dashboards
│   │   ├── __pycache__/
│   │   ├── api/                        # REST API for accounts
│   │   │   ├── __init__.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   └── services/                   # Business logic services
│   │       ├── __init__.py
│   │       └── staff_manager.py       # Staff management functions
│   ├── hospitals/                      # Hospital entities
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # Hospital model with limits
│   │   ├── tests.py
│   │   ├── views.py                    # (Empty)
│   │   ├── __pycache__/
│   │   └── migrations/                 # Database migrations
│   ├── patients/                       # Patient records
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # Patient model
│   │   ├── tests.py
│   │   ├── views.py                    # (Empty)
│   │   ├── __pycache__/
│   │   ├── api/                        # REST API for patients
│   │   │   ├── __init__.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   └── migrations/
│   ├── visits/                         # Patient visits
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # Visit and PatientVitals models
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py                    # Create visit, receptionist dashboard
│   │   ├── __pycache__/
│   │   ├── management/                 # Django management commands
│   │   │   ├── __init__.py
│   │   │   └── commands/
│   │   ├── migrations/
│   │   └── services/                   # Visit creation services
│   │       ├── __init__.py
│   │       └── visit_creator.py       # Service to create visits
│   ├── consultations/                  # Doctor consultations
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # ConsultationSession model
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py                    # Doctor queue, consultation details
│   │   ├── __pycache__/
│   │   ├── api/                        # REST API for consultations
│   │   │   ├── __init__.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   └── services/                   # Queue and session management
│   │       ├── __init__.py
│   │       ├── doctor_queue.py
│   │       ├── followup_creator.py
│   │       ├── history.py
│   │       ├── history_permissions.py
│   │       ├── patient_history.py
│   │       └── session_closer.py
│   ├── prescriptions/                  # Prescription management
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # Prescription and PrescriptionItem
│   │   ├── tests.py
│   │   ├── views.py                    # Add medicine view
│   │   ├── __pycache__/
│   │   ├── api/                        # REST API for prescriptions
│   │   │   ├── __init__.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   └── services/                   # Item management services
│   │       ├── __init__.py
│   │       ├── item_adder.py
│   │       ├── item_remover.py
│   │       ├── item_stopper.py
│   │       ├── pdf_context_builder.py
│   │       ├── pdf_generator.py
│   │       ├── prescription_creator.py
│   │       └── prescription_reader.py
│   ├── pharmacy/                       # Pharmacy operations
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # DispenseRecord model
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py                    # Dashboard, mark printed/dispensed
│   │   ├── __pycache__/
│   │   ├── api/                        # REST API for pharmacy
│   │   │   ├── __init__.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   └── services/                   # Printing and dispensing services
│   │       ├── __init__.py
│   │       ├── dispense_initializer.py
│   │       ├── dispense_marker.py
│   │       ├── pharmacy_queue.py
│   │       └── print_marker.py
│   ├── audit/                          # Audit logging
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # AuditLog model
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py                    # Audit log view
│   │   ├── __pycache__/
│   │   └── services/                   # Logging services
│   │       ├── __init__.py
│   │       └── logger.py
│   ├── discovery/                      # Demo/discovery features
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                   # (Empty)
│   │   ├── tests.py
│   │   ├── views.py                    # (Empty)
│   │   ├── __pycache__/
│   │   └── migrations/
│   └── medicines/                      # Medicine catalog
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py                   # Medicine model
│       ├── tests.py
│       ├── views.py                    # (Empty)
│       ├── __pycache__/
│       ├── api/                        # REST API for medicines
│       │   ├── __init__.py
│       │   ├── urls.py
│       │   ├── views.py
│       └── services/                   # Medicine learning services
│           ├── __init__.py
│           └── learner.py
├── common/                             # Shared utilities
│   ├── __init__.py
│   ├── api_permissions.py              # API permission classes
│   ├── constants.py                    # User roles and constants
│   ├── mixins.py                       # Reusable mixins
│   ├── permissions.py                  # Role-based permissions
│   ├── __pycache__/
├── config/                             # Django settings and configuration
│   ├── __init__.py
│   ├── asgi.py                         # ASGI configuration
│   ├── urls.py                         # Main URL configuration
│   ├── wsgi.py                         # WSGI configuration
│   ├── __pycache__/
│   └── settings/                       # Settings files
│       ├── __init__.py
│       ├── base.py                     # Base settings
│       ├── local.py                    # Local development settings
│       ├── production.py               # Production settings
│       └── __pycache__/
├── media/                              # User-uploaded files
│   └── hospital_logos/                 # Hospital logo images
├── requirements/                       # Python dependencies
│   ├── base.txt                        # Base requirements
│   ├── local.txt                       # Local development requirements
│   └── production.txt                  # Production requirements
├── static/                             # Static files (CSS, JS, images)
│   ├── css/
│   ├── images/
│   └── js/
└── templates/                          # HTML templates
    ├── audit/
    │   └── audit_log_list.html
    ├── base/
    │   ├── base.html
    │   ├── messages.html
    │   └── navbar.html
    │   └── sidebar/
    ├── doctor/
    │   ├── consultation.html
    │   └── queue.html
    ├── history/
    │   ├── consultation_list.html
    │   └── consultation_view.html
    ├── hospital_admin/
    │   └── staff_dashboard.html
    ├── pdfs/
    ├── pharmacy/
    ├── receptionist/
    │   └── registration/
    └── templates/
```

## Apps Details

### accounts

**Purpose**: User management and authentication.

#### models.py
- **User** (extends AbstractUser): Custom user model with role field (super_admin, hospital_admin, doctor, receptionist, medical_staff), hospital foreign key, is_active boolean.
  - Methods: `is_super_admin()`, `is_doctor()`, `__str__()`

#### views.py
- `login_view(request)`: Handles user login with POST authentication.
- `logout_view(request)`: Logs out the user.
- `home_redirect(request)`: Redirects users to role-specific dashboards based on their role.
- `hospital_admin_dashboard(request)`: Renders hospital admin dashboard.

#### api/views.py
- **DoctorListAPI**: GET endpoint to list active doctors for a hospital.
- **StaffListAPI**: GET endpoint for hospital admin to view staff limits and usage.
- **CreateStaffAPI**: POST endpoint to create new staff users.
- **UpdateStaffAPI**: POST endpoint to update staff username/password.
- **UpdateStaffStatusAPI**: POST endpoint to activate/deactivate staff.

#### services/staff_manager.py
- `_active_count(hospital, role)`: Counts active users for a role in a hospital.
- `can_create_staff(hospital, role)`: Checks if staff limit allows creation.
- `create_staff_user(hospital, username, password, role)`: Creates staff user with validation.
- `set_staff_status(user, hospital, is_active)`: Updates user active status.
- `update_staff_details(user, hospital, username, password)`: Updates user details.

### hospitals

**Purpose**: Hospital entities and SaaS limits.

#### models.py
- **Hospital**: Model with name, is_active, SaaS limits (max_doctors, max_receptionists, max_medical_staff), branding fields (address, phone, footer_note, logo).
  - Methods: `__str__()`

#### views.py
- (Empty)

### patients

**Purpose**: Patient records management.

#### models.py
- **Patient**: Model with hospital FK, full_name, age, gender, phone_number, address.
  - Methods: `__str__()`

#### views.py
- (Empty)

#### api/views.py
- **PatientLookupAPI**: GET endpoint to lookup patients by phone number.
- **PatientCreateOrGetAPI**: POST endpoint to create new patient or get existing by phone.

#### api/serializers.py
- **PatientSerializer**: Serializes patient fields (id, full_name, age, gender, phone_number, address).

### visits

**Purpose**: Patient visits and vital signs tracking.

#### models.py
- **Visit**: Model with hospital, patient, doctor FKs, created_at, validity_days, is_active, closed_at.
  - Methods: `validity_end_date()`, `is_expired()`, `close()`
- **PatientVitals**: Model with visit FK, height_cm, weight_kg, blood_pressure, pulse_rate, temperature_c, recorded_at.
  - Methods: `__str__()`

#### views.py
- `create_visit(request)`: POST view to create visit with vitals.
- `receptionist_dashboard(request)`: Renders receptionist dashboard.

#### services/visit_creator.py
- `create_visit_with_vitals(hospital, patient, doctor, vitals_data)`: Creates visit or followup session with vitals recording.

### consultations

**Purpose**: Doctor consultations and session management.

#### models.py
- **ConsultationSession**: Model with visit, doctor FKs, session_number, status (open/completed), started_at, completed_at.
  - Meta: unique_together (visit, session_number), ordering.
  - Methods: `__str__()`

#### views.py
- `doctor_queue(request)`: Displays doctor's consultation queue.
- `consultation_detail(request, session_id)`: Shows consultation details with prescription items.
- `complete_consultation(request, session_id)`: Completes a consultation session.
- `consultation_history(request)`: Lists consultation history.
- `consultation_view(request, visit_id)`: Views detailed consultation.
- `consultation_pdf(request, visit_id)`: Generates PDF for full consultation.
- `consultation_session_pdf(request, session_id)`: Generates PDF for single session.

#### services/
- **doctor_queue.py**: `get_doctor_queue(doctor)` - Gets open sessions for doctor.
- **followup_creator.py**: `create_followup_session(visit)` - Creates new session for existing visit.
- **session_closer.py**: `complete_session(session)`, `create_new_session(visit, doctor)` - Session management.
- **patient_history.py**: `get_recent_visit_history(patient, exclude_visit, limit)` - Gets patient history.
- **history.py**: `get_consultation_history(user)` - Gets consultation history with permissions.
- **history_permissions.py**: `can_access_visit(user, visit)` - Permission checks for history access.

### prescriptions

**Purpose**: Prescription and medicine item management.

#### models.py
- **Prescription**: Model with visit FK, created_at.
  - Methods: `__str__()`
- **PrescriptionItem**: Model with prescription, session FKs, medicine details, status (active/stopped), created_at, is_active.
  - Meta: ordering.

#### views.py
- `add_medicine(request, prescription_id)`: POST view to add medicine to prescription.

#### api/views.py
- **AddMedicineAPI**: POST endpoint to add medicine via API.
- **RemoveMedicineAPI**: POST endpoint to remove medicine.
- **ActivePrescriptionItemsAPI**: GET endpoint to list active items.

#### services/
- **item_adder.py**: `add_prescription_item(prescription, session, medicine_name, dosage, frequency, duration)` - Adds medicine item.
- **prescription_creator.py**: `get_or_create_prescription(visit, session)` - Gets or creates prescription.
- **pdf_context_builder.py**: `build_consultation_pdf_context(visit)`, `build_session_pdf_context(session)` - Builds PDF data.
- **pdf_generator.py**: Generates PDFs (not detailed in read).
- **item_remover.py**, **item_stopper.py**, **prescription_reader.py**: Additional item management.

### pharmacy

**Purpose**: Pharmacy operations for prescription dispensing.

#### models.py
- **DispenseRecord**: Model with prescription FK, is_printed, printed_at, is_dispensed, dispensed_at, created_at.
  - Methods: `__str__()`

#### views.py
- `mark_printed(request, record_id)`: Marks prescription as printed.
- `mark_dispensed(request, record_id)`: Marks as dispensed.
- `pharmacy_dashboard(request)`: Renders pharmacy dashboard.
- `prescription_detail(request, prescription_id)`: Shows prescription details for dispensing.

#### services/
- **dispense_initializer.py**: `get_or_create_dispense_record(prescription)` - Initializes dispense record.
- **print_marker.py**: `mark_as_printed(dispense_record)` - Marks as printed.
- **dispense_marker.py**: `mark_as_dispensed(dispense_record)` - Marks as dispensed.
- **pharmacy_queue.py**: Queue management (not detailed).

### audit

**Purpose**: Audit logging of system activities.

#### models.py
- **AuditLog**: Model with actor FK, action, entity, entity_id, metadata (JSON), created_at.
  - Methods: `__str__()`

#### views.py
- `audit_log_view(request)`: Displays audit logs for super/hospital admins.

#### services/logger.py
- `log_action(actor, action, entity, entity_id, metadata)`: Logs actions to audit log.

### discovery

**Purpose**: Demo/discovery features (currently empty).

#### models.py
- (Empty)

#### views.py
- (Empty)

### medicines

**Purpose**: Medicine catalog learning.

#### models.py
- **Medicine**: Model with name (unique), created_at.
  - Methods: `save()` (normalizes name), `__str__()`
  - Meta: ordering.

#### views.py
- (Empty)

#### services/learner.py
- `learn_medicine(name)`: Stores medicine name if not exists.

## Common

### constants.py
- **UserRole**: Class with role constants and CHOICES.

### permissions.py
- `role_required(*allowed_roles)`: Decorator for view role restrictions.

### api_permissions.py
- **IsRole**: Base permission class for roles.
- **IsHospitalAdmin**, **IsReceptionist**, **IsDoctor**, **IsMedicalStaff**: Specific role permissions.

### mixins.py
- (Empty)

## Config

### settings/base.py
- Base Django settings with SECRET_KEY, DEBUG, ALLOWED_HOSTS, etc.

### urls.py
- Main URL configuration including app URLs and API endpoints.

## Templates

HTML templates organized by feature:
- base/: Base templates (base.html, navbar.html, sidebar/)
- doctor/: Doctor-specific (consultation.html, queue.html)
- receptionist/: Receptionist views
- pharmacy/: Pharmacy views
- audit/: Audit log
- history/: Consultation history
- hospital_admin/: Admin dashboard
- pdfs/: PDF templates

## Requirements

- base.txt: Core dependencies (Django, djangorestframework, etc.)
- local.txt: Development dependencies
- production.txt: Production dependencies

## Database

- Uses SQLite (db.sqlite3) for simplicity.
- Migrations in each app's migrations/ directory.

This summary provides a comprehensive overview of the ClinicSetu Django project structure, models, views, services, and key functionalities.