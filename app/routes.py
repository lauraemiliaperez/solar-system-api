from flask import Blueprint, jsonify, make_response, request, abort
from app import db
from app.models.planet import Planet

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

#     planet = Planet.query.get(planet_id)

#     if not planet:
#         abort(make_response({"message": f"planet {planet_id} not found"}, 404))

#     return planet

def validate_item(model, item_id):
    try:
        item_id = int(item_id)
    except ValueError:
        return abort(make_response({"msg": f"invalid id: {item_id}"}, 400))
    
    item = model.query.get(item_id)
    
    if not item:
        abort(make_response({"msg": f"planet {item_id} not found"}, 404))
    
    return item

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return {"msg": f"Planet {new_planet.name} successfully created"}, 201


@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []

    name_query = request.args.get("name")

    if name_query is None:
        all_planets = Planet.query.all()
    else: 
        all_planets = Planet.query.filter_by(name=name_query)

    for planet in all_planets:
        response.append(planet.to_dict())

    return make_response(jsonify(response), 200)


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_item(Planet, planet_id)

    return planet.to_dict(), 200


@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_item(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.radius = request_body["radius"]

    db.session.commit()

    return make_response({"msg": f"Planet {planet_id} was succesfully updated"}, 200)

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_item(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return {"msg": f"Planet {planet_id} was deleted"}, 200
