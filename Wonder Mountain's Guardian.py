#Wonder Mountain's Guardian: simple ride simulation
import random

MIN_HEIGHT = 107  # cm

# CLASS 1: Rider
# Stores the information about one person on the ride.
class Rider:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.score = 0

#CLASS 2: Cart
# Holds the riders and handles loading and unloading.
class Cart:
    def __init__(self, name):
        self.name = name
        self.riders = []

    #adds rider
    def load(self, rider):
        self.riders.append(rider)
        print(f"{self.name}: {rider.name} boarded")

    #removes rider
    def unload(self):
        print(f"{self.name}: unloading {len(self.riders)} rider(s)")
        self.riders = []

# CLASS 3: Ride
# The controller. It owns the cart and the leaderboard and runs
# the steps of the flowchart in order.
class Ride:
    def __init__(self):
        self.cart = Cart("Cart A")
        self.leaderboard = []  # list of (score, name)

    #starts ride and goes through the first steps
    def run_cycle(self):
        print("\nLaunch!")
        print("Chain lift to the top...")
        print("Entering the tunnel. Video and sound start!")

        #starts shooting section
        #60% of a hit
        for rider in self.cart.riders:
            for _ in range(3):  # 3 targets in the tunnel
                if input(f"{rider.name}, fire at the target? (y/n): ") == "y":
                    if random.random() < 0.6:
                        rider.score += 100
                        print("  Hit! +100")
                    else:
                        print("  Miss!")

        #starts final section
        print("Stopped at the dragon. ROAR!")
        print("Vertical drop!")
        print("Driving through the leaderboard area...")

        # saves each rider's final score to the leaderboard
        for rider in self.cart.riders:
            self.leaderboard.append((rider.score, rider.name))
        self.leaderboard.sort(reverse=True)

    # final step of the ride
        print("Returning to the station...")
        self.cart.unload()

    # prints out the top five scores on the leaderboard
    def show_leaderboard(self):
        print("\n--- LEADERBOARD ---")
        for place, (score, name) in enumerate(self.leaderboard[:5], 1):
            print(f"{place}. {name}: {score}")

#MAIN PROGRAM
# Creates the ride and keeps running until the user says no.

ride = Ride()
playing = True

while playing:
    # User input: collect the rider's details
    name = input("\nRider name: ")
    height = int(input("Height in cm: "))
    rider = Rider(name, height)

    #determine if rider is tall enough to ride if so then continue ride else start over
    if rider.height >= MIN_HEIGHT:
        ride.cart.load(rider)
        ride.run_cycle()
        ride.show_leaderboard()
    else:
        print(f"Sorry, you must be at least {MIN_HEIGHT} cm to ride.")

    playing = input("Another rider? (y/n): ") == "y"

print("Ride closed. Thanks for riding!")




