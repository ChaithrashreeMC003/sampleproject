
Overview
A Python application to manage a fictional chocolate house's operations:

Seasonal flavors
Ingredient inventory.
Customer suggestions and allergy concerns
Setup Instructions
Local Setup
Clone the repository:
git clone <repo_url>
cd project
Install dependencies:
pip install django
python -m venv venv
venv/Scripts/activate
Run the application:
python manage.py runserver
Access the application at  http://127.0.0.1:8000/.
API Endpoints
Seasonal Flavors
GET /flavors: Get all flavors
Inventory
GET /inventory: Get all inventory items
POST /inventory: Add an inventory item
Customer Suggestions
GET /suggestions: Get all suggestions
POST /suggestions: Add a suggestion
