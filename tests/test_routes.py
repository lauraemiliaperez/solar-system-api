import pytest

def test_get_all_planets(client, two_planets):
    response = client.get("/planet")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Earth",
            "description": "It has water",
            "radius": 2456
        },
        {
            "id": 2,
            "name": "Venus",
            "description": "The love planet",
            "radius": 3456
        }
    ]

def test_get_one_planet():
    pass

def test_get_non_existing_planet_returns_404(client, two_planets):
    response = client.get("/planet/3")

    response_body = response.get_json()

    assert response.status_code == 404
    assert "planet 3 not found" in response_body["msg"]



def test_post_creates_planet(client):
    response = client.post("/planet", json={
            "name": "Earth",
            "description": "It has water",
            "radius": 2456
        })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "Earth" in response_body["msg"]


def test_delete_planet(client, two_planets):
    response = client.delete("/planet/2")

    response_body = response.get_json()

    assert response.status_code == 200
    assert "Planet 2 was deleted" in response_body["msg"]

def test_put_planet(client, two_planets):
    response = client.put("planet/1", json={
        "name": "Mars",
        "description": "It's red",
        "radius": 2432
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert "Planet 1 was succesfully updated" in response_body["msg"]

