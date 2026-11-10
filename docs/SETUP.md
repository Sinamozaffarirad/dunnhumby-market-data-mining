# Setup and running

These steps run the system locally on Windows. All commands are run from the repository root in
PowerShell unless stated otherwise.

## Requirements

- Python 3.11 or newer (the project was checked with Python 3.14.6)
- Microsoft SQL Server and Microsoft ODBC Driver 17 for SQL Server
- Internet access in the browser, because Bootstrap and Chart.js are loaded from a CDN

## 1. Python environment

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 2. Database

The Dunnhumby dataset tables are unmanaged Django models, so migrations do not create them. Load the
[Dunnhumby – The Complete Journey](https://www.dunnhumby.com/source-files/) files into a SQL Server
database named `marketdb`, or restore a backup of that database in SQL Server Management Studio.

`import_transactions` is a dataset-specific importer for the transaction CSV. It needs an explicit
`--csv-path`; check its column mapping against your file before using it.

The default connection uses Windows authentication against `localhost`. Set these variables if your
server, database name or driver differs:

```powershell
$env:DB_HOST = 'localhost'
$env:DB_NAME = 'marketdb'
$env:DB_DRIVER = 'ODBC Driver 17 for SQL Server'
```

## 3. Configuration

```powershell
$env:DJANGO_SECRET_KEY = & .\.venv\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Keep the same key between runs if login sessions should survive a restart. Without it, the application
generates a temporary key for each process. Other settings read from the environment:

| Variable | Default | Purpose |
|---|---|---|
| `DJANGO_DEBUG` | `1` | Debug mode |
| `DJANGO_ALLOWED_HOSTS` | loopback hosts | Allowed host names |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | empty | Trusted origins when served through a tunnel |
| `POWER_BI_EMBED_URL` | the project's published report | Power BI report shown in the BI section |

## 4. Run

```powershell
.\.venv\Scripts\python.exe webapp\manage.py migrate
.\.venv\Scripts\python.exe webapp\manage.py createsuperuser
.\.venv\Scripts\python.exe webapp\manage.py runserver
```

Open `http://127.0.0.1:8000/analysis/` and log in.

| Path | Purpose |
| --- | --- |
| `/analysis/` | Home page with key figures |
| `/analysis/basket-analysis/` | Association rules, repurchase models and revenue forecasts |
| `/analysis/association-rules/` | Product-level association rules |
| `/analysis/customer-segments/` | RFM segments and churn experiments |
| `/analysis/bi-dashboard/` | Retail performance and statistical comparisons |
| `/analysis/customer-retention/` | Retention priority list |
| `/analysis/product-recommender/` | Recommendation tools |
| `/analysis/data-management/` | Dataset browsing and maintenance |
| `/customers/search/` | Customer search and history |
| `/admin/` | Django administration |

## Trained models

`webapp/ml_models_cache/` holds the trained models the pages load: version 4 repurchase classifiers,
version 12 revenue forecasts and version 1 of the hybrid recommender. They let the pages show results
without retraining. The collaborative-filtering matrix is not included because of its size (about
2 GB); build it once with:

```powershell
cd webapp
..\.venv\Scripts\python.exe manage.py build_cf_cache
```

Other maintenance commands, also run from `webapp/`:

```powershell
..\.venv\Scripts\python.exe manage.py train_hybrid_recommender --help
..\.venv\Scripts\python.exe manage.py import_transactions --help
```

Training and maintenance commands change data or model files.

## Tests

The numerical and model-behaviour tests do not need a database:

```powershell
cd webapp
..\.venv\Scripts\python.exe manage.py test dunnhumby
```

The customer integration test needs an isolated test database.

## Demonstration scripts

`scripts/start_demo.ps1` starts the site with debug mode off and opens a temporary public HTTPS address
through a Cloudflare quick tunnel. `scripts/start_demo_ngrok.ps1` does the same through ngrok on a fixed
domain. Both expect the tunnel program (`cloudflared.exe` or `ngrok.exe`) in a local `tools/` folder,
which is not part of the repository. This setup is for a local demonstration only; a server deployment
needs its own HTTPS, cookie and database configuration.
