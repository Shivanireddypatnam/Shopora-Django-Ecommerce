# Shopora – Django E-commerce Website

## 1. About the Project

**Shopora** is a web-based e-commerce application developed using Python and Django. It allows customers to browse products, search for items, add products to a shopping cart, save products to a wishlist, place orders, and manage their purchases.

This project demonstrates the main features of an online shopping website, including user authentication, product management, cart management, order processing, and database operations.

This guide explains how to set up, run, and test the project on a Windows computer.

## 2. Project Features

### Customer Features
- Register a new account.
- Log in and log out securely.
- Browse available products.
- Search for products.
- Filter products by category.
- View individual product details.
- Add products to a shopping cart.
- Update or remove cart items.
- Add products to a wishlist.
- Remove products from a wishlist.
- Enter shipping details during checkout.
- Place an order.
- View previous orders and order details.
- Cancel eligible orders.
- Restore product stock when an eligible order is cancelled.

### Administrative Features
- Manage application data through Django Admin.
- Add and manage product categories.
- Add and manage products.
- Review relevant order and customer records, according to the configured admin permissions.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Web application framework |
| MySQL | Database |
| HTML | Web page structure |
| CSS | Web page styling |
| JavaScript | Client-side interactions |
| Git | Version control |
| GitHub | Source code hosting |

## 4. Requirements

Before installing the project, make sure your computer has the following software:

1. **Python** – Required to run the Django application.
2. **MySQL Server** – Required to store application data when using the configured MySQL database.
3. **Visual Studio Code** – Recommended editor for viewing and modifying the code.
4. **Git** – Required to clone the repository from GitHub.
5. **A web browser** – Chrome, Edge, Firefox, or another modern browser.

Download the software from the official websites:

- Python: https://www.python.org/downloads/
- MySQL: https://dev.mysql.com/downloads/installer/
- Visual Studio Code: https://code.visualstudio.com/
- Git: https://git-scm.com/downloads

During Python installation on Windows, select **Add Python to PATH** if that option is shown.

To check whether Python and Git are installed, open PowerShell and run:

```powershell
python --version
git --version
```

Both commands should display version information.

## 5. Download the Project

Open PowerShell and navigate to the folder where you want to store the project.

For example:

```powershell
cd Desktop
```

Clone the repository:

```powershell
git clone https://github.com/Shivanireddypatnam/Shopora-Django-Ecommerce.git
```

Open the downloaded project folder:

```powershell
cd Shopora-Django-Ecommerce
```

Open it in Visual Studio Code:

```powershell
code .
```

If the `code` command is unavailable, open Visual Studio Code manually and select **File → Open Folder**, then choose the downloaded project folder.

## 6. Create a Virtual Environment

A virtual environment keeps the Python packages required by this project separate from packages used by other projects.

In the project folder, run:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, the terminal should show `(venv)` at the beginning of the prompt.

If PowerShell blocks activation, you can use Command Prompt and run:

```cmd
venv\Scripts\activate.bat
```

## 7. Install Project Dependencies

First, check whether the repository contains a `requirements.txt` file.

If it exists, install the packages listed in it:

```powershell
python -m pip install -r requirements.txt
```

If the file does not exist, the project maintainer should create it from the working development environment and upload it to GitHub before other users attempt installation. The required packages must be identified from the actual project configuration.

Verify that Django is installed:

```powershell
python -m django --version
```

The command should display the installed Django version.

## 8. Configure the MySQL Database

Shopora uses MySQL in its configured development environment. MySQL Server must be installed and running before starting the application.

### Step 1: Create the database

Open your MySQL client or MySQL Workbench and execute:

```sql
CREATE DATABASE ecommerce_db;
```

If the database already exists, do not create it again.

### Step 2: Configure Django

Open:

`shoppingapp/settings.py`

Find the `DATABASES` configuration and confirm that it points to your MySQL database.

The configuration must use the database name, MySQL username, password, host, and port that are valid on your computer.

**Security note:** Never publish your real database password or Django secret key in a public GitHub repository. Use environment variables or another appropriate local configuration method for sensitive values.

If you are using a different database name or MySQL account, update the local configuration accordingly.

## 9. Apply Database Migrations

Migrations create the database tables required by Django models.

In the terminal, make sure you are in the same folder as `manage.py` and your virtual environment is active.

Run:

```powershell
python manage.py check
```

This checks the Django project configuration.

Next, apply the existing migrations:

```powershell
python manage.py migrate
```

Wait for the command to finish. Django should report that the migrations have been applied or are already up to date.

If Django reports a database connection error, confirm that MySQL is running and that the database credentials in the local settings are correct.

## 10. Create an Administrator Account

Create a Django administrator account:

```powershell
python manage.py createsuperuser
```

Follow the prompts to enter a username, email address if requested, and password.

The password may not appear on the screen while you type. This is normal.

This account allows you to access the Django administration interface.

## 11. Add Sample Products

A newly installed database may not contain any products or categories. If the product list is empty, add some sample data before testing the shopping features.

### Step 1: Start the server

```powershell
python manage.py runserver
```

### Step 2: Open Django Admin

Visit:

http://127.0.0.1:8000/admin/

Log in with the administrator account created in the previous step.

### Step 3: Add categories and products

If the relevant models are registered in Django Admin:

1. Create at least one product category.
2. Add several sample products.
3. Enter the required product details, including name, price, category, and available stock.
4. Save each product.
5. Open the customer-facing home page to confirm that the products appear.

Use the actual fields shown by your project. If categories or products do not appear in Django Admin, check whether their models have been registered and whether the database migrations have been applied.

## 12. Run the Application

From the directory containing `manage.py`, execute:

