from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


posts: list[dict] = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is the content of the first post.",
        "date": "2023-01-01"
    },
    {
        "id": 2,
        "author": "Jane Smith",
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "date": "2023-01-02"
    }
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/post", include_in_schema=False)
@app.get("/smth", include_in_schema=False, name="smth")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts})


@app.get("/posts")
def get_posts():
    return posts