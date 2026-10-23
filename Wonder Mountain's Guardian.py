"""Wonder Mountain's Guardian: simple ride simulation."""

import random

MIN_HEIGHT = 107  # cm


class Rider:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.score = 0


class Cart:
    def __init__(self, name):
        self.name = name
        self.riders = []

    def load(self, rider):
        self.riders.append(rider)
        print(f"{self.name}: {rider.name} boarded")

    def unload(self):
        print(f"{self.name}: unloading {len(self.riders)} rider(s)")
        self.riders = []


class Ride:
    def __init__(self):
        self.cart = Cart("Cart A")
        self.leaderboard = []  # list of (score, name)

    def run_cycle(self):
        print("\nLaunch!")
        print("Chain lift to the top...")
        print("Entering the tunnel. Video and sound start!")

        for rider in self.cart.riders:
            for _ in range(3):  # 3 targets in the tunnel
                if input(f"{rider.name}, fire at the target? (y/n): ") == "y":
                    if random.random() < 0.6:
                        rider.score += 100
                        print("  Hit! +100")
                    else:
                        print("  Miss!")

        print("Stopped at the dragon. ROAR!")
        print("Vertical drop!")
        print("Driving through the leaderboard area...")

        for rider in self.cart.riders:
            self.leaderboard.append((rider.score, rider.name))
        self.leaderboard.sort(reverse=True)

        print("Returning to the station...")
        self.cart.unload()

    def show_leaderboard(self):
        print("\n--- LEADERBOARD ---")
        for place, (score, name) in enumerate(self.leaderboard[:5], 1):
            print(f"{place}. {name}: {score}")


ride = Ride()
playing = True

while playing:
    name = input("\nRider name: ")
    height = int(input("Height in cm: "))
    rider = Rider(name, height)

    if rider.height >= MIN_HEIGHT:
        ride.cart.load(rider)
        ride.run_cycle()
        ride.show_leaderboard()
    else:
        print(f"Sorry, you must be at least {MIN_HEIGHT} cm to ride.")

    playing = input("Another rider? (y/n): ") == "y"

print("Ride closed. Thanks for riding!")




