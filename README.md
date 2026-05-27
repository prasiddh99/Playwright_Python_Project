# Playwright Python Automation Framework

End-to-End Web Automation Framework developed using Playwright with Python, Pytest, and Page Object Model (POM) architecture.

This project automates major user workflows of an E-Commerce website including User Login, Product Browsing, Add To Cart, Checkout, and End-to-End Purchase Flow.

---

# Application Under Test

automationexercise E-Commerce Website

https://automationexercise.com/

---

# Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- HTML Reports (pytest-html)
- Git & GitHub

---

# Framework Features

- Page Object Model Design Pattern
- Reusable Base Utilities
- Explicit Waits
- Pytest Fixtures
- HTML Reporting
- Screenshot Capture on Failures
- Modular Framework Structure
- End-to-End Automation Testing

---

# Project Structure

```bash
Playwright_Framework/
│
├── pages/
│   ├── account_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── products_page.py
│
├── reports/
│   └── report.html
│
├── screenshots/
│
├── tests/
│   ├── test_Framework_e2e_checkout.py
│   └── test_Simple_e2e_checkout.py
│
├── utilities/
│   ├── base_page.py
│   ├── helpers.py
│   └── test_data.py
│
├── conftest.py
└── pytest.ini
```

---

# Key Automation Scenarios

- User Login Validation
- Product Browsing & Selection
- Add Products To Cart
- Checkout & Order Placement
- End-to-End Purchase Flow
- Screenshot Capture on Failure
- HTML Report Generation

---

# Reporting

HTML reports are generated automatically after execution.

```bash
reports/report.html
```

Screenshots are automatically captured on test failures.

```bash
screenshots/
```

---

# Installation

```bash
pip install playwright
pip install pytest
pip install pytest-html
```

Install Playwright browsers:

```bash
playwright install
```

OR

```bash
pip install -r requirements.txt
```

---

# Run Tests

## Run All Tests

```bash
pytest
```

## Run Specific Test File

```bash
pytest tests/test_Framework_e2e_checkout.py
```

## Run Tests in Parallel with HTML Report

```bash
pytest tests -n auto --browser_name=firefox -v --html=reports/report.html --self-contained-html
```

---

# Clone Repository

```bash
git clone https://github.com/prasiddh99/Playwright_Python_Project.git
```

---

# Future Improvements

- Jenkins CI/CD Integration
- Allure Reporting
- API + UI Hybrid Framework
- Data Driven Testing

---

# Author

Prasiddh Dharmnathi

GitHub:
https://github.com/prasiddh99
