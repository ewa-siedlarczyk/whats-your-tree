"""
Celtic Tree Search
Based on a date provided by the user, the program returns a name of 
a tree species according to the Celtic Tree Astrology.
"""
#%%
from sys import exit

#%% dict {(month, day) -> tree name}
long_data = {
	(1, 2): 'fir', (1, 3): 'fir', (1, 4): 'fir', (1, 5): 'fir', (1, 6): 'fir', 
	(1, 7): 'fir', (1, 8): 'fir', (1, 9): 'fir', (1, 10): 'fir', (1, 11): 'fir', 
	(7, 5): 'fir', (7, 6): 'fir', (7, 7): 'fir', (7, 8): 'fir', (7, 9): 'fir', 
	(7, 10): 'fir', (7, 11): 'fir', (7, 12): 'fir', (7, 13): 'fir', 
	(7, 14): 'fir', (1, 12): 'elm', (1, 13): 'elm', (1, 14): 'elm', 
	(1, 15): 'elm', (1, 16): 'elm', (1, 17): 'elm', (1, 18): 'elm', 
	(1, 19): 'elm', (1, 20): 'elm', (1, 21): 'elm', (1, 22): 'elm', 
	(1, 23): 'elm', (1, 24): 'elm', (7, 15): 'elm', (7, 16): 'elm', 
	(7, 17): 'elm', (7, 18): 'elm', (7, 19): 'elm', (7, 20): 'elm', 
	(7, 21): 'elm', (7, 22): 'elm', (7, 23): 'elm', (7, 24): 'elm', 
	(7, 25): 'elm', (1, 25): 'cypress', (1, 26): 'cypress', (1, 27): 'cypress', 
	(1, 28): 'cypress', (1, 29): 'cypress', (1, 30): 'cypress', 
	(1, 31): 'cypress', (2, 1): 'cypress', (2, 2): 'cypress', (2, 3): 'cypress', 
	(7, 26): 'cypress', (7, 27): 'cypress', (7, 28): 'cypress', 
	(7, 29): 'cypress', (7, 30): 'cypress', (7, 31): 'cypress', 
	(8, 1): 'cypress', (8, 2): 'cypress', (8, 3): 'cypress', (8, 4): 'cypress', 
	(2, 4): 'poplar', (2, 5): 'poplar', (2, 6): 'poplar', (2, 7): 'poplar', 
	(2, 8): 'poplar', (8, 5): 'poplar', (8, 6): 'poplar', (8, 7): 'poplar', 
	(8, 8): 'poplar', (8, 9): 'poplar', (8, 10): 'poplar', (8, 11): 'poplar', 
	(8, 12): 'poplar', (8, 13): 'poplar', (2, 9): 'cedar', (2, 10): 'cedar', 
	(2, 11): 'cedar', (2, 12): 'cedar', (2, 13): 'cedar', (2, 14): 'cedar', 
	(2, 15): 'cedar', (2, 16): 'cedar', (2, 17): 'cedar', (2, 18): 'cedar', 
	(8, 14): 'cedar', (8, 15): 'cedar', (8, 16): 'cedar', (8, 17): 'cedar', 
	(8, 18): 'cedar', (8, 19): 'cedar', (8, 20): 'cedar', (8, 21): 'cedar', 
	(8, 22): 'cedar', (8, 23): 'cedar', (2, 19): 'pine', (2, 20): 'pine', 
	(2, 21): 'pine', (2, 22): 'pine', (2, 23): 'pine', (2, 24): 'pine', 
	(2, 25): 'pine', (2, 26): 'pine', (2, 27): 'pine', (2, 28): 'pine', 
	(2, 29): 'pine', (8, 24): 'pine', (8, 25): 'pine', (8, 26): 'pine', 
	(8, 27): 'pine', (8, 28): 'pine', (8, 29): 'pine', (8, 30): 'pine', 
	(8, 31): 'pine', (9, 1): 'pine', (9, 2): 'pine', (3, 1): 'willow', 
	(3, 2): 'willow', (3, 3): 'willow', (3, 4): 'willow', (3, 5): 'willow', 
	(3, 6): 'willow', (3, 7): 'willow', (3, 8): 'willow', (3, 9): 'willow', 
	(3, 10): 'willow', (9, 3): 'willow', (9, 4): 'willow', (9, 5): 'willow', 
	(9, 6): 'willow', (9, 7): 'willow', (9, 8): 'willow', (9, 9): 'willow', 
	(9, 10): 'willow', (9, 11): 'willow', (9, 12): 'willow', (3, 11): 'linden', 
	(3, 12): 'linden', (3, 13): 'linden', (3, 14): 'linden', (3, 15): 'linden', 
	(3, 16): 'linden', (3, 17): 'linden', (3, 18): 'linden', (3, 19): 'linden', 
	(3, 20): 'linden', (9, 13): 'linden', (9, 14): 'linden', (9, 15): 'linden', 
	(9, 16): 'linden', (9, 17): 'linden', (9, 18): 'linden', (9, 19): 'linden', 
	(9, 20): 'linden', (9, 21): 'linden', (9, 22): 'linden', (3, 21): 'oak', 
	(3, 22): 'hazel', (3, 23): 'hazel', (3, 24): 'hazel', (3, 25): 'hazel', 
	(3, 26): 'hazel', (3, 27): 'hazel', (3, 28): 'hazel', (3, 29): 'hazel', 
	(3, 30): 'hazel', (3, 31): 'hazel', (9, 24): 'hazel', (9, 25): 'hazel', 
	(9, 26): 'hazel', (9, 27): 'hazel', (9, 28): 'hazel', (9, 29): 'hazel', 
	(9, 30): 'hazel', (10, 1): 'hazel', (10, 2): 'hazel', (10, 3): 'hazel', 
	(4, 1): 'rowan', (4, 2): 'rowan', (4, 3): 'rowan', (4, 4): 'rowan', 
	(4, 5): 'rowan', (4, 6): 'rowan', (4, 7): 'rowan', (4, 8): 'rowan', 
	(4, 9): 'rowan', (4, 10): 'rowan', (10, 4): 'rowan', (10, 5): 'rowan', 
	(10, 6): 'rowan', (10, 7): 'rowan', (10, 8): 'rowan', (10, 9): 'rowan', 
	(10, 10): 'rowan', (10, 11): 'rowan', (10, 12): 'rowan', (10, 13): 'rowan', 
	(4, 11): 'maple', (4, 12): 'maple', (4, 13): 'maple', (4, 14): 'maple', 
	(4, 15): 'maple', (4, 16): 'maple', (4, 17): 'maple', (4, 18): 'maple', 
	(4, 19): 'maple', (4, 20): 'maple', (10, 14): 'maple', (10, 15): 'maple', 
	(10, 16): 'maple', (10, 17): 'maple', (10, 18): 'maple', (10, 19): 'maple', 
	(10, 20): 'maple', (10, 21): 'maple', (10, 22): 'maple', (10, 23): 'maple', 
	(4, 21): 'walnut', (4, 22): 'walnut', (4, 23): 'walnut', (4, 24): 'walnut', 
	(4, 25): 'walnut', (4, 26): 'walnut', (4, 27): 'walnut', (4, 28): 'walnut', 
	(4, 29): 'walnut', (4, 30): 'walnut', (10, 24): 'walnut', (10, 25): 'walnut', 
	(10, 26): 'walnut', (10, 27): 'walnut', (10, 28): 'walnut', 
	(10, 29): 'walnut', (10, 30): 'walnut', (10, 31): 'walnut', 
	(11, 1): 'walnut', (11, 2): 'walnut', (11, 3): 'walnut', (11, 4): 'walnut', 
	(6, 4): 'hornbeam', (6, 5): 'hornbeam', (6, 6): 'hornbeam', 
	(6, 7): 'hornbeam', (6, 8): 'hornbeam', (6, 9): 'hornbeam', 
	(6, 10): 'hornbeam', (6, 11): 'hornbeam', (6, 12): 'hornbeam', 
	(6, 13): 'hornbeam', (12, 2): 'hornbeam', (12, 3): 'hornbeam', 
	(12, 4): 'hornbeam', (12, 5): 'hornbeam', (12, 6): 'hornbeam', 
	(12, 7): 'hornbeam', (12, 8): 'hornbeam', (12, 9): 'hornbeam', 
	(12, 10): 'hornbeam', (12, 11): 'hornbeam', (6, 14): 'fig tree', 
	(6, 15): 'fig tree', (6, 16): 'fig tree', (6, 17): 'fig tree', 
	(6, 18): 'fig tree', (6, 19): 'fig tree', (6, 20): 'fig tree', 
	(6, 21): 'fig tree', (6, 22): 'fig tree', (6, 23): 'fig tree', 
	(12, 12): 'fig tree', (12, 13): 'fig tree', (12, 14): 'fig tree', 
	(12, 15): 'fig tree', (12, 16): 'fig tree', (12, 17): 'fig tree', 
	(12, 18): 'fig tree', (12, 19): 'fig tree', (12, 20): 'fig tree', 
	(12, 21): 'fig tree', (6, 25): 'apple', (6, 26): 'apple', (6, 27): 'apple', 
	(6, 28): 'apple', (6, 29): 'apple', (6, 30): 'apple', (7, 1): 'apple', 
	(7, 2): 'apple', (7, 3): 'apple', (7, 4): 'apple', (12, 23): 'apple', 
	(12, 24): 'apple', (12, 25): 'apple', (12, 26): 'apple', (12, 27): 'apple', 
	(12, 28): 'apple', (12, 29): 'apple', (12, 30): 'apple', (12, 31): 'apple', 
	(1, 1): 'apple', (5, 1): 'mock-orange', (5, 2): 'mock-orange', 
	(5, 3): 'mock-orange', (5, 4): 'mock-orange', (5, 5): 'mock-orange', 
	(5, 6): 'mock-orange', (5, 7): 'mock-orange', (5, 8): 'mock-orange', 
	(5, 9): 'mock-orange', (5, 10): 'mock-orange', (5, 11): 'mock-orange', 
	(5, 12): 'mock-orange', (5, 13): 'mock-orange', (5, 14): 'mock-orange', 
	(11, 5): 'mock-orange', (11, 6): 'mock-orange', (11, 7): 'mock-orange', 
	(11, 8): 'mock-orange', (11, 9): 'mock-orange', (11, 10): 'mock-orange', 
	(11, 11): 'mock-orange', (5, 15): 'horse chestnut', 
	(5, 16): 'horse chestnut', (5, 17): 'horse chestnut', 
	(5, 18): 'horse chestnut', (5, 19): 'horse chestnut', 
	(5, 20): 'horse chestnut', (5, 21): 'horse chestnut', 
	(5, 22): 'horse chestnut', (5, 23): 'horse chestnut', 
	(5, 24): 'horse chestnut', (11, 12): 'horse chestnut', 
	(11, 13): 'horse chestnut', (11, 14): 'horse chestnut', 
	(11, 15): 'horse chestnut', (11, 16): 'horse chestnut', 
	(11, 17): 'horse chestnut', (11, 18): 'horse chestnut', 
	(11, 19): 'horse chestnut', (11, 20): 'horse chestnut', 
	(11, 21): 'horse chestnut', (5, 25): 'ash', (5, 26): 'ash', 
	(5, 27): 'ash', (5, 28): 'ash', (5, 29): 'ash', (5, 30): 'ash', 
	(5, 31): 'ash', (6, 1): 'ash', (6, 2): 'ash', (6, 3): 'ash', 
	(11, 22): 'ash', (11, 23): 'ash', (11, 24): 'ash', (11, 25): 'ash', 
	(11, 26): 'ash', (11, 27): 'ash', (11, 28): 'ash', (11, 29): 'ash', 
	(11, 30): 'ash', (12, 1): 'ash', (6, 24): 'birch', (9, 23): 'olive tree', 
	(12, 22): 'beech'
	}

#%%     
def get_number(prompt, rmin, rmax):
    """
	Get from the user str-type input within the given range of values.
    """
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            continue
        if value not in range(rmin, rmax + 1):
            continue
        else:
            break
    return value
 
   
def tree_search():
    """
	Call the get_nb function to collect input from the user,
	then compare it with the data dict and return the corresponding value.
        """
    global day
    global month
    global result
    day = get_number("Day: > ", 1, 31)
    month = get_number("Month: > ", 1, 12)

    result = long_data[(month, day)]
	
    print("A guardian tree for a person born on {}.{}. is {}."
		  .format(day, month, result.capitalize()))


print("Welcome to the Celtic Tree Astrology.")
print("In order to get to know your guardian tree, provide you date of birth.")
tree_search()
while True:
    print("Do you want to check it for another date?")
    again = input('(y/n) > ')
    if again == 'y':
        tree_search()
    elif again == 'n':
        input("Press enter to exit.")
        exit(0)
