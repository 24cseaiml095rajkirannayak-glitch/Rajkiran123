class Post:
    total_posts = 0

    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.likes = 0
        self.comments = []
        Post.total_posts += 1

    def add_like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"\n📝 {self.user.username}: {self.content}\n   ❤ Likes: {self.likes} | 💬 Comments: {len(self.comments)}"

class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text

    def __str__(self):
        return f"   └─ @{self.user.username}: {self.text}"

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        return post

    def like_post(self, post):
        post.add_like()

    def comment_on_post(self, post, text):
        comment = Comment(self, text)
        post.add_comment(comment)
        return comment

    def __str__(self):
        return f"👤 @{self.username} | Posts: {len(self.posts)}"

# Get input from user
print("=== Mini Social Media Platform ===\n")

# Create users
u1_name = input("Create User 1 - Username: ")
u1 = User(u1_name)

u2_name = input("Create User 2 - Username: ")
u2 = User(u2_name)

print("\n--- Post Creation ---")
# Create post
post_content = input(f"\n{u1_name}, write a post: ")
p1 = u1.create_post(post_content)
print("✓ Post created!")

# Like post
print(f"\n--- Interaction ---")
like_choice = input(f"{u2_name}, do you like this post? (yes/no): ").lower()
if like_choice in ["yes", "y"]:
    u2.like_post(p1)
    print("✓ Liked!")

# Comment on post
comment_choice = input(f"{u2_name}, do you want to comment? (yes/no): ").lower()
if comment_choice in ["yes", "y"]:
    comment_text = input("Write your comment: ")
    u2.comment_on_post(p1, comment_text)
    print("✓ Comment added!")

# Display feed
print("\n=== Feed ===")
print(p1)

if p1.comments:
    print("\n   Comments:")
    for c in p1.comments:
        print(c)

# Display statistics
print(f"\n--- Platform Statistics ---")
print(f"Total posts: {Post.total_posts}")
print(f"{u1}")
print(f"{u2}")
