banner = '''
 _   _ _   __ _   __                          _____ 
| | | | | / /| | / /                         /  ___|
| | | | |/ / | |/ /  ___  _ __ ___  _ __ ___ \ `--. 
| | | |    \ |    \ / _ \| '_ ` _ \| '_ ` _ \ `--. \
\ \_/ / |\  \| |\  \ (_) | | | | | | | | | | /\__/ /
 \___/\_| \_/\_| \_/\___/|_| |_| |_|_| |_| |_\____/ 
            			coded by: @foxeditor
            			 
'''
print(banner)
print('Введите все данные и будет создан файл \'nakrutka.py\', запустив его комментарии будут крутиться на ваш/не ваш пост, а вы можете попить чаек ;3\n')
token = input('Введите Ваш токен--->')
ownid = input('Введите Ваш ID--->')
psid = input('Введите ID поста--->')
num = int(input('Введите количество комментариев---->'))


f = 'nakrutka.py'
n = open(f,"w",encoding='utf-8')
n.write("""import vkbee, asyncio,time
banner = '''
 _   _ _   __ _   __                          _____ 
| | | | | / /| | / /                         /  ___|
| | | | |/ / | |/ /  ___  _ __ ___  _ __ ___ \ `--. 
| | | |    \ |    \ / _ \| '_ ` _ \| '_ ` _ \ `--. \
\ \_/ / |\  \| |\  \ (_) | | | | | | | | | | /\__/ /
 \___/\_| \_/\_| \_/\___/|_| |_| |_|_| |_| |_\____/
            			coded by: @foxeditor
            			                          
'''
print(banner)
async def main(loop):
    vk=vkbee.VkApi('"""+str(token)+"""',loop=loop)
    for i in range("""+str(num)+"""):
        comment=await vkbee.VkApi.call(vk,'wall.createComment',{'owner_id':"""+str(ownid)+""",'post_id':"""+str(psid)+""",'sticker_id':107})
        print(comment)
        time.sleep(1)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
""")
print('Скрипт для накрутки готов ;3')
