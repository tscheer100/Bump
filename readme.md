# Bump Bot
## Description 
A discord bot created to remind users to bump the server 2 hours after the previous bump.
![image](https://user-images.githubusercontent.com/54217979/114446088-737e7880-9b96-11eb-809e-1e8393a5a688.png)

![image](https://user-images.githubusercontent.com/54217979/114446137-842eee80-9b96-11eb-8597-d5725d2e4a0f.png)

## Requirements:
- Python 3.X
- [Discord.py](https://pypi.org/project/discord.py/)
- [Dotenv](https://pypi.org/project/python-dotenv/)

### Adding this bot to your server:
You can find the invite link [here](https://discord.com/api/oauth2/authorize?client_id=767435275365515274&permissions=1074265152&scope=bot)

### Setting up code locally:
1) Make sure all of the requirements are met above.
2) Go through the standard git pull procedure with 

    `git clone https://github.com/tscheer100/Bump.git`
3) Once the files are pulled from ***GitHub***, check the code on lines `10` and `11`. If the bot will be on running via VSCode (not recommended) then make sure to uncomment line `11`. Otherwise, if the bot will be running via terminal, leave line `11` commented out.
![image](https://user-images.githubusercontent.com/54217979/114445753-0ff44b00-9b96-11eb-95e3-d49e0046abe5.png)

4) Next, create a file named `.env`. Open up that file to add your `DISCORD_TOKEN`. Use the image below as an example on how to format it.

    ![image](https://user-images.githubusercontent.com/54217979/114444792-e38bff00-9b94-11eb-8ec9-922b97651124.png)
    Save file end exit it.
5) If using VSCode, simply run the script by hitting the run button. Otherwise, if using terminal, type `python3 bump.py`
6) Voila! The bot is now running!
#### What I've learned from this project
- the benefits of using `asyncio` over `time.sleep`
- scratched the surface with `asyncio.lock()`