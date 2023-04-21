from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, radius):
        self.id = id
        self.name = name
        self.description = description
        self.radius = radius

planet1 = Planet(1, "Mars", "It's red", 2106)
planet2 = Planet(2, "Earth", "It has life", 3959) 
planet3 = Planet(3, "Jupiter", "It's the biggest", 43441)

planet_list = [planet1, planet2, planet3]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    for planet in planet_list:
        planet_dict = {
            "id": planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "radius": planet.radius
        }
        response.append(planet_dict)

    return jsonify(response), 200

@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    try:
        planet_id = int(id)
    except ValueError:
        return {"message": f"invalid id: {id}"}, 400
    
    for planet in planet_list:
        if planet.id == planet_id:
            return jsonify ({
            "id": planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "radius": planet.radius
            }), 200
    
    return {"message": f"id {planet_id} not found"}, 404

    
