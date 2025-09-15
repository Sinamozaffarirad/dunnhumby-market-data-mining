# Market Data Mining Project

A comprehensive Django-based web application for market basket analysis using the Dunnhumby dataset.

## Features

### 🛒 Market Basket Analysis
- **Descriptive Analysis**: Association rules mining at department and commodity levels
- **Predictive Analysis**: Machine learning models (Neural Networks, Random Forest, SVM) for future purchase predictions
- **Differential Analysis**: Statistical comparison between customer segments, time periods, store locations, and seasonal patterns

### 🤖 Machine Learning
- **Multiple ML Models**: Neural Networks, Random Forest, SVM, Gradient Boosting
- **Dynamic Configuration**: Configurable training parameters and model selection
- **AI-Powered Recommendations**: Product recommendations with confidence scores and revenue impact predictions
- **Real-time Training**: Background model training with progress tracking

### 📊 Interactive Visualizations
- **Dynamic Charts**: Interactive charts using Chart.js with real-time updates
- **Professional UI**: Modern Bootstrap 5 interface with responsive design
- **Expandable Views**: Popup modals for detailed analysis views
- **Clickable Cards**: Detailed insights accessible through interactive cards

### 🗄️ Data Management
- **SQL Server Integration**: Direct connection to Dunnhumby database
- **Data Import/Export**: CSV data manipulation capabilities
- **Customer Segmentation**: Advanced customer profiling and segmentation
- **Transaction Analysis**: Comprehensive transaction data analysis

## Technology Stack

### Backend
- **Django 5.2.10**: Web framework
- **Python 3.x**: Core programming language
- **SQL Server**: Database with mssql-django adapter
- **scikit-learn**: Machine learning library
- **pandas & numpy**: Data processing

### Frontend
- **Bootstrap 5**: UI framework
- **Chart.js**: Interactive charts
- **Font Awesome**: Icons
- **JavaScript ES6+**: Dynamic functionality

### Database
- **Microsoft SQL Server**: Primary database
- **pyodbc**: Database connectivity
- **Raw SQL queries**: Optimized database operations

## Installation

### Prerequisites
- Python 3.8+
- SQL Server
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sinamozaffarirad/market-data-mining-project.git
   cd market-data-mining-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Configuration**
   - Set up SQL Server connection in `Website/market/market/settings.py`
   - Import Dunnhumby dataset to SQL Server
   - Update database credentials

4. **Run the application**
   ```bash
   cd Website/market
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the application**
   - Open browser and navigate to `http://localhost:8000`

## Project Structure

```
market-data-mining-project/
├── Website/
│   ├── market/                 # Django project root
│   │   ├── core/              # Core application
│   │   ├── dunnhumby/         # Main analysis application
│   │   │   ├── ml_models.py   # Machine learning models
│   │   │   ├── views.py       # API endpoints and views
│   │   │   └── templates/     # HTML templates
│   │   ├── static/            # CSS, JS, images
│   │   └── templates/         # Base templates
│   └── venv/                  # Virtual environment
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Key Features in Detail

### Machine Learning Models
- **Neural Networks (MLPClassifier)**: Deep learning for complex pattern recognition
- **Random Forest**: Ensemble method for robust predictions
- **Support Vector Machines**: Kernel-based classification
- **Gradient Boosting**: Sequential learning for improved accuracy

### Analysis Types
1. **Descriptive Analysis**: Historical pattern discovery
2. **Predictive Analysis**: Future trend forecasting
3. **Differential Analysis**: Comparative statistical analysis

### API Endpoints
- `/api/ml/train/`: Train machine learning models
- `/api/ml/predictions/`: Get model predictions
- `/api/ml/recommendations/`: AI-powered product recommendations
- `/api/ml/performance/`: Model performance metrics

## Configuration

### Machine Learning Configuration
- Training/Test split ratios
- Model selection (Neural Network, Random Forest, SVM)
- Feature engineering parameters
- Cross-validation settings

### Database Configuration
Update `settings.py` with your SQL Server connection details:
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'your_database_name',
        'HOST': 'your_server',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is part of academic research. Please contact the authors for usage permissions.

## Authors

- **Sina Mozaffarirad** - *Project Lead & Developer*

## Acknowledgments

- Dunnhumby for providing the retail dataset
- Django community for the excellent web framework
- scikit-learn team for machine learning tools
- Bootstrap team for the UI framework

## Dataset

This project uses the Dunnhumby "The Complete Journey" dataset, which includes:
- Transaction data
- Product information
- Customer demographics
- Campaign and promotional data
- Causal data for market analysis

**Note**: The dataset files are not included in this repository due to size constraints. Please download from the official Dunnhumby source.

## Screenshots

The application features a modern, responsive interface with:
- Interactive dashboards
- Real-time chart updates
- Professional data visualizations
- Mobile-friendly design

## Support

For questions or issues, please open an issue on GitHub or contact the development team.

---

**Last Updated**: September 2025
**Version**: 1.0.0