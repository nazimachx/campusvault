from fastapi.testclient import TestClient
from app.main import app
from pydantic import BaseModel, ConfigDict, Field

client = TestClient(app)

def test_create_then_read():
    r = client.post("/notes", json={"title": "Docker", "body": "namespaces + cgroups"}) 
    assert r.status_code == 201 
    note_id = r.json()["id"] 
    assert r.headers["Location"] == f"/notes/{note_id}" 
    assert client.get(f"/notes/{note_id}").json()["title"] == "Docker"
    
def test_missing_note_is_404(): 
    assert client.get("/notes/99999").status_code == 404

# TODO 5 (security): a body with an unknown field "owner" must be rejected with 422

class NoteCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    body: str

# TODO 6 (security): a title of 101 characters must be rejected with 422

class NoteCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(max_length=100)
    body: str

class NoteUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str | None = Field(default=None, max_length=100)
    body: str | None = None

# TODO 7: DELETE returns 204, then GET on the same id returns 404

def test_delete_then_get_404():
    r = client.post(
        "/notes",
        json={
            "title": "Docker",
            "body": "namespaces and cgroups"
        }
    )

    note_id = r.json()["id"]

    delete_response = client.delete(f"/notes/{note_id}")

    assert delete_response.status_code == 204

    get_response = client.get(f"/notes/{note_id}")

    assert get_response.status_code == 404