from fastapi.testclient import TestClient
from Main_FastApi import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello welcome to my app python"}


def test_read_machine():
    response = client.get("/machine/inversion", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "hostname": "inversion",
        "ip": "125.0.0.12",
        "nombre_cpu": 0,
        "taille_ram": 0,
        "nombre_disque_dur": 0,
        "taille_disque_dur": 0,
        "os": "string",
        "version_os": "string"
    }


def test_read_inexistent_machine():
    response = client.get("/machine/apiapiapi", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 400
    assert response.json() == {"detail": "machine not found"}


def test_create_machine():
    response = client.post(
        "/machine/",
        headers={"X-Token": "coneofsilence"},
        json={
            "hostname": "apitest",
            "ip": "125.0.0.12",
            "nombre_cpu": 0,
            "taille_ram": 0,
            "nombre_disque_dur": 0,
            "taille_disque_dur": 0,
            "os": "string",
            "version_os": "string"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "hostname": "apitest",
        "ip": "125.0.0.12",
        "nombre_cpu": 0,
        "taille_ram": 0,
        "nombre_disque_dur": 0,
        "taille_disque_dur": 0,
        "os": "string",
        "version_os": "string"
    }


def test_create_machine_bad_headers():
    response = client.post(
        "/machine/",
        headers={"X-Token": "hailhydra"},
        json={
            "hostname": "apitest",
            "ip": "125.0.0.12",
            "nombre_cpu": 0,
            "taille_ram": 0,
            "nombre_disque_dur": 0,
            "taille_disque_dur": 0,
            "os": "string",
            "version_os": "string"
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_machine():
    response = client.post(
        "/machine/",
        headers={"X-Token": "coneofsilence"},
        json={
            "hostname": "inversion",
            "ip": "125.0.0.12",
            "nombre_cpu": 0,
            "taille_ram": 0,
            "nombre_disque_dur": 0,
            "taille_disque_dur": 0,
            "os": "string",
            "version_os": "string"
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Machine already exists"}
