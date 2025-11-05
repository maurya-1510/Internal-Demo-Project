# Playwright Python Framework

This is a comprehensive Playwright automation framework in Python for testing the PrintXpand application.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Chrome browser installed
- Required packages (see requirements.txt)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd Final-Playwright-Python

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

## 📁 Project Structure

```
Final-Playwright-Python/
├── tests/
│   ├── register/           # User registration/signup tests
│   │   ├── signup-maurya-patel.py    # Specific signup test
│   │   ├── signup-generic.py         # Generic signup test
│   │   ├── register-new.py           # Legacy demo test
│   │   └── README.md                 # Signup tests documentation
│   └── login/              # User login tests
├── config/                 # Configuration files
├── allure-results/         # Test execution results
├── allure-report/          # Generated test reports
├── conftest.py            # Pytest configuration and fixtures
├── pytest.ini            # Pytest settings
└── requirements.txt       # Python dependencies
```

## 🧪 Test Suites

### Signup Tests (`tests/register/`)

#### Maurya Patel Signup Test
- **File**: `signup-maurya-patel.py`
- **Purpose**: Tests specific user signup scenario
- **Test Data**: Maurya Patel, maurya115@yopmail.com, baps@200
- **Features**: Comprehensive allure reporting, step-by-step verification

#### Generic Signup Test  
- **File**: `signup-generic.py`
- **Purpose**: Tests signup with dynamic test data
- **Features**: Auto-generated unique emails, reusable test scenario

### Login Tests (`tests/login/`)
- Valid login scenarios
- Invalid login scenarios

## 🏃‍♂️ Running Tests

### Using Test Runner Scripts
```bash
# Run all signup tests
python run_signup_tests.py

# Run specific signup test
python run_signup_tests.py --specific

# Run generic signup test  
python run_signup_tests.py --generic
```

### Direct pytest Commands
```bash
# Run all tests
pytest tests/ -v --alluredir=allure-results

# Run specific test suite
pytest tests/register/ -v --alluredir=allure-results
pytest tests/login/ -v --alluredir=allure-results

# Run specific test file
pytest tests/register/signup-maurya-patel.py -v --alluredir=allure-results
```

## 📊 Test Reports

### Allure Reports
Generate and view detailed test reports:

```bash
# Generate report
allure generate allure-results --clean -o allure-report

# Serve report (opens in browser)
allure serve allure-results

# View static report
open allure-report/index.html
```

### Report Features
- Screenshots at each step
- Test execution timeline
- Pass/fail status
- Detailed test data
- Verification results

## ⚙️ Configuration

### Browser Configuration (`conftest.py`)
- Chrome browser in headed mode
- Configurable for headless execution
- Session and function-level fixtures

### Test Configuration (`pytest.ini`)
- Allure reporting enabled
- Test discovery patterns
- Output directory configuration

## 🔧 Framework Features

- **Playwright Integration**: Modern browser automation
- **Allure Reporting**: Rich test reports with screenshots
- **Page Object Pattern**: Maintainable test structure
- **Fixture Management**: Reusable browser and page instances
- **Test Data Management**: Both static and dynamic test data
- **Screenshot Capture**: Automatic screenshots at key steps
- **Error Handling**: Comprehensive error reporting

## 🐛 Troubleshooting

### Common Issues
1. **Browser Installation**: Run `playwright install`
2. **Dependencies**: Ensure all packages from requirements.txt are installed
3. **Network Issues**: Check internet connection and website availability
4. **Element Locators**: Update selectors if website structure changes

### Debug Mode
```bash
# Run with verbose output
python run_signup_tests.py --verbose

# Run specific test with debug
pytest tests/register/signup-maurya-patel.py -v -s
```

## 📚 Documentation

- **Signup Tests**: See `tests/register/README.md`
- **Test Data**: Check individual test files for specific data
- **Configuration**: Review `conftest.py` and `pytest.ini`

## 🤝 Contributing

1. Follow existing test patterns
2. Add allure steps for better reporting
3. Include comprehensive verification
4. Update documentation as needed
5. Test new additions thoroughly

## 📝 Test Data

### Current Test Accounts
- **Maurya Patel**: maurya115@yopmail.com (for specific signup test)
- **Dynamic Users**: Auto-generated for generic tests

### Environment
- **Test URL**: https://dev-headless.printxpand.tech/en
- **Browser**: Chrome (headed mode)
- **Timeout**: 3-5 seconds between steps