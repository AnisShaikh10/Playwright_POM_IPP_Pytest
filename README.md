# Playwright_POM_IPP_Pytest

Python-based end-to-end test automation framework using **Playwright**, **Pytest**, and **Page Object Model (POM)** design pattern.

This project demonstrates how to structure UI automation tests for web applications with readable, maintainable code and scalable architecture.

---

## 🧠 Features

- 📦 Python test automation using Playwright + Pytest  
- 🗂 Page Object Model (POM) for clean and reusable UI interactions  
- 📋 Configured with `pytest.ini` for custom test settings  
- ⛓ Support for browser fixtures via Playwright  
- ⚡ Parallel test execution with pytest-xdist (optional)  
- 🧪 Reports and data files included (like `data.txt`)

---

## 📁 Project Structure
📦Playwright_POM_IPP_Pytest
┣ 📂pages/ # Page object modules
┣ 📂tests/ # Test case modules
┣ 📂utils/ # Helper utilities and functions
┣ 📜conftest.py # Pytest fixtures & setup hooks
┣ 📜pytest.ini # Pytest configuration
┣ 📜requirements.txt # Python dependencies
┣ 📜data.txt # Test data
┗ 📜.gitignore