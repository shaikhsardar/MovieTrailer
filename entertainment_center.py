import fresh_tomato
import media
toy_story = media.Movie("Toy Story 3","Andy's toys get mistakenly delivered to a day care centre. Woody convinces the other toys that they weren't dumped and leads them on an expedition back home.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar","Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.","https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

#avatar.show_trailer()

bdnthkidulhania = media.Movie("Badrinath Ki Dulhania","A man (Varun Dhawan) and a woman (Alia Bhatt) fall in love despite their opposing views on gender and life in general.","https://upload.wikimedia.org/wikipedia/en/8/88/Badrinath_ki_Dulhania.jpg","https://www.youtube.com/watch?v=ztX-iGlZ_Ug")

#print(bdnthkidulhania.storyline)

#bdnthkidulhania.show_trailer()


movies = [toy_story, avatar, bdnthkidulhania]
fresh_tomato.open_movies_page(movies)
