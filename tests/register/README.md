# Signup Tests

This directory contains automated tests for user registration/signup functionality on the PrintXpand application.

## Test Files

### 1. `signup-maurya-patel.py`
- **Purpose**: Specific test case for Maurya Patel user signup
- **Test Data**: 
  - First Name: Maurya
  - Last Name: Patel
  - Email: maurya115@yopmail.com
  - Password: baps@200
- **Features**:
  - Detailed allure reporting with screenshots
  - Step-by-step test execution
  - Comprehensive verification
  - Critical priority test

### 2. `signup-generic.py`
- **Purpose**: Generic signup test with dynamic test data
- **Test Data**: Auto-generated unique data using timestamp
- **Features**:
  - Reusable test with unique email generation
  - Same verification steps as specific test
  - Normal priority test

### 3. `register-new.py`
- **Purpose**: Original demo test (legacy)
- **Note**: Uses different URL and may need updates

## Test Flow

Both signup tests follow this sequence:

1. **Navigate to Website** → `https://dev-headless.printxpand.tech/en`
2. **Click My Account** → Access account menu
3. **Navigate to Signup** → Click signup link from dropdown
4. **Fill Form** → Enter all required fields
5. **Submit Form** → Click "Create An Account" button
6. **Verify Success** → Check for success message and redirect

## Verification Points

- ✅ Redirected to login page (`/customer/account/login`)
- ✅ Success message displayed ("Customer register successfully")
- ✅ Login form is visible and accessible
- ✅ All form fields are properly filled

## Running Tests

### Option 1: Using the Test Runner Script
```bash
# Run all signup tests
python run_signup_tests.py

# Run specific test only
python run_signup_tests.py --specific

# Run generic test only
python run_signup_tests.py --generic

# Run in headless mode
python run_signup_tests.py --headless

# Run with verbose output
python run_signup_tests.py --verbose
```

### Option 2: Direct pytest commands
```bash
# Run all signup tests
pytest tests/register/ -v --alluredir=allure-results

# Run specific test
pytest tests/register/signup-maurya-patel.py -v --alluredir=allure-results

# Run generic test
pytest tests/register/signup-generic.py -v --alluredir=allure-results
```

## Allure Reports

After running tests, generate and view reports:

```bash
# Generate report
allure generate allure-results --clean -o allure-report

# Serve report (opens in browser)
allure serve allure-results

# Or open static report
open allure-report/index.html
```

## Test Data Management

### Specific Test Data (signup-maurya-patel.py)
- Hard-coded test data as per requirements
- Consistent results for specific user scenario
- Easy to trace and debug

### Dynamic Test Data (signup-generic.py)
- Auto-generated unique emails using timestamp
- Prevents conflicts with existing accounts
- Good for continuous testing

## Screenshots and Attachments

Each test captures:
- Homepage state
- My Account click
- Signup page
- Filled form
- After submission
- Final verification state
- Form data used
- Verification results
- Test summary

## Dependencies

- `playwright` - Browser automation
- `pytest` - Test framework
- `allure-pytest` - Reporting
- `pytest-playwright` - Playwright integration

## Configuration

Tests use the configuration from:
- `conftest.py` - Browser and page fixtures
- `pytest.ini` - Pytest configuration
- Browser runs in headed mode by default (configurable in conftest.py)

## Troubleshooting

### Common Issues

1. **Browser not found**: Ensure Chrome is installed
2. **Timeout errors**: Increase wait times if network is slow
3. **Element not found**: Check if website structure changed
4. **reCAPTCHA**: Tests may need manual intervention for reCAPTCHA

### Debug Mode
Run with verbose output to see detailed execution:
```bash
python run_signup_tests.py --verbose
```

## Test Maintenance

- Update selectors if website structure changes
- Adjust wait times based on performance
- Update test data as needed
- Monitor allure reports for failures
