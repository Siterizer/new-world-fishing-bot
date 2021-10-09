# new-world-fishing-bot release 1.2.0

[![Demonstration](https://i.imgur.com/SLQC3oT.png)](https://www.youtube.com/watch?v=fxEKNIxCn38)
click img for demonstration

# Download guide
* Click at latest release:\
  ![alt text](https://i.imgur.com/Dj1hNl2.png)
* Download and extract bot.zip:\
  ![alt text](https://i.imgur.com/HFLQu24.png)
* When you run file bot.exe following user interface should appear:\
  ![alt text](https://i.imgur.com/G2XeHbX.png)

# Game settings
* Visuals: resolution 1920x1080, contrast/brightness default, low details:\
  ![alt text](https://i.imgur.com/VnfYTrA.png)

* Standard key bindings, **except of 'CAMERA' -> 'FREE LOOK' key binding, it must be 'B'!**\
  ![alt text](https://i.imgur.com/oGIdYhR.png)
  
  
* Remember to set you windows Scale to 100%:\
  ![alt text](https://i.imgur.com/0302u4A.png)

# Usage guide
* Before you start fishing you need to indicate correct fishing positions\
  The left ('Fishing') panel inputs are the pointing area where fishing icons are going to appear\
  The best way to configure it is to open the game, stand over the fishing ground\
  set a rectangle so that most of it is on the right side of the character, and set the appropriate height\
  ![alt text](https://i.imgur.com/4mikQR1.png)
* The smaller the rectangle, the faster the program will run - because it will have fewer pixels to check\
  I strongly suggest setting the repair/bait positions at this point as well\
  Just open the inventory, and set positions so that it completely covers the rod\
  ![alt text](https://i.imgur.com/caYEloT.png)
* Do the same, for the bait buttons\
  ![alt text](https://i.imgur.com/3NZ5tg5.png)
* Now all you have to do is click the ‘Start fishing’ button and move the mouse cursor into the game window.

# Personalization guide
* Repairing functionality will work every interval you set on the panel and is activated while searching for a fish\
  Each interval, starting with casting the fishing rod, retrieving the fish, opening the inventory for repairs, is possible to change\
  Close app, go to your installation folder, open resources and open config.xml with any text editor you have\
  ![alt text](https://i.imgur.com/0yR6nIM.png)
* As you can see there are values that you assigned a moment ago. What interests you are all the values\
  appearing after the line 'timeouts'. Each timeout will be a random number in the range of min and max.
  And their properties are listed here: (All values are given in seconds)
1. loop is responsible for the breaks between successive iterations of the program. I recommend leaving it at 0.0.1
2. notice is a left mouse click duration when fish is found
3. reeling is a left mouse click duration when the green icon is visible
4. pause tells you how much time the program should 'release' when it sees a brown or red icon
5. cast is a left mouse click duration of casting the fishing rod.
6. arm_disarm - time the program will wait before/after arming/disarming the rod
7. inventory - time the program will wait before/after opening/closing your inventory
8. repair - time the program will wait before/after clicking the fishing rod
9. confirm - time the program will wait before/after confirming repair
10. select - time the program will wait after selecting a bait
11. confirm - time the program will wait after 'Equip Bait' button
12. Additionally, if you want the program to display more information while fishing, change 'log_lvl' from INFO to DEBUG.\

# Code installation guide
* Clone repo ```git clone https://github.com/Siterizer/new-world-fishing-bot.git```
* Install python https://www.python.org/downloads/
* Create python virtual environment ```python3 -m venv instalation_directory\new-world-fishing-bot```
* Enter virtual environment ```Scripts\activate```
* Install modules: ```pip install -r requirements.txt```
* run ```python bot.py``` following user interface should appear:\
![alt text](https://i.imgur.com/Pgv97yv.png)
# If you would like to create your own .exe file:
1. Install: ```pip install pyinstaller```
2. Run following command: ```pyinstaller --add-data resources;resources bot.py```
3. Your exe file should generate in ```dist\bot\bot.exe ```
