from django.shortcuts import render

class Article(models.Model):
	class Meta():
		db_table = "article"
	aritcle_title = models.CharField(max_length = 200)
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField()