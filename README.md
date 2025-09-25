# MinePyWrapper
<p align="center">
  <img width="150" height="150" alt="MinePyWrapperLogoPlaceholder" src="https://github.com/user-attachments/assets/38e8f391-5c0e-460a-9f05-ea9bc74ebf33" />
</p>
<p align="center">MinePyWrapper is a Python wrapper for running and extending features in a Minecraft <i>Java Edition</i> server.</p>

Instead of writing full Java plugins or mods, this lets you hook into the server’s state/lifecycle events (starting, running, idle, stopping, stopped) and add custom functionality directly in Python. 
This means simple features you want to add don't require the overhead of a mod loader (fabric, forge) or a plugin loader (paper, spigot, bukkit) and you can keep the server in its vanilla form.
Of course, you can still definitely use your favorite mods or plugins if you'd like.

## 🟢 Current Features
- Console Styling 🎨: Updates the server title and color based on the server's current state.
- State Manager 🔄: A script that manages and stores the state of the server (starting, running, idle, stopping, stopped) and has an event system for other scripts to detect state changes 
- Sneaky Bans 👻: An example of how you can extend the server with custom features. Instead of banning players in the usual way (which makes it obvious),
  when they join, they get kicked with a fake error message (e.g., “Connection timed out: getsockopt”). Perfect for keeping out that one person who thinks
  that they got away with X-raying.

## 🔜 Future Features
- Google Drive Integration 💾: Let the owner log into their google account to allow the world file to be saved on the cloud when the server stops along with being able to have past backups of the world.
- Remote Panels 🌐: Allow the owner along with anyone else authorized to remotely turn on and off the server. Only the owner will be able to view logs and run commands however.

## ⬆️ Installation Guide
There is currently not a proper installation but this is it for now.
1. Inside of the folder with the server jar, create a folder named `StartScripts`
2. Clone all of the scripts into `StartScripts`
3. Edit Config.json and rename `"jar_info"/"jar_name"` to the name of the server jar (without the .jar extension).
   You can edit everything else to your liking such as the minimum ram, maximum ram, other arguments, console styles, sneaky bans, and a lot more in the future.
4. Inside of the folder with the server jar, create a `.bat` file and name it whatever you want.
5. Insert this inside of the `.bat` file and save:
   ```
   python StartScripts/Start.py
   PAUSE
   ```
6. That's it! To run the server, just run the `.bat` file.

## 📜 License
MinePyWrapper is released under the MIT License.  
Feel free to use, modify, and share.
