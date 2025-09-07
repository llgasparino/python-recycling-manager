def test_index_ok(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Recycle Manager" in resp.data


def test_404(client):
    resp = client.get("/nao-existe")
    assert resp.status_code == 404
