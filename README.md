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

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd clinicsetu
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements/local.txt
   ```

4. **Environment Setup**:
   - Copy `.env.example` to `.env` and configure environment variables (e.g., SECRET_KEY).
   - Example `.env`:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3
     ```

5. **Database Setup**:
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:8000`
   - Login with the superuser credentials

## Usage

### User Roles and Workflows

1. **Super Admin**:
   - Manage hospitals and their limits
   - Access audit logs

2. **Hospital Admin**:
   - Manage staff (doctors, receptionists, medical staff)
   - View hospital-specific audit logs

3. **Receptionist**:
   - Register new patients
   - Create patient visits
   - Record vital signs

4. **Doctor**:
   - View consultation queue
   - Conduct consultations
   - Add prescription items
   - View patient history

5. **Medical Staff**:
   - Manage pharmacy operations
   - Mark prescriptions as printed/dispensed

### Key URLs

- `/` - Home (redirects based on role)
- `/admin/` - Django Admin
- `/accounts/login/` - Login page
- `/visits/` - Visit management
- `/consultations/` - Doctor consultations
- `/pharmacy/` - Pharmacy operations
- `/audit/` - Audit logs

## Project Structure

```
clinicsetu/
├── manage.py                          # Django management script
├── db.sqlite3                          # SQLite database file
├── apps/                               # Custom Django applications
│   ├── accounts/                       # User management and authentication
│   ├── hospitals/                      # Hospital entities
│   ├── patients/                       # Patient records
│   ├── visits/                         # Patient visits
│   ├── consultations/                  # Doctor consultations
│   ├── prescriptions/                  # Prescription management
│   ├── pharmacy/                       # Pharmacy operations
│   ├── audit/                          # Audit logging
│   ├── discovery/                      # Demo/discovery features
│   └── medicines/                      # Medicine catalog
├── common/                             # Shared utilities
├── config/                             # Django settings and configuration
├── media/                              # User-uploaded files
├── requirements/                       # Python dependencies
├── static/                             # Static files (CSS, JS, images)
└── templates/                          # HTML templates
```

## API Documentation

ClinicSetu provides REST API endpoints for programmatic access:

### Authentication
All API endpoints require authentication. Use session-based authentication or token authentication.

### Endpoints

#### Accounts API (`/api/v1/accounts/`)
- `GET /api/v1/accounts/doctors/` - List doctors
- `GET /api/v1/accounts/staff/` - List staff (Hospital Admin only)
- `POST /api/v1/accounts/staff/` - Create staff (Hospital Admin only)
- `POST /api/v1/accounts/staff/{id}/` - Update staff (Hospital Admin only)

#### Patients API (`/api/v1/patients/`)
- `GET /api/v1/patients/lookup/` - Lookup patients by phone
- `POST /api/v1/patients/create-or-get/` - Create or get patient

#### Prescriptions API (`/api/v1/prescriptions/`)
- `POST /api/v1/prescriptions/add-medicine/` - Add medicine to prescription
- `POST /api/v1/prescriptions/remove-medicine/` - Remove medicine
- `GET /api/v1/prescriptions/active-items/` - Get active prescription items

#### Pharmacy API (`/api/v1/pharmacy/`)
- Pharmacy operation endpoints

#### Medicines API (`/api/v1/medicines/`)
- Medicine catalog endpoints

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
- Follow PEP 8 guidelines
- Use Black for code formatting
- Use isort for import sorting

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Deployment

### Production Settings
- Use `config/settings/production.py`
- Set `DEBUG=False`
- Configure proper database (PostgreSQL recommended)
- Set up static file serving
- Configure HTTPS

### Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (False in production)
- `DATABASE_URL`: Database connection URL
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact the development team or create an issue in the repository.

## Changelog

### Version 1.0.0
- Initial release with core clinic management features
- Multi-role user system
- Patient, visit, consultation, and prescription management
- Pharmacy operations
- Audit logging
- REST API

---

ClinicSetu - Streamlining Clinic Operations