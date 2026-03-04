# 🚀 Playwright POM Automation Framework (Python)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-orange.svg)
![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-purple.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

------------------------------------------------------------------------

## 📌 Professional Summary

This project is a scalable **UI Test Automation Framework** built using
**Playwright (Python)** and **Pytest**, following the **Page Object
Model (POM)** design pattern.

It demonstrates:

-   Clean automation architecture
-   Separation of test logic and UI interactions
-   Reusable fixtures and utilities
-   Scalable test structure for enterprise applications
-   Support for parallel execution and reporting

This framework reflects real-world automation engineering practices used
in modern QA teams.

------------------------------------------------------------------------

# 🧠 Tech Stack

-   **Language:** Python
-   **Automation Tool:** Playwright
-   **Test Framework:** Pytest
-   **Design Pattern:** Page Object Model (POM)
-   **Reporting:** pytest-html (optional)
-   **Parallel Execution:** pytest-xdist

------------------------------------------------------------------------

## 📁 Project Architecture
```
Playwright_POM_IPP_Pytest/
│
├── pages/ # Page Object classes (UI actions)
├── tests/ # Test scenarios
├── utils/ # Reusable helpers
├── conftest.py # Shared fixtures (browser setup/teardown)
├── pytest.ini # Pytest configuration
├── requirements.txt # Dependencies
└── .gitignore
```

🔹 Architecture Flow:
Test File → Page Object → Playwright Actions → Browser

This structure ensures:

- High maintainability

- Low duplication

- Clear separation of concerns

- Easy debugging and scalability

------------------------------------------------------------------------

## 🎯 Project Purpose

This automation framework is currently implemented for:

**IPP Applicant Creation Workflow Automation**

The framework automates the end-to-end process of creating an IPP applicant through a web-based application, validating UI behavior, form submissions, and workflow transitions.

### 🔄 Framework Reusability

Although currently built for IPP Applicant creation, this framework is **application-agnostic** and can be easily extended to automate:

- Any web-based enterprise application  
- Form-driven workflows  
- Multi-step business processes  
- Role-based application flows  
- Regression and smoke test suites  

Because it follows the **Page Object Model (POM)** architecture and modular fixture design, new applications can be automated by simply:

- Creating new Page Object classes  
- Writing new test scenarios  
- Reusing existing framework utilities  

This makes the framework scalable, reusable, and production-ready.

------------------------------------------------------------------------

# 🚀 Getting Started

## 1️⃣ Clone Repository

git clone https://github.com/AnisShaikh10/Playwright_POM_IPP_Pytest.git
cd Playwright_POM_IPP_Pytest

## 2️⃣ Create Virtual Environment

python -m venv venv

Activate:

Windows: venv`Scripts`{=tex}`activate`{=tex}

Mac/Linux: source venv/bin/activate

## 3️⃣ Install Dependencies

pip install -r requirements.txt

## 4️⃣ Install Playwright Browsers

playwright install

------------------------------------------------------------------------

# 🧪 Test Execution

Run all tests: pytest

Run specific file: pytest tests/test_example.py

Verbose: pytest -v

Parallel: pytest -n auto

------------------------------------------------------------------------

# 📊 Reporting

pytest --html=report.html

------------------------------------------------------------------------

# 🎭 Page Object Model (POM)

-   Locators and UI actions are encapsulated in `pages/`
-   Tests remain clean and readable
-   Reduces duplication
-   Improves maintainability
-   Supports scalable test suites

------------------------------------------------------------------------

# 🛠 Key Capabilities

✔ Structured automation architecture\
✔ Fixture-based browser management\
✔ Parallel execution support\
✔ Report generation\
✔ Clean Git version control

------------------------------------------------------------------------

# 📌 Future Enhancements

-   GitHub Actions CI
-   Allure reporting
-   Environment-based configuration
-   Docker support
-   Cross-browser execution matrix

------------------------------------------------------------------------

# 👨‍💻 Author

**Anis Shaikh**\
Automation Engineer \| Python \| Playwright \| Pytest

------------------------------------------------------------------------

# 📬 Contributing
Contributions, suggestions, and improvements are welcome.

Feel free to open an issue or submit a pull request.