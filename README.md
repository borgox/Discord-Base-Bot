# Bot Base
This is a basic bot base for Discord bots, aimed at providing a starting point for developers to build their own bots. It includes configurations, utility functions, and a custom subclassed bot for cleaner and faster instantiation.

# Installation
-  Run `install.bat`

## Configuration
On the first lines of the main.py file there is all the config variables
```py
TOKEN = ""                # Bot token, get one at: https://discord.com/developers/applications
COMMAND_PREFIX = ""       # Command prefix (e.g., !help)
PROXY = False             # Specify use of proxies (False = No proxy, True = Use proxy)
PROXYFILE = "proxies.txt" # Proxy file path (Do not edit this setting if you aren't using proxies)
OWNER_IDS = []            # IDs of bot owner(s)
STATUS = "test"           # Bot status
```
Here configure as the program says!

## Running the bot
- After configuring everything you can run in cmd `python main.py` and then your bot will start!
  
# Credits:
- Discord: borgo.xyz
- Website: [borgoxy.xyz](https://borgoxy.xyz)
- Github: [borgox](https://github.com/borgox)