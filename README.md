# new-world-fishing-bot release 1.0.0 
(1.1.0 incoming in first 2 days of game release)

# Instalation guide
* Clone repo ```git clone https://github.com/Siterizer/new-world-fishing-bot.git```
* Install python https://www.python.org/downloads/
* Create python virtual enviroment ```python3 -m venv instalation_directory\new-world-fishing-bot```
* Enter virtual enviroment ```Scripts\activate```
* Install following modules:
  * ```pip install pyyaml```
  * ```pip install pywin32```
  * ```pip install numpy```
  * ```pip install opencv-python```
  * ```pip install Pillow```
* run ```python main.py``` following user interface should appear:\
![alt text](https://i.imgur.com/rRDoqSS.png)
# If you would like to create your own .exe file:
1. Install: ```pip install pyinstaller```
2. Run following command: ```pyinstaller --add-data resources;resources main.py```
3. Your exe file should generate in ```dist\main\main.exe ```
# I will create explanation video about installation\run\usage in first 2 days of the game release
