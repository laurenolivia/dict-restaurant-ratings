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

print_ratings = print_ratings(ratings(restaurant_ratings)
# sorted(ratings.items())

# write function that takes file as arg
# while loop = True
# user_input has 3 options, view, add, quit
# if == "view" run print_display function
# elif == "add":
    #add_restaurant_name 
    #add_rating 1-5 


#write function accept two args, restaurant_name, rating 
def add_to_restaurant_ratings(restaurant_name, rating):
    restaurant_name = raw_input("Enter the restaurant name: ").capitalize()
    rating = int(raw_input("Enter rating 1 - 5 only: "))


    restaurant_ratings[restaurant_name] = restaurant_ratings.get(rating, 0) + rating

    return restaurant_ratings