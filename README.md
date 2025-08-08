# Selenium Test Automation - Insider QA Jobs

This project automates testing of Quality Assurance (QA) job listings on the [Insider](https://useinsider.com) website.  
It is developed using Python and Selenium WebDriver following the Page Object Model (POM) design pattern.

---

## 📋 Project Features

- Verify Insider homepage loads successfully
- Navigate from the "Company" menu to the "Careers" page
- Check visibility of Locations, Teams, and Life at Insider sections on Careers page
- Filter QA job listings by Location: Istanbul, Turkey and Department: Quality Assurance
- Validate that all filtered jobs match the criteria
- Click on the "View Role" button and verify navigation to Lever application form page
- Take screenshot on test failure
- Tests organized with unittest framework
- Fully compliant with POM principles

---

## 🛠 Setup & Running Tests

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rumeysaevcimen/Tester-Selenium-Project.git
   cd Tester-Selenium-Project

 2. **Create and activate a virtual environment:**

   **On Windows:**

      ```bash
         python -m venv venv
         .\venv\Scripts\activate

   **On Mac/Linux:**

         ```bash
         python3 -m venv venv
         source venv/bin/activate

  3. **Install dependencies:**

         ```bash
         pip install -r requirements.txt

   4. **Run the tests:**

         ```bash
         python -m unittest discover -s tests


## 📁 Project Structure 

Tester-Selenium-Project/
├── pages/
│   ├── base.py
│   ├── home.py
│   ├── career.py
│   └── qa_jobs.py
├── tests/
│   └── test.py
├── requirements.txt
├── README.md
└── .gitignore


## 📝 Test Scenario

- Open Insider homepage and verify the page title
- Navigate through the "Company" menu to the "Careers" page
- Verify that the Locations, Teams, and Life at Insider sections are visible
- Click the "See all QA jobs" button on the Quality Assurance careers page
- Apply filters: Department = "Quality Assurance" and Location = "Istanbul, Turkey"
- Verify that all listed jobs meet the filter criteria
- Click the first "View Role" button and confirm navigation to the Lever application page
- Capture a screenshot if any step fails

    
