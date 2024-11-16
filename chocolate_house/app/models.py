from app.database import db

class SeasonalFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

class IngredientInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_suggestion = db.Column(db.String(200), nullable=False)
    allergy_concern = db.Column(db.String(200), nullable=True)
