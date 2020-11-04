###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename) as f:
        cow_dict = {}
        for line in f:
            """All but the last item in document has a new line marker that needs to be removed"""
            """Split cow and weight value and allocate to dictionary"""
            if "\n" in line:
                end_of_slice = len(line) - 1
                slice_line = line[0:end_of_slice]
                split_line = slice_line.split(",")
                cow_dict[split_line[0]] = int(split_line[1])
                #cow_dict[split_line[0]] = split_line[1]
            else:
                split_line = line.split(",")
                cow_dict[split_line[0]] = int(split_line[1])
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    all_trips = []
    cows_list = []
    for k, v in cows.items():
        t = k, v
        cows_list.append(t)
    cows_list.sort(key=lambda x: x[1], reverse=True)

    while cows_list:
        remaining_limit = 10
        trip = []
        for i in cows_list:
            if i[1] < remaining_limit:
                trip.append(i[0])
                remaining_limit -= i[1]
        #cannot remove cows from the cows_list in the for loop as the loop then skips the next cow
        #loop below removes cows that have been transported in the current trip from cows_list
        for i in trip:
            for c in cows_list:
                if i is c[0]:
                    cows_list.remove(c)

        all_trips.append(trip)
    return all_trips


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #TODO do this without a counter
    for partition in get_partitions(cows):
        counter = 0
        for trip in partition:
            total_weight = 0
            for i in trip:
                total_weight += cows.get(i)
            if total_weight <= limit:
                counter += 1

        if counter is len(partition):
            return partition

#cows = {'Jessie': 6, 'Maybel': 3, 'Callie': 2, 'Maggie': 5}


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    greedy = greedy_cow_transport(cows)
    end = time.time()
    print('Greedy algorithm result', greedy, '\n Greedy took', (end - start), 'seconds to run.')

    start = time.time()
    brute = brute_force_cow_transport(cows)
    end = time.time()
    print('Brute force algorithm result', brute, '\n Brute force took', (end - start), 'seconds to run.')

compare_cow_transport_algorithms()