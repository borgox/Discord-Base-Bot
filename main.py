
#* CONFIG
TOKEN = "" #? es: MTObm832n3dskk2324...  - bot token, get one at: https://discord.com/developers/applications
COMMAND_PREFIX = "" #? ex: !   - command prefix (like !help)
PROXY = False #! Specify use of proxies False = No proxy True = Yes proxy
PROXYFILE = "proxies.txt" #! Don't edit this setting if you aren't using proxies
OWNER_IDS = [] #? ex: OWNER_IDS = [1234, 5678]   -IDS of bot owner
STATUS = "test"

#* IMPORTS/LIBRARIES
import datetime, random, os, ctypes, disnake
from colorama import Fore, Style
from disnake.ext import commands, tasks
from typing import Any

#* CODE

#? Utility Functions and Classes
def clear() -> None: return os.system("cls") if os.name == "nt" else os.system("clear")
def get_proxy(fp="./Data/proxies.txt") -> str: return random.choice(open(fp, "r").read().splitlines()) if random.choice(open(fp, "r").read().splitlines()) != "" else None
def title(title) -> Any: return ctypes.WinDLL("kernel32").SetConsoleTitleW(title) if os.name == "nt" else None
def abbreviate_string(s, length=15) -> str: return s[:random.randint(1, min(length, len(s) -8))] + "..." if len(s) <= length else s[:length] + "..."
def times() -> str: return f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
class Log:
    @staticmethod
    def err(msg):
        print(f'{Fore.RESET}{Style.BRIGHT}[{Fore.CYAN}{times()}{Fore.RESET}] {Fore.RESET}{Style.BRIGHT}[{Fore.LIGHTRED_EX}-{Fore.RESET}] {msg}{Fore.RESET}')

    @staticmethod
    def succ(msg):
        print(f'{Fore.RESET}{Style.BRIGHT}[{Fore.CYAN}{times()}{Fore.RESET}] {Fore.RESET}{Style.BRIGHT}[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {msg}{Fore.RESET}')

    @staticmethod
    def console(msg):
        print(f'{Fore.RESET}{Style.BRIGHT}[{Fore.CYAN}{times()}{Fore.RESET}] {Fore.RESET}{Style.BRIGHT}[{Fore.BLUE}/{Fore.RESET}] {msg}{Fore.RESET}')
    @staticmethod
    def info(msg):
        print(f'{Fore.RESET}{Style.BRIGHT}[{Fore.CYAN}{times()}{Fore.RESET}] {Fore.RESET}{Style.BRIGHT}[{Fore.YELLOW}!{Fore.RESET}] {msg}{Fore.RESET}')
class CogLoader():
    def __init__(self, bot:commands.InteractionBot):
        self.bot = bot
        self.loaded = 0
        self.not_loaded = 0
        self.LoadCogs()

    def GetData(self):
        return (self.loaded, self.not_loaded)

    def LoadCogs(self):
        if os.path.exists("./cogs"):
            for file in os.listdir("./cogs"):
                if file.endswith(".py"):
                    if file[:-3] in self.bot.cogs:
                        pass
                    else:
                        try:
                            self.bot.load_extension(f"cogs.{file[:-3]}")
                            self.loaded += 1
                        except commands.ExtensionError as e:
                            if "already" in str(e):
                                pass
                            else:
                                Log.err(f"Failed to load cog {file}: {e}")
                                self.not_loaded += 1
                        except Exception as e:
                            Log.err(f"An unexpected error occurred while loading cog {file}: {e}")
                            self.not_loaded += 1
        else:
            Log.err("The 'cogs' directory does not exist.")
            
#? Custom SubClassed bot to have a more clean and fast istance
class Bot(commands.Bot):
    def __init__(self, command_prefix, owner_ids, proxy=None, intents=disnake.Intents.all(), **kwargs):
        super().__init__(command_prefix=command_prefix, owner_ids=owner_ids, intents=intents,**kwargs)
        self.proxy = proxy
        try:
            self.status_rotator.start()
            Log.info("Status Rotator: STARTED")
        except:
            Log.err("Status Rotator: NOT STARTED")
    @tasks.loop(seconds=60)
    async def status_rotator(self):
        await self.wait_until_ready()
        try:
            s = disnake.Status.dnd
            activity = None
            if STATUS != "" and list(STATUS):
                activity = disnake.Game(name=random.choice(list(STATUS)))
            await self.change_presence(status=s, activity=activity)
        except:
            pass

    async def on_ready(self):
        if self.status_rotator.current_loop >= 0:
            
                Log.info(f"Status Rotator: {Fore.LIGHTGREEN_EX}STARTED")
        else:
            Log.err(f"Status Rotator: {Fore.RED}NOT STARTED")
        if self.proxy:
            Log.info("Using proxy: {}{}".format(Fore.LIGHTCYAN_EX, abbreviate_string(self.proxy["http"], length=35)))
        title(f"{self.user} - Logged in..")
        Log.info(f"Logged in as {Fore.BLUE}{self.user}")
        #//Log.console(f"Bot cmds: {[cmd for cmd in self.slash_commands]}")
        try:
            self.remove_command("help")
            Log.info(f"Bot: {Fore.GREEN} REMOVED{Fore.RESET} '{Fore.LIGHTMAGENTA_EX}help{Fore.RESET}' command")
        except:
            Log.err(f"Bot: {Fore.RED} NOT REMOVED {Fore.RESET} '{Fore.LIGHTMAGENTA_EX}help{Fore.RESET}' command")

#? Main Code
if PROXY != "":
    bot = Bot(owner_ids=OWNER_IDS, command_prefix=COMMAND_PREFIX)
else:
    proxy = get_proxy(fp=PROXYFILE)
    bot = Bot(command_prefix=COMMAND_PREFIX, owner_ids=OWNER_IDS, proxy={"http":f"http://{proxy}", "https":f"https://{proxy}"})

#? CLI UI and Main Code
if __name__ == '__main__':
    try:
        clear()
        title("Starting up...")
        #! Please don't remove credits :(
        txt = f"""{Fore.LIGHTYELLOW_EX}
 888888ba             dP   
 88    `8b            88   
a88aaaa8P' .d8888b. d8888P    
 88   `8b. 88'  `88   88      [{Fore.LIGHTGREEN_EX}Credits: borgo.xyz github.com/borgox{Fore.LIGHTYELLOW_EX}] 
 88    .88 88.  .88   88   
 88888888P `88888P'   dP
        """
        print(txt)
        try:
            bot.run(TOKEN)
        except disnake.errors.LoginFailure as e:
            Log.err(f"{Fore.LIGHTRED_EX}Improper token has been passed: {Fore.RESET}")
            title("Not Suppressed Error")
            input(f"{Fore.RED}Press ENTER to exit...{Fore.RESET}")
    except KeyboardInterrupt:
        Log.info("Program has been stopped.") # suppress keyboard interrupt
