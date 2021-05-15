from fastapi.testclient import TestClient
from Main_FastApi import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello welcome to my app python"}


def test_read_machine():
    response = client.get("/machine/michael")
    assert response.status_code == 200
    assert response.json() == {
        "hostname": "michael",
        "ip": "124.0.0.1",
        "nombre_cpu": 12,
        "taille_ram": 8,
        "nombre_disque_dur": 3,
        "taille_disque_dur": 128,
        "os": "osmichael",
        "version_os": "3"
    }


def test_read_inexistent_machine():
    response = client.get("/machine/apiapiapiapi1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Machine not exists"}


def test_create_machine():
    response = client.post(
        "/machine/",
        json={
            "hostname": "apitestmahine",
            "ip": "125.0.0.12",
            "nombre_cpu": 12,
            "taille_ram": 6,
            "nombre_disque_dur": 4,
            "taille_disque_dur": 98,
            "os": "osapitestmahine",
            "version_os": "4"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "hostname": "apitestmahine",
        "ip": "125.0.0.12",
        "nombre_cpu": 12,
        "taille_ram": 6,
        "nombre_disque_dur": 4,
        "taille_disque_dur": 98,
        "os": "osapitestmahine",
        "version_os": "4"
    }


def test_create_existing_machine():
    response = client.post(
        "/machine/",
        json={
            "hostname": "michael",
            "ip": "124.0.0.1",
            "nombre_cpu": 12,
            "taille_ram": 8,
            "nombre_disque_dur": 3,
            "taille_disque_dur": 128,
            "os": "osmichael",
            "version_os": "3"
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Machine already exists"}


def test_update_machine():
    response = client.put(
        "/machine/michael",
        json={
            "hostname": "michaelupdatetest",
            "ip": "125.0.0.12",
            "nombre_cpu": 12,
            "taille_ram": 6,
            "nombre_disque_dur": 4,
            "taille_disque_dur": 98,
            "os": "osmichaelupdatetest",
            "version_os": "4"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "hostname": "michaelupdatetest",
        "ip": "125.0.0.12",
        "nombre_cpu": 12,
        "taille_ram": 6,
        "nombre_disque_dur": 4,
        "taille_disque_dur": 98,
        "os": "osmichaelupdatetest",
        "version_os": "4"
    }


def test_delete_machine():
    response = client.delete(
        "/machine/michael",
    )
    assert response.status_code == 400


def test_update_inexistent_machine():
    response = client.put("/machine/apiapiapiapi2")
    assert response.status_code == 400
    assert response.json() == {"detail": "Machine not exists"}

