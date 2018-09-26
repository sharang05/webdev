
import uuid
from database import Database
import datetime

class Post(object):

	def __init__(self, blog_id, title, content, author, date = datetime.datetime.utcnow(), post_id = None):
		self.blog_id = blog_id
		self.title = title
		self.content = content
		self.author = author
		self.date =date
		self.post_id = uuid.uuid4().hex if post_id is None else post_id

	def save_to_mongo(self):
		Database.insert(collection = 'posts',
						data = self.json())

	def json(self):
		return {'post_id': self.post_id,
				'blog_id': self.blog_id,
				'author': self.author,
				'title': self.title,
				'content': self.content,
				'date': self.date
		}

	@staticmethod
	def from_mongo(id):
		return Database.find_one('posts', query ={'post_id': id})

	@staticmethod
	def from_blog(id):
		return [post for post in Database.find(collection = 'posts', query= {'blog_id': id})]