```powershell
python manage.py runserver
```

The terminal should display a message indicating that the development server is running.

Open the following address in your browser:

http://127.0.0.1:8000/

You should see the Shopora application.

**Important:** Keep the terminal open while using the application. To stop the development server, return to the terminal and press `Ctrl + C`.

The Django development server is intended for local development and testing, not direct production hosting.

## 13. Manual Testing Guide

The following checklist can be used to test the main application features through the browser.

### Test 1: User Registration

1. Open the Shopora home page.
2. Navigate to the registration page.
3. Enter the requested details.
4. Submit the form.
5. Confirm that registration succeeds or that appropriate validation messages appear.

**Expected result:** A valid registration should create an account and follow the application's configured success flow.

### Test 2: Login and Logout

1. Log in with a registered account.
2. Confirm that the account is authenticated.
3. Log out.
4. Attempt to open a page that requires authentication.

**Expected result:** Login and logout should work correctly, and protected pages should follow the application's authentication rules.

### Test 3: Product Browsing

1. Open the home page.
2. Confirm that the sample products are displayed.
3. Open a product.
4. Check the product details.

**Expected result:** The correct product information should be displayed.

### Test 4: Search and Category Filtering

1. Enter a product name into the search field.
2. Submit the search.
3. Select a product category.

**Expected result:** The displayed products should match the search term or selected category.

### Test 5: Shopping Cart

1. Log in as a customer.
2. Add a product to the cart.
3. Open the cart.
4. Change the quantity if supported.
5. Remove a product.

**Expected result:** The cart should reflect the selected items and quantities, and removed items should no longer appear.

### Test 6: Wishlist

1. Log in as Customer A.
2. Add a product to the wishlist.
3. Open the wishlist and confirm that the product appears.
4. Remove the product and confirm that it disappears.
5. Log in as Customer B and check the wishlist.

**Expected result:** Wishlist actions should work, and one customer's wishlist should not expose another customer's saved items.

### Test 7: Checkout and Order Placement

1. Log in as a customer.
2. Add a product to the cart.
3. Proceed to checkout.
4. Enter the required shipping details.
5. Submit the order.

**Expected result:** A valid order should be created, the order details should be available, and product stock and cart contents should update according to the application's order-processing logic.

### Test 8: My Orders and Order Details

1. Place an order.
2. Open the My Orders page.
3. Select the order to view its details.

**Expected result:** The customer should see their own order history and the relevant details for the selected order.

### Test 9: Order Cancellation

1. Place an order that is eligible for cancellation.
2. Record the product's stock quantity.
3. Cancel the order.
4. Check the order status.
5. Check the product stock again.

**Expected result:** The order status should change to the configured cancelled status, and the stock should be restored according to the application's cancellation logic.

### Test 10: Access Control

1. Log out.
2. Try to access the cart, wishlist, or order pages directly.
3. Log in as a different customer and revisit customer-specific pages.

**Expected result:** Authentication and ownership rules should prevent unauthorized access to protected customer data.

**Testing note:** These are manual test procedures and expected results, not a claim that every test has been executed on a fresh installation. Record actual results when you perform them.

## 14. Troubleshooting

### Error: `python is not recognized`

Install Python and ensure it is available on PATH. Close and reopen the terminal, then try:

```powershell
python --version
```

### Error: `No module named django`

Activate the project's virtual environment and install the required dependencies:

```powershell
python -m pip install -r requirements.txt
```

This command requires the repository to contain a valid `requirements.txt` file.

### Error: MySQL connection refused

Check that MySQL Server is running. Confirm the database name, username, password, host, and port in your local Django configuration.

### Error: `Unknown database`

Create the database specified in the Django database configuration, or correct the configured database name.

### Error: `no such table` or missing database tables

Make sure you have activated the correct virtual environment and run:

```powershell
python manage.py migrate
```

### Error: No products are displayed

The database may not contain any product records. Open Django Admin, create the necessary categories and products, and refresh the home page.

### Error: Port 8000 is already in use

Run the development server on another port:

```powershell
python manage.py runserver 8001
```

Then open:

http://127.0.0.1:8001/

### Error: Page not found (404)

Confirm that the URL is correct and that the relevant URL patterns have been configured in the Django application.

## 15. Project Structure

The repository contains the Django project and its application modules.

```text
Shopora-Django-Ecommerce/
│
├── manage.py
├── shoppingapp/
├── accounts/
├── products/
├── carts/
├── orders/
├── wishlist/
├── templates/
├── static/
├── .gitignore
└── README.md
```

Additional files, including the dependency list and environment configuration instructions, should be included where required.

## 16. Screenshots

Add screenshots of the actual running application to a `screenshots/` folder in the repository.

Recommended screenshots:

1. Home page with products.
2. Registration or login page.
3. Product details page.
4. Shopping cart.
5. Wishlist.
6. Checkout page.
7. My Orders page.
8. Order details or cancellation result.
9. Django Admin, if useful for demonstrating product management.

Use relative image paths so GitHub can display them. For example, if a screenshot is saved as `screenshots/home.png`, include:

```markdown
![Shopora Home Page](screenshots/home.png)
```

Only include screenshots that you have actually captured from the application.

## 17. Future Improvements

Possible future improvements include:

- Payment gateway integration.
- Order confirmation emails.
- Product reviews and ratings.
- Improved automated test coverage.
- Deployment to a production hosting platform.

These are potential enhancements and are not necessarily implemented in the current version.

## 18. Author

**Shivani Reddy Patnam**

GitHub: https://github.com/Shivanireddypatnam

## 19. Project Repository

Source code:

https://github.com/Shivanireddypatnam/Shopora-Django-Ecommerce
