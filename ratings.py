"""Restaurant rating lister."""


# put your code here
def track_restaurant_ratings(file):  # write a function that takes 1 parameter, file
    restaurant_rating = {}  # create empty dictionary restaurant_rating = {}
    with open(file) as txt_file:  # open the file using the with..as
        for line in txt_file:  # for line in txt_file
            line = line.strip()
            line = line.split(":")  # line = split line at the colon (:)
            key = line[0]  # key = line[0]
            value = line[1]  # value = line[1]
            restaurant_rating[key] = value  # restaurant_rating[key] = value
    sorted_ratings = sorted(restaurant_rating.items())
    
    return sorted_ratings

restaurant_ratings = track_restaurant_ratings("scores.txt")


for restaurant, rating in restaurant_ratings:
    print "{} is rated at {}.".format(restaurant, rating)