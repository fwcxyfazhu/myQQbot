from pydoc import plain
from this import d
from tkinter import N
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
import random
# weather = on_command("weather", rule=to_me(), aliases={"天气", "天气预报"}, priority=5)


# @weather.handle()
# async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
#     plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
#     if plain_text:
#         matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


# @weather.got("city", prompt="你想查询哪个城市的天气呢？")
# async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
#     if city_name not in ["北京", "上海"]:  # 如果参数不符合要求，则提示用户重新输入
#         # 可以使用平台的 Message 类直接构造模板消息
#         await weather.reject(city.template("你想查询的城市 {city} 暂不支持，请重新输入！"))

#     city_weather = await get_weather(city_name)
#     await weather.finish(city_weather)


# # 在这里编写获取天气信息的函数
# async def get_weather(city: str) -> str:
#     return f"{city}的天气是..."
#-----------------------------------------------------------------------------#
rollPoint = on_command("roll", aliases={"r","投掷"}, priority=5)
#, rule=to_me()
@rollPoint.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("ndn", args)

@rollPoint.got("ndn",prompt="要roll几d几呢")
async def handle_ndn(ndn:Message=Arg(),ndnstr:str =ArgPlainText("ndn")):
    ndnlist=[1,100]
    try:
        ndnlist[0]=int(ndnstr.split("d")[0])
    except:
        pass
    try:
        ndnlist[1]=int(ndnstr.split("d")[1])
    except:
        pass
    # l=len(ndnData)
    # print(l)
    # if len(ndnData)!=2:
    #     await rollPoint.reject(ndn.template("你输入的{ndn}不符合格式,请重新输入！"))
    point_Roll = await getRoll(ndnlist)
    await rollPoint.finish(point_Roll)

async def getRoll(li):
    ans = 0
    for i in range(li[0]):
        ans+=random.randint(1,li[1])
    return f"{li[0]}d{li[1]}={ans}!"
    # return li