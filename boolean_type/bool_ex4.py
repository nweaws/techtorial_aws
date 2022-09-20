
#Creat a program to print true if there is enough ticket for the nba game
# We will have two variables sold tickets and max capacity of the stadium.
# if stadium capacity is more than sold tickets we should print true and all the
#other case we shoul print false.

sold_tickets,max_capacity = 13000, 13000

is_there_space = sold_tickets < max_capacity

print("Is there ticket left  in the NBA game",is_there_space,"because we sold",
sold_tickets,"We have max capacity of",max_capacity)