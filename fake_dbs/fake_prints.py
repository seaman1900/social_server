from datetime import datetime
from models.print import Print, PrintMetadata
# Fake Data 1
print1 = Print(
    print_id="123e4567-e89b-12d3-a456-426614174000",
    author_id="user123",
    title="My First 3D Print",
    created_at=datetime(2023, 10, 1, 14, 30),
    price=19,
    description="A simple 3D print of a vase.",
    body="This is the body of the print, containing detailed information about the 3D model.",
    metadata=PrintMetadata(
        views=150,
        comments=10,
        likes=25,
        dislikes=2,
        total_invest=500
    ),
    tags=["3D Printing", "Vase", "Home Decor"],
    status="published"
)

# Fake Data 2
print2 = Print(
    print_id="223e4567-e89b-12d3-a456-426614174001",
    author_id="user456",
    title="Custom Phone Stand",
    created_at=datetime(2023, 9, 15, 9, 45),
    price=12,
    description="A customizable phone stand for your desk.",
    body="This print allows you to adjust the angle of your phone stand.",
    metadata=PrintMetadata(
        views=300,
        comments=20,
        likes=50,
        dislikes=5,
        total_invest=750
    ),
    tags=["Phone Accessories", "3D Printing", "Desk Organizer"],
    status="draft"
)

# Fake Data 3
print3 = Print(
    print_id="323e4567-e89b-12d3-a456-426614174002",
    author_id="user789",
    title="Miniature Figurine",
    created_at=datetime(2023, 8, 20, 18, 15),
    price=9,
    description="A small figurine for tabletop games.",
    body="This miniature is perfect for RPGs and tabletop gaming.",
    metadata=PrintMetadata(
        views=450,
        comments=30,
        likes=100,
        dislikes=10,
        total_invest=1000
    ),
    tags=["Miniature", "Tabletop Games", "RPG"],
    status="published"
)

# Fake Data 4
print4 = Print(
    print_id="423e4567-e89b-12d3-a456-426614174003",
    author_id="user101",
    title="Eco-Friendly Planter",
    created_at=datetime(2023, 7, 5, 12, 0),
    price=15,
    description="A sustainable planter for your plants.",
    body="This planter is designed to be eco-friendly and easy to print.",
    metadata=PrintMetadata(
        views=200,
        comments=15,
        likes=40,
        dislikes=3,
        total_invest=600
    ),
    tags=["Eco-Friendly", "Gardening", "3D Printing"],
    status="archived"
)

# Fake Data 5
print5 = Print(
    print_id="523e4567-e89b-12d3-a456-426614174004",
    author_id="user202",
    title="Custom Keychain",
    created_at=datetime(2023, 6, 10, 16, 20),
    price=6,
    description="A personalized keychain with your name.",
    body="This keychain can be customized with any name or text.",
    metadata=PrintMetadata(
        views=500,
        comments=25,
        likes=75,
        dislikes=8,
        total_invest=900
    ),
    tags=["Keychain", "Personalized", "3D Printing"],
    status="published"
)
fake_prints_db= {
    print1.print_id: print1,
    print2.print_id: print2,
    print3.print_id: print3,
    print4.print_id: print4,
    print5.print_id: print5,
}