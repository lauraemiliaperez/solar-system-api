from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, radius):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.radius = radius

# planet1 = Planet(1, "Mars", "It's red", 2106)
# planet2 = Planet(2, "Earth", "It has life", 3959) 
# planet3 = Planet(3, "Jupiter", "It's the biggest", 43441)

# planet_list = [planet1, planet2, planet3]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        radius = request_body["radius"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        response.append(planet.to_dict())

    return jsonify(response), 200

# @planet_bp.route("/<id>", methods=["GET"])
# def get_one_planet(id):
#     try:
#         planet_id = int(id)
#     except ValueError:
#         return {"message": f"invalid id: {id}"}, 400
    
#     for planet in planet_list:
#         if planet.id == planet_id:
#             return jsonify ({
#             "id": planet.id,
#             "name" : planet.name,
#             "description" : planet.description,
#             "radius": planet.radius
#             }), 200
    
#     return {"message": f"id {planet_id} not found"}, 404

    
