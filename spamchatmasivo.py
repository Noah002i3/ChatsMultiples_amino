import aminofix as amino
import pyfiglet, colorama

print(colorama.Fore.GREEN)
print(pyfiglet.figlet_format("Spam", font="slant"))
print("      [Creditos] [Noah] ")

print(colorama.Fore.GREEN)
client=amino.Client()
client.login(email=input(" - Email: "), password=input(" - Contraseña: "))
comus=client.sub_clients(size=100)
for x, name in enumerate(comus.name, 1):
    print(f" -{x}.{name}")
comId = comus.comId[int(input("\nSelecciona la comunidad: ")) - 1]
sub_client=amino.SubClient(comId=comId, profile=client.profile)
chatsint=int(input(" - Chats: "))
mensaje= """texto"""



def chatsxd():
        usersIdxd=sub_client.get_online_users(start=0, size=1000).profile.userId
        userrecent = sub_client.get_all_users(start=0, size=1000, type= "recent").profile.userId
        userscomplete = [*usersIdxd, *userrecent]
        if userrecent:
            for userId in userrecent:
                for x in range(chatsint):
                    try:
                        sub_client.start_chat(userId=userscomplete, message="")
                        chats = sub_client.get_chat_threads(start=0, size=150)
                        for chatId , titulo in zip(chats.chatId, chats.title):
                            sub_client.edit_chat(chatId=chatId,title="texto",viewOnly=200, )
                            sub_client.send_message(chatId=chatId,message=mensaje)
                            print(" - Finalizado")
                    except Exception as e:
                        print(e)
                        pass
                    else:
                        break
                        
 
chatsxd()
