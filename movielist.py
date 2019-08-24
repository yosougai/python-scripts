movielist = 0
moviestor = []
number = 0

print "What are your top ten favorite Netflix movies?"

while movielist < 10:
    movies = raw_input("Please enter the movie's title: ")
    moviestor.append(movies)
    movielist = movielist + 1
    
print "\nYour list of favorite movies is:"

for i in moviestor:
    number = number + 1
    print "#"+str(number)+".", i