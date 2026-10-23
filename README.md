# Wonder-Mountain-s-Guardian-Digital-Twin
represents the digital twin for the ride Wonder Mountain's Guardian at Canada's Wonderland
Wonder Mountain's Guardian is a roller coaster dark ride hybrid where the first little bit is a roller coaster that leads to a dark ride area with interactive screens where you can shoot at bug like monsters for points which leads to the dragon or "Guardian" where it then drops the cart straight down like a dropper attraction into the score room and back to the loading and unloading station


---------------------------------------------------------------------
How to Run the Program
-
Requirements: Python 3.6 or newer. No extra libraries are needed.

Save the code as wonder_mountains_guardian_commented.py (or the simple version, wonder_mountains_guardian_simple.py).
Open a terminal in the folder that contains the file.
Run:
   python wonder_mountains_guardian_commented.py

On some systems use python3 instead of python.

Follow the prompts:
Enter the rider's name.
Enter the rider's height in cm (whole number).
If the rider is tall enough, answer y or n to "fire at the target?" for each of the 3 targets.
Answer y to "Another rider?" to continue, or anything else to close the ride.


---------------------------------------------------------------------
Class 1: Rider
-
  Purpose: Stores the information about one guest.

  Attributes

  Attribute	Type	Description
  name	string	The rider's name.
  height	integer	The rider's height in cm.
  score	integer	Points earned on the current ride. Starts at 0.

  Methods

  Method	Parameters	Returns	What it does
  __init__	name, height	nothing	The constructor. It runs when a Rider is created and sets the name, height and a starting score of 0.

Class 2: Cart
-
  Purpose: Represents the ride cart. It holds the riders and handles loading and unloading.

  Attributes

  Attribute	Type	Description
  name	string	The cart's name, such as "Cart A".
  riders	list of Rider	The riders currently aboard. Empty when the cart is in the station.

  Methods

  Method	Parameters	Returns	What it does
  __init__	name	nothing	The constructor. It sets the cart's name and starts with an empty rider list.
  load	rider	nothing	Adds the rider to the riders list and prints a boarding message. Called from the main loop after the height check passes.
  unload	none	nothing	Prints how many riders are leaving, then resets riders to an empty list. Called at the end of Ride.run_cycle().

Class 3: Ride
-
  Purpose: The controller of the program. It owns the cart and the leaderboard and runs the ride steps in the order shown in the flowchart.
  
  Attributes
  
  Attribute	Type	Description
  cart	Cart	The cart used by the ride ("Cart A"), created in the constructor.
  leaderboard	list of (score, name)	Every finished rider's score, kept sorted from highest to lowest.
  
  Methods
  
  Method	Parameters	Returns	What it does
  __init__	none	nothing	The constructor. It creates Cart("Cart A") and an empty leaderboard.
  run_cycle	none	nothing	Runs one full trip. In order: prints the launch, chain lift and tunnel messages; loops over each rider and gives 3 chances to fire (using random.random() < 0.6 for a hit, +100 points); prints the dragon stop and vertical drop; adds each rider's score to the leaderboard and sorts it; then calls cart.unload().
  show_leaderboard	none	nothing	Prints the top 5 entries of the leaderboard with their place number, name and score. Called after each ride.

  ----------------------------------------------------------------------------------------
Assumptions
-
The minimum rider height is 107 cm. This is a placeholder value, not the real ride's limit.
Each shot has a 60% chance of hitting. This is also a made-up value.
A hit is worth 100 points, and each rider gets 3 shots per ride.
Riders choose to fire by typing a lowercase y. Any other answer counts as not firing.
Only the top 5 scores are shown on the leaderboard.
The ride steps (launch, chain lift, dragon, drop) are represented by printed messages, not by a real physical simulation.

Limitations
-
One rider at a time: the cart is loaded with a single rider per cycle, and there is only one cart.
No input validation: typing letters instead of a number for height will crash the program with a ValueError. Negative or unrealistic heights are not rejected.
Case-sensitive answers: Y is not accepted as "yes". Only lowercase y works.
No saved data: the leaderboard resets every time the program is closed.
Duplicate names: two riders with the same name appear as separate leaderboard entries with nothing to tell them apart.
Rider scores reset only through new objects: each rider is created fresh, so a returning guest starts at 0 again.
Text only: there is no graphics, sound or video, even though the ride steps mention them.
