IMPORTANT
If you have your servers save file inside the server folder itself then this script doesnt copy it over to the new server, this script assumes that the world file is stored outside of the factorio folder
EX: if your save file is located here: "/home/user/Desktop/My-Factorio-Server/factorio/saves/my-world.zip" the server will not copy it over and you must do that yourself
if your server stores its save file outside the factorio folder like this "/home/user/Desktop/My-Factorio-Server/my-world.zip" then you should be fine


Usage

Run the script in the terminal
```
python3 PATH-TO-SCRIPT/factorio_server_updater.py
```

The script will then ask for the file path of the server, it is looking for the directory that the server is located inside of.
EX: /home/user/Desktop/My-Factorio-Server
if you put "/home/user/Desktop/My-Factorio-Server/factorio" then the script assues that the server is located inside a folder called 'factorio' and it wont work.

after the scrip confirms the file path it should just be sit back and watch, the scrip will automatically copy the old server settings, whitelist, player-data, and achievments
after that it will ask if you would like to delete the old server, i would recomend against it untill you have started your server and joined to make sure that nothing is broken or anything but in order for the script to work the old server will have to be removed or renamed to something else


Use at your own risk
