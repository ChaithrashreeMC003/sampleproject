# Chocolate House Application

## Overview
A Python application to manage a fictional chocolate house's operations:
- Seasonal flavors
- Ingredient inventory.
- Customer suggestions and allergy concerns

## Setup Instructions

### Local Setup
1. Clone the repository:
   ```
   git clone <repo_url>
   cd chocolate_house
   ```
2. Install dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app/main.py
   ```
4. Access the application at `http://localhost:5000`.

### Docker Setup
1. Build and run the Docker container:
   ```
   docker-compose up --build
   ```
2. Access the application at `http://localhost:5000`.

## API Endpoints
1. **Seasonal Flavors**
   - `GET /flavors`: Get all flavors
   - `POST /flavors`: Add a flavor
2. **Inventory**
   - `GET /inventory`: Get all inventory items
   - `POST /inventory`: Add an inventory item
3. **Customer Suggestions**
   - `GET /suggestions`: Get all suggestions
   - `POST /suggestions`: Add a suggestion
