from mysql import connector

db = connector.connect(host = "localhost", user = "root", passwd = "********", database = "wordpost")
cursor = db.cursor()

class wordpost():
	def get_words(self):
		cursor.execute("select * from words;")
		result = cursor.fetchall()
		for i in range(len(result)):
			result[i] = result[i][0]
		return result
	def add_word(self, word):
		cursor.execute("insert into words (Word) values ('" + word + "');")
		db.commit()
	def del_word(self, word):
		cursor.execute("delete from words where Word='" + word + "';")
		db.commit()