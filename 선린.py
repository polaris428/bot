import discord
import asyncio
import time 
client = discord.Client()

@client.event

async def on_ready():

    print('Logged in as')

    print(client.user.name)

    print(client.user.id)

    print('------')
    await client.change_presence(game=discord.Game(name="asdasda"))

@client.event
async def on_message(message):
    if message.content.startswith("!상태"):
        embed = discord.Embed(title="봇 상태", description="양호!!(버전:0.0.01)", color=0x00ff56) 
        embed.set_footer(text="하단 설명")
        
        await message.channel.send("봇 상태입니다", embed=embed)
   
    if message.content.startswith("!봇 정검"):
        await message.channel.send("10%")
        await message.channel.send("20%")
        time.sleep(1)
        await message.channel.send("35%")
        await message.channel.send("50%")
        time.sleep(3)
        await message.channel.send("70%")
        await message.channel.send("80%")
        await message.channel.send("99%")
        time.sleep(2)

        await message.channel.send("100%")
        embed = discord.Embed(title="봇 상태", description="양호!!(버전:0.0.01)", color=0x00ff56) 
        embed.set_footer(text="하단 설명")
        
        await message.channel.send("봇 상태입니다", embed=embed)
   
        

        
    if message.content.startswith("!정민재"):
        await message.channel.send("세상에서 제일 똑똑 하신 분이자 저를 만드신 분이죠")

    if message.content.startswith("!정지영"):
        await message.channel.send("신입생 OT에서 전교생 앞에서 손을 들어 솦과의 대범함을 전교에 알리신 분이에여")    
    
    if message.content.startswith("!현정"):
        await message.channel.send("롤창아ㅏㅏ!")  
    
    if message.content.startswith("!이종서"):
        await message.channel.send("다이에나는 필벤 입니다")

    if message.content.startswith("!박세로이"):
        await message.channel.send("ㅈㄴ잘생기신 분이져 아 물론 배우가 ^^7")        

    if message.content.startswith("!예나"):
        await message.channel.send("자야연습하세여")
    
    if message.content.startswith("안녕"):
        await message.channel.send("오랜만이에요!")


   
    if message.content.startswith( "숙제 "):
        await message.channel.send("X발 개같은거")
    
    if message.content.startswith( "싸가지 없는거"):
        await message.channel.send("힝....")    

    
    
    if message.content.startswith( "온라인 클래스" ):
        await message.channel.send("https://hoc22.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=00285&schCssTyp=online_high")    
    if message.content.startswith( "롤 "):
        await message.channel.send("op.gg")
 




client.run('NjU1Njc3MzE1OTIwOTUzMzc0.XpUQ7A.Not0UQQzWIer8edchsaqQ9V4zBk')