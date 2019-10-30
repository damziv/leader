from instabot import Bot

bot = Bot()
bot.login(username= "username", password = "password")

username = "rekan_hushyar"
user_id = bot.convert_to_user_id(username)
infodict = bot.get_user_info(user_id)
print(infodict["public_email"])