
import json
import app as web_app


def test_home_page_loads():
    client = web_app.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Functional Testing Lab" in response.data


def test_run_function_successfully():
    client = web_app.app.test_client()
    response = client.post(
        "/",
        data={"function": "is_adult", "args": "[18]"},
    )

    assert response.status_code == 200
    assert b"True" in response.data


def test_function_error_is_displayed():
    client = web_app.app.test_client()
    response = client.post(
        "/",
        data={"function": "is_adult", "args": "[-1]"},
    )

    assert response.status_code == 200
    assert b"ValueError" in response.data


def test_invalid_json_is_displayed():
    client = web_app.app.test_client()
    response = client.post(
        "/",
        data={"function": "is_adult", "args": "not-json"},
    )

    assert response.status_code == 200
    assert b"Error:" in response.data


def test_health_endpoint():
    client = web_app.app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["status"] == "ok"
    assert data["commit_sha"] == "local"
