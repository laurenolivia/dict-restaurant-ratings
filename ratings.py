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

def access_ratings(ratings): # write function that takes file as arg
    """allow user to view ratings or add to ratings"""
    while True: # while loop = True
        user_choice = raw_input("Enter [V] to view, [A] to add or [Q] to quit: ").upper() # user_input has 3 options, view, add, quit
        if user_choice == "Q":
            break
        elif user_choice == "V":
            print_ratings # if == "view" run print_display function
        elif user_choice == "A": # elif == "add":
            restaurant_name = raw_input("Enter the restaurant name: ").capitalize()
            if restaurant_name in restaurant_ratings.keys():
                print "Restaurant already exists."
                restaurant_name = raw_input("Enter the restaurant name: ").capitalize()    
            else:
                add_to_restaurant_ratings
    

#write function accept two args, restaurant_name, rating 
def add_to_restaurant_ratings(restaurant_name):
    """Add restaurant and rating."""    
    
    while True:
        rating = int(raw_input("Enter rating 1 - 5 only: "))
        if not rating >= 1 and rating <= 5:
            print "Rating must be between 1 - 5."
            continue
        else:
            restaurant_ratings[restaurant_name] = rating
            # restaurant_ratings[restaurant_name] = restaurant_ratings.get(restaurant_name, 0) + rating

return restaurant_ratings
