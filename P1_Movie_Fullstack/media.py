import webbrowser

class Movies():
	""" This is a class that creates and stores movies and their information.
	Attributes:
		title(str): This stores the movie title
		storyline(str): This stores a short
                                description of the plot line
		poster_image_url(str): This stores a url
                                link to the poster image of the movie
		trailer_youtube_url(str): This stores a url
                                link to the youtube video of the trialer
		rt_rating(str): This stores a movie rating
                                from rotten tomato 
	"""

	#This function initializes an intstance of movie and sets the attributes of that movie
	def __init__(self, movie_title, movie_storyline,
                     poster_image, trailer_youtube, rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rt_rating = rating

	#This function opens a movie trailer from the youtube url
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
