"""Restaurant rating lister."""


# put your code here
def track_restaurant_ratings(file_name):  # write a function that takes 1 parameter, file
    restaurant_ratings = {}  # create empty dictionary restaurant_rating = {}
    with open(file_name) as txt_file:  # open the file using the with..as
        for line in txt_file:  # for line in txt_file
            line = line.strip()
            key, value = line.split(":")
            restaurant_ratings[key] = value  # restaurant_rating[key] = value
   
    return restaurant_ratings

restaurant_ratings = track_restaurant_ratings("scores.txt")


def display_ratings(ratings):
    """return line by line restaurant ratings."""
   
    sorted_ratings = sorted(ratings.items())
   
    for restaurant, rating in sorted_ratings:
        print "{} is rated at {}.".format(restaurant, rating)

display_ratings(restaurant_ratings)
# sorted(ratings.items())