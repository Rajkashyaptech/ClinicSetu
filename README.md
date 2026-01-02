# ClinicSetu

## Overview

ClinicSetu is a comprehensive Django-based clinic management system designed to streamline operations in a hospital or clinic environment. It supports multiple user roles including hospital administrators, doctors, receptionists, and medical staff, enabling efficient management of patient visits, consultations, prescriptions, and pharmacy dispensing. The system incorporates role-based access control, audit logging, and REST API endpoints for integration.

## Features

- **User Authentication and Role-Based Access**: Secure login with different roles (Super Admin, Hospital Admin, Doctor, Receptionist, Medical Staff).
- **Patient Management**: Store and manage patient records including demographics and contact information.
- **Visit Tracking**: Create patient visits with vital signs recording and doctor assignment.
- **Consultation Management**: Doctors can view queues, conduct consultations, and manage prescription items.
- **Prescription System**: Create and manage prescriptions with medicine items, dosages, and durations.
- **Pharmacy Operations**: Track prescription printing and dispensing status.
- **Audit Logging**: Maintain logs of system activities.
- **REST API**: Programmatic access to core functionalities.
- **Responsive Web Interface**: User-friendly dashboards for each role.

## Installation

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd clinicsetu
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements/local.txt
   ```

3. **Environment Setup**:
   - Copy `.env.example` to `.env` and configure environment variables (e.g., SECRET_KEY).

4. **Database Setup**:
   ```
   python manage.py migrate
   ```

5. **Create Superuser**:
   ```
   python manage.py createsuperuser
   ```

6. **Run the Server**:
   ```
   python manage.py runserver
   ```

## Project Structure

```
clinicsetu/
├── manage.py                          # Django management script
├── config/                            # Django settings and configuration
│   ├── settings/
│   │   ├── base.py                    # Base settings with INSTALLED_APPS
│   │   ├── local.py                   # Local development settings
│   │   └── production.py              # Production settings
│   ├── urls.py                        # Main URL configuration
│   ├── wsgi.py                        # WSGI configuration
│   └── asgi.py                        # ASGI configuration
├── apps/                              # Custom Django applications
│   ├── accounts/                      # User management and authentication
│   │   ├── models.py                  # User model with roles
│   │   ├── views.py                   # Login, logout, dashboards
│   │   ├── services/staff_manager.py  # Staff management functions
│   │   └── api/views.py               # API endpoints for users
│   ├── hospitals/                     # Hospital entities
│   │   └── models.py                  # Hospital model with limits
│   ├── patients/                      # Patient records
│   │   └── models.py                  # Patient model
│   ├── visits/                        # Patient visits
│   │   ├── models.py                  # Visit and PatientVitals models
│   │   ├── views.py                   # Create visit, receptionist dashboard
│   │   └── services/visit_creator.py  # Service to create visits
│   ├── consultations/                 # Doctor consultations
│   │   ├── models.py                  # ConsultationSession model
│   │   ├── views.py                   # Doctor queue, consultation details
│   │   └── services/                  # Queue and session management
│   ├── prescriptions/                 # Prescription management
│   │   ├── models.py                  # Prescription and PrescriptionItem
│   │   ├── views.py                   # Add medicine view
│   │   ├── services/                  # Item management services
│   │   └── api/views.py               # API for prescription operations
│   ├── pharmacy/                      # Pharmacy operations
│   │   ├── models.py                  # DispenseRecord model
│   │   ├── views.py                   # Dashboard, mark printed/dispensed
│   │   └── services/                  # Printing and dispensing services
│   ├── audit/                         # Audit logging
│   └── discovery/                     # Demo/discovery features
├── common/                            # Shared utilities
│   ├── constants.py                   # User roles and constants
│   ├── permissions.py                 # Role-based permissions
│   ├── mixins.py                      # Reusable mixins
│   └── api_permissions.py             # API permission classes
├── templates/                         # HTML templates
│   ├── base/                          # Base templates
│   ├── dashboard/                     # Role-specific dashboards
│   └── ...                            # Other templates
├── requirements/                      # Python dependencies
│   ├── base.txt                       # Core dependencies
│   ├── local.txt                      # Local dev dependencies
│   └── production.txt                 # Production dependencies
└── db.sqlite3                         # SQLite database (default)
```

## Apps Description

### Accounts App
Handles user authentication, role management, and staff operations.

**Models:**
- `User`: Extends Django's `AbstractUser` with `role` (choices from `UserRole`), `hospital` (ForeignKey), and `is_active` fields. Methods include `is_super_admin()`, `is_doctor()`.

**Views:**
- `login_view(request)`: Authenticates users via POST, redirects to role-based dashboard on success.
- `logout_view(request)`: Logs out the user and redirects to login.
- `home_redirect(request)`: Redirects authenticated users to their role-specific dashboard (e.g., receptionist_dashboard for Receptionist).
- `hospital_admin_dashboard(request)`: Renders the hospital admin staff dashboard.

**Services (staff_manager.py):**
- `_active_count(hospital, role)`: Counts active staff of a role in a hospital.
- `can_create_staff(hospital, role)`: Checks if hospital can add more staff of the role (based on limits).
- `create_staff_user(hospital, username, password, role)`: Creates a new staff user.
- `set_staff_status(user, hospital, is_active)`: Activates/deactivates staff.
- `update_staff_details(user, hospital, username, password)`: Updates staff credentials.

**API (api/views.py):**
- GET endpoints for user lists and details.
- POST endpoints for creating and updating users.

### Hospitals App
Manages hospital information and SaaS limits.

**Models:**
- `Hospital`: Fields for `name`, `is_active`, staff limits (`max_doctors`, `max_receptionists`, `max_medical_staff`).

### Patients App
Stores patient demographic and contact information.

**Models:**
- `Patient`: Linked to `Hospital`, includes `full_name`, `age`, `gender`, `phone_number`, `address`.

### Visits App
Manages patient visits and initial vital recordings.

**Models:**
- `Visit`: Links `hospital`, `patient`, `doctor`; tracks `validity_days`, `is_active`, `closed_at`. Methods: `validity_end_date()`, `is_expired()`, `close()`.
- `PatientVitals`: One-to-one with `Visit`; stores `height_cm`, `weight_kg`, `blood_pressure`, `pulse_rate`, `temperature_c`.

**Views:**
- `create_visit(request)`: POST creates a visit with vitals using `create_visit_with_vitals()` service.
- `receptionist_dashboard(request)`: Renders receptionist interface for creating visits.

**Services (visit_creator.py):**
- `create_visit_with_vitals(hospital, patient, doctor_id, vitals_data)`: Creates visit and associated vitals.

### Consultations App
Handles doctor consultation sessions.

**Models:**
- `ConsultationSession`: Linked to `Visit` and `Doctor`; fields for `session_number`, `status` (open/completed), timestamps.

**Views:**
- `doctor_queue(request)`: Retrieves and displays doctor's pending sessions using `get_doctor_queue()`.
- `consultation_detail(request, session_id)`: Shows session details, lazy-creates prescription, displays active items.
- `complete_consultation(request, session_id)`: Completes the session using `complete_session()` and redirects.
- `doctor_dashboard(request)`: Renders doctor's queue page.

**Services:**
- `doctor_queue.py`: `get_doctor_queue(user)`: Fetches open sessions for the doctor.
- `session_closer.py`: `complete_session(session)`: Marks session as completed and updates timestamp.

### Prescriptions App
Manages prescriptions and medicine items.

**Models:**
- `Prescription`: One-to-one with `Visit`.
- `PrescriptionItem`: Linked to `Prescription` and `ConsultationSession`; fields for medicine details, `status` (active/stopped).

**Views:**
- `add_medicine(request, prescription_id)`: POST adds item using `add_prescription_item()` service.

**Services:**
- `prescription_creator.py`: `get_or_create_prescription(visit, session)`: Creates prescription if not exists.
- `item_adder.py`: `add_prescription_item(prescription, session, medicine_name, dosage, frequency, duration)`: Adds medicine item.
- `item_stopper.py`: `stop_prescription_item(prescription, session, medicine_name)`: Stops an item.
- `prescription_reader.py`: `get_active_items(prescription)`: Retrieves active prescription items.

**API (api/views.py):**
- POST endpoints for adding and stopping prescription items.
- GET endpoint for retrieving prescription details.

### Pharmacy App
Tracks prescription dispensing workflow.

**Models:**
- `DispenseRecord`: Linked to `Prescription`; tracks `is_printed`, `printed_at`, `is_dispensed`, `dispensed_at`.

**Views:**
- `pharmacy_dashboard(request)`: Renders pharmacy dashboard.
- `prescription_detail(request, prescription_id)`: Shows prescription details, creates dispense record if needed, checks if dispensable.
- `mark_printed(request, record_id)`: Marks record as printed using `mark_as_printed()`.
- `mark_dispensed(request, record_id)`: Marks as dispensed using `mark_as_dispensed()`.

**Services:**
- `print_marker.py`: `mark_as_printed(record)`: Updates print status and timestamp.
- `dispense_marker.py`: `mark_as_dispensed(record)`: Updates dispense status and timestamp.
- `dispense_initializer.py`: `get_or_create_dispense_record(prescription)`: Creates dispense record if not exists.

### Audit App
Handles system audit logging (details not specified in provided context).

### Discovery App
Contains demo or discovery features (details not specified).

### Common
Shared utilities across apps.

- `constants.py`: Defines `UserRole` choices (SUPER_ADMIN, HOSPITAL_ADMIN, DOCTOR, RECEPTIONIST, MEDICAL_STAFF).
- `permissions.py`: `role_required` decorator for view access control.
- `mixins.py`: Reusable Django mixins.
- `api_permissions.py`: Custom permission classes for API views.

## Flow of the Project

1. **Patient Registration and Visit Creation**: Receptionist logs in, creates a patient record if new, then creates a visit assigning a doctor and recording initial vitals.

2. **Doctor Consultation**: Doctor views their queue of pending visits. For each session, they can view patient details, vitals, and manage prescriptions by adding or stopping medicines.

3. **Prescription Management**: During consultation, doctors add prescription items. Prescriptions are created lazily on first access.

4. **Session Completion**: Doctor completes the consultation session, which may allow pharmacy dispensing.

5. **Pharmacy Operations**: Medical staff views prescriptions, prints labels (marking as printed), and dispenses medicines (marking as dispensed).

6. **Administrative Oversight**: Hospital admins manage staff, view dashboards, and ensure compliance with staff limits.

7. **Audit and Logging**: All actions are logged for compliance and tracking.

## Database

- **Default**: SQLite (`db.sqlite3`)
- **Models**: Relational structure with ForeignKey relationships linking hospitals, users, patients, visits, sessions, prescriptions, and dispense records.
- **Migrations**: Located in each app's `migrations/` directory.

## API

RESTful API endpoints provided in `api/views.py` of relevant apps (accounts, prescriptions). Uses Django REST Framework for serialization and authentication.

## Technologies Used

- **Backend**: Django 4.2, Django REST Framework
- **Database**: SQLite (configurable)
- **Frontend**: Django Templates, HTML/CSS
- **Authentication**: Django's built-in auth with custom User model
- **Permissions**: Custom decorators and permission classes

## Contributing

1. Follow Django best practices.
2. Use services for business logic.
3. Ensure role-based permissions.
4. Write tests in `tests.py`.
5. Run migrations for model changes.

## License

[Specify license if applicable]