from app import app
from models import User, Post, Group, user_groups, db

with app.app_context():
    db.session.query(user_groups).delete()
    db.session.commit()
    # Delete all data from the tables
    User.query.delete()
    Post.query.delete()
    Group.query.delete()

    # Add Users
    u1 = User(username='user1', email="user1@example.com")
    u2 = User(username='user2', email="user2@example.com")
    u3 = User(username='user3', email="user3@example.com")
    u4 = User(username='user4', email="user4@example.com")
    u5 = User(username='user5', email="user5@example.com")

    db.session.add_all([u1, u2, u3, u4, u5])
    db.session.commit()

    # Add Posts
    posts = [
        Post(title="post1", description="post1 description", user=u1),
        Post(title="post2", description="post2 description", user=u1),
        Post(title="post3", description="post3 description", user=u1),
        Post(title="post4", description="post4 description", user=u1),
        Post(title="post5", description="post5 description", user=u1),
        Post(title="post6", description="post6 description", user=u1),
        Post(title="post7", description="post7 description", user=u1),
        Post(title="post8", description="post8 description", user=u1),
        Post(title="post9", description="post9 description", user=u1),
        Post(title="post10", description="post10 description", user=u1)
    ]

    db.session.add_all(posts)
    db.session.commit()

    # Add Groups
    g1 = Group(name="group1")
    g2 = Group(name="group2")
    g3 = Group(name="group3")
    g4 = Group(name="group4")
    g5 = Group(name="group5")

    db.session.add_all([g1, g2, g3, g4, g5])
    db.session.commit()

    # Add Groups to Users and vice versa
    u1.groups.append(g5)
    u1.groups.append(g2)

    g5.users.append(u2)
    g5.users.append(u5)

    g4.users.append(u3)
    g4.users.append(u1)

    db.session.commit()
