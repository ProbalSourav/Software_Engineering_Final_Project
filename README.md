# 🏥 Hospital Management System — Team Vitality

📋 **Overview**  
The Hospital Management System (HMS) is a user-friendly, efficient, and secure solution designed to simplify and streamline the administrative and clinical processes of healthcare facilities. This system integrates essential hospital functions, reducing manual work and enhancing patient care.

---

📑 **Table of Contents**  
✨ Features  
💡 Benefits  
📂 Project Structure  
🚀 Getting Started  
🔧 Usage  
🤝 Contribution  
📄 License  
🙌 Acknowledgments  
📞 Contact  

---

✨ **Features**

🏥 **Patient Panel**  
- Register and submit symptoms  
- View appointment status and billing details  
- Access discharge information and medical history  

👨‍⚕️ **Doctor Panel**  
- Register and await admin approval  
- View and manage appointments  
- Access records of assigned patients  

🛡️ **Admin Panel**  
- Approve or decline patient and doctor registrations  
- Manage appointments and discharge patients  
- Generate and download bills  
- Monitor hospital activity with summaries and reports  

📅 **Appointment Scheduling**  
- Patients book appointments  
- Doctors approve or decline requests  
- Admin oversees scheduling and conflict resolution  

💳 **Billing System**  
- Admins generate bills with room, doctor, and medicine charges  
- Patients view and download bills (CSV or PDF)  

📤 **Discharge Workflow**  
- Admins discharge patients and record discharge details  

📊 **Reporting & Monitoring**  
- Admin dashboard with key metrics  
- Appointment and billing summaries  

---

💡 **Benefits**

⚡ Efficiency Boost: Automates routine tasks, freeing up staff for critical responsibilities  
📋 Accurate Documentation: Minimizes errors in patient data, billing, and scheduling  
❤️ Enhanced Patient Care: Provides immediate access to detailed patient records  
✅ Regulatory Compliance: Aligns with healthcare industry standards  
🔐 Data Security: Role-based access and encrypted data handling  

---

📂 **Project Structure**

```
Hospital-Management-System/ 
├── accounts/            # Handles user registration and role-based access
├── patients/            # Manages patient profiles and symptoms
├── doctors/             # Manages doctor profiles and appointments
├── appointments/        # Handles appointment scheduling and status
├── billing/             # Generates and tracks hospital bills
├── adminpanel/          # Admin dashboard and approval workflows
├── templates/           # HTML templates (optional)
├── static/              # CSS, JS, and images (optional)
├── db.sqlite3           # Database
├── manage.py            # Django project runner
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

---

🚀 **Getting Started**

### Prerequisites
- Python 3.10+  
- Django Framework  

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/hospital-management-system.git  
cd hospital-management-system  
```

2. **Virtual Environment Setup**
```bash
python -m venv venv  
venv\Scripts\activate  # On Windows  
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt  
```

4. **Set Up the Database**
```bash
python manage.py makemigrations  
python manage.py migrate  
```

5. **Create Superuser**
```bash
python manage.py createsuperuser  
```

6. **Run the Development Server**
```bash
python manage.py runserver  
```

Access the system at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

🔧 **Usage**

- Log in as an administrator to manage hospital operations  
- Register patients and doctors, approve requests  
- Schedule and manage appointments  
- Generate bills and discharge patients  
- Patients and doctors access their respective dashboards  

---

🤝 **Contribution**

We welcome contributions to improve this system. To contribute:

1. Fork the repository  
2. Create a new branch for your feature or bug fix  
3. Commit your changes  
4. Create a pull request  

---

📄 **License**

This project is licensed under the MIT License.  
If you use or distribute this project, please credit the original authors:

- **Project Name**: Hospital Management System  
- **Original Authors**: Team Vitality — Soumen Dhar, Probal Nath, Ashiqur Rahman  

See the LICENSE file for detailed terms.

---

🙌 **Acknowledgments**

Thanks to our team for their dedication to this project:  
- Probal Nath (C223077)  
- Soumen Dhar (C223068)
- Ashiqur Rahman (C223049)  

Special appreciation to healthcare professionals for their insights and feedback.  
Presented on: 19.06.2025

---

📞 **Contact**

For queries or collaboration:  
📧 probalnath50@gmail.com  
🌐 GitHub: [ProbalSourav](https://github.com/ProbalSourav)

---
