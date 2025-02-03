from fastapi import FastAPI
from api.database.session import engine
from api.routes import user, post, comment, category
from api.database.models import Base, User, Category, Post, Comment
from api.schemas.user import User
from api.schemas.category import Category
from api.schemas.post import Post
from api.schemas.comment import Comment

# İleri referansları çözmek için rebuild çağırılıyor.
User.model_rebuild()
Category.model_rebuild()
Post.model_rebuild()
Comment.model_rebuild()

app = FastAPI(
    title="Blog API",
    description="Kısmen REST basit bir blog apisi.",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_event():
    """Uygulama başladığında veritabanı tablolarını oluşturur."""
    Base.metadata.create_all(bind=engine)
    # print("Veritabanı tabloları başarıyla oluşturuldu.")

@app.get("/health/", status_code=200)
def health_check():
    return {"status": "ok"}

# Router'ları ekleme
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(category.router, prefix="/api/v1/category", tags=["category"])
app.include_router(post.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(comment.router, prefix="/api/v1/comments", tags=["comments"])