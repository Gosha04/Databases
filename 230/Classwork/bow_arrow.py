import random
import math

# Declared variables
arrows = 10
wolves = 6
wolf_dist = []
castle_height = 12
traj = 15

# Hypotenuse stuff
def hypo(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c

# Gives each wolf distance
def dist():
    for i in range(wolves):
        wolf_dist.append(random.randint(1, 15))
dist()

# Main function which only runs while there are wolves and arrows
while wolves != 0 and arrows != 0:
    # Lots of print statements for users 
    print(f"The wolves are {wolf_dist} ft away")
    # Sets which wolf is actively being target: always closest one
    min_dist = min(wolf_dist)
    wolf_index = wolf_dist.index(min_dist)
    # If the wolf has dis 0 you're dead
    if wolf_dist[wolf_index] == 0:
        break
    else:
        # All the fun math stuff to check if you can shoot the wolf
        if hypo(castle_height, wolf_dist[wolf_index]) <= traj:
            print(f"The wolf is {min_dist} ft away")
            shoot = input("Do you Shoot? (y/n)")
            # More math that checks if you hit the wolf and then the distance of all wolves afterwards
            if shoot == "y":
                arrows -= 1
                roll = random.randint(1, 10)
                if wolf_dist[wolf_index] <= 5:
                    roll += random.randint(1, 3)
                elif wolf_dist[wolf_index] <= 8:
                    roll += random.randint(1, 2)
                if roll >= 9:
                    print("You hit a wolf!")
                    wolves -= 1
                    wolf_dist.pop(wolf_index)
                    print("The wolves dodge away from their fallen comrade")
                    for i in range(len(wolf_dist)):
                        wolf_dist[i] += 1
                        if wolf_dist[i] >= 15:
                            wolf_dist[i] -= 3
                            print("The wolves will not fall back")
                # Lost conditions and stuff 
                else:
                    print("You missed...")
                    wolf_dist[wolf_index] -= 1
                    if wolf_dist[wolf_index] <= 0:
                        print("The wolves rip you to shreds")
                        break
            else:
                print("You bide your time...")
                wolf_dist[wolf_index] -= 1
                if wolf_dist[wolf_index] <= 0:
                    print("The wolves rip you to shreds")
                    break

if wolves == 0:
    print("All the wolves are dead!")
elif arrows == 0:
    print("You ran out of arrows!")
