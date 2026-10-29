from fastapi import FastAPI, HTTPException
from src.schemas import PostCreate


app = FastAPI()


text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "AI Project", "content": "Just finished building a new AI project."},
    3: {"title": "Learning Update", "content": "Learning more about machine learning and AI every day."},
    4: {"title": "Project Update", "content": "Made some progress on my latest project today."},
    5: {"title": "New Feature", "content": "Added a new feature and everything is working smoothly."},
    6: {"title": "Coding Session", "content": "Spent the day coding and experimenting with new ideas."},
    7: {"title": "Milestone", "content": "Reached an exciting milestone in my project!"},
    8: {"title": "Tech Update", "content": "Trying out some new technologies and tools."},
    9: {"title": "Weekend Project", "content": "Working on a small project this weekend."},
    10: {"title": "Getting Started", "content": "Starting a new journey into AI and software development."},
    11: {"title": "Quick Update", "content": "Another productive day of learning and building."},
    12: {"title": "Experiment", "content": "Testing a few new ideas to see what works best."}
}



# To retrive all posts
@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts
    
    # When dealing with APIs and endpoints, we use JSON (JavaScript Object Notation) files. 
    # JSON object is similar to dictionary and can work with it.


# To retrive a specific post
@app.get("/posts/{id}")
def get_post(id: int):

    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_posts.get(id)

    # The ID will go from the link (decorator) to the function parameter and then to the body of the function



# To upload a post
@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
