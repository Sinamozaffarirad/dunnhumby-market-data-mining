# Directory Tree Structure

This is a comprehensive tree view of the Final Project directory structure.

```
Final Project/
│   └── settings.local.json
├── .dist/
├── DataBase Queries/
│   ├── create_user_7.27.2025.bak
│   └── SQLQuery1.sql
├── Dunhummy/
│   ├── campaign_desc.csv
│   ├── campaign_table.csv
│   ├── causal_data.csv
│   ├── coupon.csv
│   ├── coupon_redempt.csv
│   ├── hh_demographic.csv
│   ├── product.csv
│   └── transaction_data.csv
├── fonts/
│   ├── B Titr.ttf
│   ├── BNazanin.ttf
│   ├── BNaznnBd.ttf
│   ├── ScheherazadeNew-Bold.ttf
│   ├── Times new roman bold (2).ttf
│   ├── times new roman bold italic.ttf
│   ├── Times new roman bold.ttf
│   ├── Times New Roman CE Bold (2).ttf
│   ├── Times New Roman CE Bold.ttf
│   ├── Times New Roman CE Italic.ttf
│   ├── Times New Roman CE.ttf
│   ├── times new roman italic.ttf
│   └── times new roman.ttf
├── Website/
│   ├── .dist/
│   ├── market/
│   │   ├── catalog/
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   ├── admin.cpython-311.pyc
│   │   │   │   ├── apps.cpython-311.pyc
│   │   │   │   └── models.cpython-311.pyc
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   │   ├── 0001_initial.cpython-311.pyc
│   │   │   │   │   └── 0002_initial.cpython-311.pyc
│   │   │   │   ├── 0001_initial.py
│   │   │   │   └── 0002_initial.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   ├── admin.cpython-311.pyc
│   │   │   │   ├── apps.cpython-311.pyc
│   │   │   │   └── models.cpython-311.pyc
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   │   │   └── __pycache__/
│   │   │   │       └── __init__.cpython-311.pyc
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── customers/
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   ├── admin.cpython-311.pyc
│   │   │   │   ├── apps.cpython-311.pyc
│   │   │   │   └── models.cpython-311.pyc
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   │   └── 0001_initial.cpython-311.pyc
│   │   │   │   └── 0001_initial.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── manage.py
│   │   ├── market/
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   ├── settings.cpython-311.pyc
│   │   │   │   ├── urls.cpython-311.pyc
│   │   │   │   └── wsgi.cpython-311.pyc
│   │   │   ├── asgi.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   ├── market.zip
│   ├── marketDB.bak
│   ├── requirements.txt
│   └── venv/ (Python virtual environment with extensive Django dependencies)
├── Website.zip
├── archive.zip
├── Dunhummy.aux
├── Dunhummy.bcf
├── Dunhummy.log
├── Dunhummy.out
├── Dunhummy.pdf
├── Dunhummy.run.xml
├── Dunhummy.synctex.gz
├── Dunhummy.tex
├── Dunhummy.toc
├── kashanu.jpeg
├── marketDB.bak
├── report.xml
├── ReportOfDatasets.docx
├── ReportOfDunhummbyDataset.pdf
├── ~$portOfDatasets.docx (temporary file)
└── ~WRL0120.tmp (temporary file)
```

## Key Components:

### 1. Database Related Files
- **DataBase Queries/**: SQL scripts and database backups
- **marketDB.bak**: Database backup file
- **Website/marketDB.bak**: Another database backup

### 2. Django Web Application
- **Website/market/**: Main Django project
  - **catalog/**: App for product catalog functionality
  - **core/**: Core application components
  - **customers/**: Customer management app
  - **market/**: Main project settings and configuration
  - **venv/**: Python virtual environment with Django and dependencies

### 3. Data Files
- **Dunhummy/**: CSV data files containing:
  - Campaign descriptions and tables
  - Causal data
  - Coupon information
  - Household demographics
  - Product data
  - Transaction data

### 4. Documentation & Reports
- **ReportOfDatasets.docx**: Dataset documentation
- **ReportOfDunhummbyDataset.pdf**: PDF report
- **Dunhummy.tex**: LaTeX source file
- **Dunhummy.pdf**: Compiled PDF from LaTeX

### 5. Resources
- **fonts/**: Various font files (Persian, Arabic, Latin scripts)
- **kashanu.jpeg**: Image file

### 6. Configuration & Build Files
- **report.xml**: XML report file
- Various temporary and archive files (.zip, .tmp, .aux, etc.)

This appears to be a final project involving a Django-based e-commerce or market analysis website with accompanying database, data analysis, and documentation components.