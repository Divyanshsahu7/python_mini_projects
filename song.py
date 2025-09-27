import random
import webbrowser
class mood:
	def __init__(self,mood,playlist):
		self.mood=mood
		self.playlist=playlist
	def suggest_song(self):
		 return random.choice(self.playlist) 

happy = mood("happy", [
    "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Happy - Pharrell Williams
    "https://www.youtube.com/watch?v=1y6smkh6c-0",  # Good Life - Kanye West
])

sad = mood("sad", [
    "https://www.youtube.com/watch?v=RB-RcX5DS5A",  # Someone Like You - Adele
    "https://www.youtube.com/watch?v=RBumgq5yVrA",  # Let Her Go - Passenger
])

energetic = mood("energetic", [
    "https://www.youtube.com/watch?v=_Yhyp-_hX2s",  # Lose Yourself - Eminem
    "https://www.youtube.com/watch?v=PsO6ZnUZI0g",  # Stronger - Kanye West
    "https://www.youtube.com/watch?v=btPJPFnesV4"   # Eye of the Tiger - Survivor
])

focus = mood("focus", [
    "https://www.youtube.com/watch?v=UfcAVejslrU",  # Weightless - Marconi Union
    "https://www.youtube.com/watch?v=Yw8i5z9UJ2A",  # Night Owl - Galimatias
    "https://www.youtube.com/watch?v=7gphiFVVtUI"   # Sunset Lover - Petit Biscuit
])

moods = {
    "happy": happy,
    "sad": sad,
    "energetic": energetic,
    "focus": focus
}

print("++++++++++Mood to music suggestor+++++")
user_mood=input("Enter your mood :")

if user_mood in moods:
  link = moods[user_mood].suggest_song()
  print(f"Suggested Song: {link}")
  webbrowser.open(link)
else:
    print("Sorry! Mood not found in system.")