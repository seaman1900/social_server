from datetime import datetime
from models.user import User, Metadata

# 模拟数据库
fake_users_db = {
    "user123": User(
        user_id="user123",
        username="user123",
        email="test_user@example.com",
        password_hash="a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", # 123的hash
        registration_date=datetime.now(),
        last_login=datetime.now(),
        role=["user"],
        avatar_url="https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
        mark_list=[],
        wish_list=[],
        metadata=Metadata(followers=0, likes=0, dislikes=0)
    ),
    "user456": User(
        user_id="user456",
        username="user456",
        email="test_user@example.com",
        password_hash="a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", # 123的hash
        registration_date=datetime.now(),
        last_login=datetime.now(),
        role=["user"],
        avatar_url="https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
        mark_list=[],
        wish_list=[],
        metadata=Metadata(followers=0, likes=0, dislikes=0)
    ),
    "user789": User(
        user_id="user789",
        username="user789",
        email="test_user@example.com",
        password_hash="a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", # 123的hash
        registration_date=datetime.now(),
        last_login=datetime.now(),
        role=["user"],
        avatar_url="https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
        mark_list=[],
        wish_list=[],
        metadata=Metadata(followers=0, likes=0, dislikes=0)
    ),
    "user101": User(
        user_id="user101",
        username="user101",
        email="test_user@example.com",
        password_hash="a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", # 123的hash
        registration_date=datetime.now(),
        last_login=datetime.now(),
        role=["user"],
        avatar_url="https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
        mark_list=[],
        wish_list=[],
        metadata=Metadata(followers=0, likes=0, dislikes=0)
    ),
    "user202": User(
        user_id="user202",
        username="user202",
        email="test_user@example.com",
        password_hash="a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", # 123的hash
        registration_date=datetime.now(),
        last_login=datetime.now(),
        role=["user"],
        avatar_url="https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
        mark_list=[],
        wish_list=[],
        metadata=Metadata(followers=0, likes=0, dislikes=0)
    )
}