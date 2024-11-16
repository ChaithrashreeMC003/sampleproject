from flask import Flask, request, jsonify
from app.database import db
from app.models import SeasonalFlavor, IngredientInventory, CustomerSuggestion

def register_routes(app):
    @app.route('/flavors', methods=['GET', 'POST'])
    def flavors():
        if request.method == 'POST':
            data = request.json
            new_flavor = SeasonalFlavor(name=data['name'], description=data.get('description'))
            db.session.add(new_flavor)
            db.session.commit()
            return jsonify({"message": "Flavor added"}), 201
        flavors = SeasonalFlavor.query.all()
        return jsonify([{"id": f.id, "name": f.name, "description": f.description} for f in flavors])

    @app.route('/inventory', methods=['GET', 'POST'])
    def inventory():
        if request.method == 'POST':
            data = request.json
            new_item = IngredientInventory(name=data['name'], quantity=data['quantity'])
            db.session.add(new_item)
            db.session.commit()
            return jsonify({"message": "Inventory item added"}), 201
        items = IngredientInventory.query.all()
        return jsonify([{"id": i.id, "name": i.name, "quantity": i.quantity} for i in items])

    @app.route('/suggestions', methods=['GET', 'POST'])
    def suggestions():
        if request.method == 'POST':
            data = request.json
            new_suggestion = CustomerSuggestion(
                flavor_suggestion=data['flavor_suggestion'],
                allergy_concern=data.get('allergy_concern')
            )
            db.session.add(new_suggestion)
            db.session.commit()
            return jsonify({"message": "Suggestion added"}), 201
        suggestions = CustomerSuggestion.query.all()
        return jsonify([{"id": s.id, "flavor_suggestion": s.flavor_suggestion, "allergy_concern": s.allergy_concern} for s in suggestions])
