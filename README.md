# Office Employee Management System

A Django web application for managing employee information in an office environment. This system allows administrators to add, view, filter, and remove employee records with support for departments and roles.

## Features

- **Employee Management**
  - Add new employees with detailed information
  - View all employees in the system
  - Remove employees from the database
  - Track hire dates automatically

- **Employee Filtering**
  - Search employees by name (first or last name)
  - Filter by department
  - Filter by role
  - Combine multiple filters for advanced search

- **Data Management**
  - Manage departments and locations
  - Organize roles
  - Track salary and bonus information
  - Store contact information (phone numbers)

- **Admin Dashboard**
  - Access Django admin panel for direct database management
  - Manage all models (Employees, Departments, Roles)

## Project Structure

```
office_emp_app/
├── emp_app/                      # Main project configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing configuration
│   ├── wsgi.py                  # WSGI application
│   └── asgi.py                  # ASGI application
├── employee/                    # Employee management app
│   ├── models.py               # Database models (Employee, Department, Roles)
│   ├── views.py                # View functions for handling requests
│   ├── admin.py                # Django admin configuration
│   ├── migrations/             # Database migration files
│   └── templates/
│       └── employee/           # HTML templates
│           ├── index.html      # Home page
│           ├── view_emp.html   # Employee list view
│           ├── add_emp.html    # Add employee form
│           ├── remove_emp.html # Remove employee page
│           └── filter_emp.html # Employee filter page
├── manage.py                   # Django management script
└── db.sqlite3                  # SQLite database
```

## Database Models

### Employee
- `first_name` - Employee's first name
- `last_name` - Employee's last name
- `dept` - Foreign key to Department
- `role` - Foreign key to Roles
- `salary` - Annual salary (integer)
- `bonus` - Bonus amount (integer)
- `phone` - Contact phone number
- `hire_date` - Date employee was hired

### Department
- `name` - Department name
- `location` - Department location

### Roles
- `name` - Job role/title

## URL Routes

| Route | Description |
|-------|-------------|
| `/` | Home page |
| `/view_emp/` | View all employees |
| `/add_emp/` | Add new employee form and processing |
| `/remove_emp/` | Remove employee page |
| `/remove_emp/<emp_id>` | Remove specific employee by ID |
| `/filter_emp/` | Filter employees by criteria |
| `/admin/` | Django admin panel |

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd office_emp_app
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install django
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for admin access:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Application: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Usage

### Adding an Employee
1. Navigate to `/add_emp/`
2. Fill in the employee details:
   - First and last name
   - Select department
   - Select role
   - Enter salary and bonus
   - Enter phone number
3. Submit the form
4. The employee will be added to the system

### Viewing Employees
1. Go to `/view_emp/` to see all employees
2. View complete employee information including contact details and salary

### Filtering Employees
1. Navigate to `/filter_emp/`
2. Use search criteria:
   - Search by employee name (partial matching supported)
   - Filter by department
   - Filter by role
3. Click filter to see matching results

### Removing Employees
1. Navigate to `/remove_emp/`
2. Select an employee to remove or provide the employee ID
3. Confirm removal

## Technologies Used

- **Django 6.0** - Web framework
- **Python 3.x** - Programming language
- **SQLite** - Database (default)
- **HTML/CSS** - Frontend templates

## Configuration

The project uses Django's default configuration with SQLite database. Key settings are in [emp_app/settings.py](emp_app/settings.py):

- `DEBUG = True` - Development mode enabled
- `ALLOWED_HOSTS = []` - Configure for production use
- Database: SQLite (`db.sqlite3`)

### Important Security Notes

⚠️ **Development Only**: This project contains default development settings. Before deploying to production:
- Change `SECRET_KEY` to a secure random value
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS` properly
- Use a production database (PostgreSQL, MySQL, etc.)
- Configure proper security settings

## API Endpoints

All endpoints use standard HTTP methods (GET, POST):

- **GET** `/view_emp/` - Display all employees
- **GET/POST** `/add_emp/` - Display form or add employee
- **GET** `/remove_emp/` - Display removal page
- **POST** `/remove_emp/<emp_id>` - Remove employee
- **GET/POST** `/filter_emp/` - Filter employees

## Testing

To test the application:

1. Create test data through the admin panel or add_emp endpoint
2. Verify all CRUD operations work correctly
3. Test filtering functionality with various combinations

## Future Enhancements

- User authentication and authorization
- Employee profile pictures
- Performance reviews module
- Attendance tracking
- Search pagination
- Export employee data to CSV/Excel
- Email notifications
- API endpoints for mobile apps

## Troubleshooting

### Issue: "No such table" error
**Solution:** Run migrations
```bash
python manage.py migrate
```

### Issue: Admin panel not working
**Solution:** Create a superuser
```bash
python manage.py createsuperuser
```

### Issue: Department or Roles not showing
**Solution:** Add data through Django admin panel at `/admin/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is provided as-is for educational and organizational purposes.

## Support

For issues, questions, or suggestions, please refer to the Django documentation at https://docs.djangoproject.com/

## Author

Django Employee Management Application

---

**Last Updated:** February 2026
