
from post import Post
from database import Database


Database.initialize()

post = Post("The nun", "This is recent released hollywood movie", "Not Known")

print("Tilte of Movie is {}".format(post.title))
print(post.content)