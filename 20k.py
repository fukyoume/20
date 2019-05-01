# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
print ("===============[ADMIN LOGIN]===============\n")
#aditmadzs = LineClient("","ppp12345")
#aditmadzs = LineClient("","ppp12345")
aditmadzs = LineClient("dxdxdxdx132@gmail.com","ppp12345")
print ("===============[PRO 1 LOGIN SUKSES]===============\n") 
k1 = LineClient("wfj07570@cndps.com","ppp12345")
print ("===============[PRO 2 LOGIN SUKSES]===============\n") 
k2 = LineClient("eqs30287@cndps.com","ppp12345")
print ("===============[PRO 3 LOGIN SUKSES]===============\n") 
k3 = LineClient("dxdxdxdx200@yopmail.com","ppp12345")
print ("===============[PRO 4 LOGIN SUKSES]===============\n") 
k4 = LineClient("tdu68600@cndps.com","ppp12345")
print ("===============[PRO 5 LOGIN SUKSES]===============\n") 
k5 = LineClient("lje65133@cndps.com","ppp12345")
print ("===============[PRO 6 LOGIN SUKSES]===============\n") 
k6 = LineClient("kmo37694@cndps.com","ppp12345")
print ("===============[PRO 7 LOGIN SUKSES]===============\n") 
k7 = LineClient("zwj73044@cndps.com","ppp12345")
print ("===============[PRO 8 LOGIN SUKSES]===============\n") 
k8 = LineClient("wqk19169@cndps.com","ppp12345")
print ("===============[PRO 9 LOGIN SUKSES]===============\n") 
k9 = LineClient("dxdxdxdx3000@gmail.com","ppp12345")
print ("===============[PRO 10 LOGIN SUKSES]===============\n") 
k10 = LineClient("ncb30592@cndps.com","ppp12345")
print ("===============[PRO 11 LOGIN SUKSES]===============\n") 
k11 = LineClient("pgi62524@cndps.com","ppp12345")
print ("===============[PRO 12 LOGIN SUKSES]===============\n") 
k12 = LineClient("del24008@cndps.com","ppp12345")
print ("===============[PRO 13 LOGIN SUKSES]===============\n") 
k13 = LineClient("kyk47504@cndps.com","ppp12345")
print ("===============[PRO 14 LOGIN SUKSES]===============\n") 
k14 = LineClient("voz11727@cndps.com","ppp12345")
print ("===============[PRO 15 LOGIN SUKSES]===============\n") 
k15 = LineClient("llk99507@cndps.com","ppp12345")
print ("===============[PRO 16 LOGIN SUKSES]===============\n") 
k16 = LineClient("uvr74400@cndps.com","ppp12345")
print ("===============[PRO 17 LOGIN SUKSES]===============\n") 
k17 = LineClient("whh73477@cndps.com","ppp12345")
print ("===============[PRO 18 LOGIN SUKSES]===============\n") 
k18 = LineClient("ukw54994@cndps.com","ppp12345")
print ("===============[PRO 19 LOGIN SUKSES]===============\n") 
k19 = LineClient("hzw29130@cndps.com","ppp12345")
print ("===============[PRO 20 LOGIN SUKSES]===============\n") 
k20 = LineClient("apf93958@cndps.com","ppp12345")
print ("===============[PRO GHOST LOGIN SUKSES]===============\n") 
g1 = LineClient("zws35262@cndps.com","ppp12345")
print ("==========[ MAX LOGIN BOT ]===========")

poll = LinePoll(aditmadzs)
call = aditmadzs
aditmadzsProfile = aditmadzs.getProfile()
channel = LineChannel(aditmadzs)
creator = ["ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"]
owner = ["ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"]
admin = ["ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"]
staff = ["ube7e5b15dbea0cc92f2067c04d25b1fc","ube7e5b15dbea0cc92f2067c04d25b1fc"]
mid = aditmadzs.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid
Fmid = k6.getProfile().mid
Gmid = k7.getProfile().mid
Hmid = k8.getProfile().mid
Imid = k9.getProfile().mid
Jmid = k10.getProfile().mid
Kmid = k11.getProfile().mid
Lmid = k12.getProfile().mid
Mmid = k13.getProfile().mid
Nmid = k14.getProfile().mid
Omid = k15.getProfile().mid
Pmid = k16.getProfile().mid
Qmid = k17.getProfile().mid
Rmid = k18.getProfile().mid
Smid = k19.getProfile().mid
Tmid = k20.getProfile().mid
g1MID = g1.getProfile().mid
KAC = [aditmadzs,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20]
ABC = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20]
Kicker = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid,g1MID]
Aditmadzs = admin + staff

zxcv = []
protectqr = []
protectkick = []
protectkick1 = []
protectjoin = []
protectinvite = []
protectcancel = []
protectcanceljs = []
protectantijs = []
ghost = []

welcome = []
simisimi = []

responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName
responsename6 = k6.getProfile().displayName
responsename7 = k7.getProfile().displayName
responsename8 = k8.getProfile().displayName
responsename9 = k9.getProfile().displayName
responsename10 = k10.getProfile().displayName
responsename11 = k11.getProfile().displayName
responsename12 = k12.getProfile().displayName
responsename13 = k13.getProfile().displayName
responsename14 = k14.getProfile().displayName
responsename15 = k15.getProfile().displayName
responsename16 = k16.getProfile().displayName
responsename17 = k17.getProfile().displayName
responsename18 = k18.getProfile().displayName
responsename19 = k19.getProfile().displayName
responsename20 = k20.getProfile().displayName

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

aditProfile = aditmadzs.getProfile()
myProfile["displayName"] = aditProfile.displayName
myProfile["statusMessage"] = aditProfile.statusMessage
myProfile["pictureStatus"] = aditProfile.pictureStatus

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    
with open('protectcanceljs.json', 'r') as fp:
    protectcanceljs = json.load(fp)    
with open('protectantijs.json', 'r') as fp:
    protectantijs = json.load(fp)
with open('ghost.json', 'r') as fp:
    ghost = json.load(fp)
Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k2.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k3.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k4.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention5(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k5.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention6(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k6.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention7(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k7.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMention8(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k8.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention9(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k9.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention10(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k10.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention11(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k11.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention12(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k12.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention13(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k13.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention14(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k14.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention15(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k15.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention16(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k16.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention17(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k17.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention18(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k18.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention19(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k19.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention20(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k20.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "TOTAL MENTION USER{}\n\n  [ MENTION ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ SUCCESS ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "TOTAL SIDER USER{}\nHAI ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ SUCCESS ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "TOTAL MEMBER MASUK{}\nHAI  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ SUCCESS ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "TOTAL MEMBER KELUAR{}\nBYE  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n[ SUCCESS ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = aditmadzs.getAllContactIds()
        gid = aditmadzs.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"* Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" \n* Group : "+str(len(gid))+"\n* Teman : "+str(len(teman))+"\n* Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n* Runtime : \n * "+bot
        aditmadzs.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "HELP" + "\n" + \
                  "* " + key + "Me\n" + \
                  "* " + key + "Mid\n" + \
                  "* " + key + "Bk @\n" + \
                  "* " + key + "Vk @\n" + \
                  "* " + key + "Kickban\n" + \
                  "* " + key + "Mybot\n" + \
                  "* " + key + "Status\n" + \
                  "* " + key + "Sp\n" + \
                  "* " + key + "Speed\n" + \
                  "* " + key + "Tag\n" + \
                  "* " + key + "In\n" + \
                  "* " + key + "Out\n" + \
                  "* " + key + "Bc\n" + \
                  "* " + key + "Cb\n" + \
                  "self bot by max"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "???????????????????" + "\n" + \
                  "? ????? s??? ??? ?? ??x" + "\n" + \
                  "???????????????????" + "\n" + \
                  "? ????? ????? HELP BOT ?????" + "\n" + \
                  "???????????????????" + "\n" + \
                  "? ????? " + key + "Sider\n" + \
                  "? ????? " + key + "Pesan\n" + \
                  "? ????? " + key + "Respon\n" + \
                  "? ????? " + key + "Welcome\n" + \
                  "? ????? " + key + "Leave\n" + \
                  "? ????? " + key + "Set sider:?Text?\n" + \
                  "? ????? " + key + "Set spam:?Text?\n" + \
                  "? ????? " + key + "Set pesan:?Text?\n" + \
                  "? ????? " + key + "Set respon:?Text?\n" + \
                  "? ????? " + key + "Set welcome:?Text?\n" + \
                  "? ????? " + key + "Set leave:?Text?\n" + \
                  "? ????? " + key + "Name:?Nama?\n" + \
                  "? ????? " + key + "1-20name:?Nama?\n" + \
                  "? ????? " + key + "1-20up?Kirim fotonya?\n" + \
                  "? ????? " + key + "Broadcast:?Text?\n" + \
				  "? ????? " + key + "Self?on/off?\n" + \
				  "? ????? " + key + "Leave:?Namagrup?\n" + \
                  "? ????? " + key + "Blc\n" + \
                  "? ????? " + key + "Ban:on\n" + \
                  "? ????? " + key + "Unban:on\n" + \
                  "? ????? " + key + "Ban?@?\n" + \
                  "? ????? " + key + "Unban?@?\n" + \
                  "? ????? " + key + "Talkban?@?\n" + \
                  "? ????? " + key + "Untalkban?@?\n" + \
                  "? ????? " + key + "Talkban:on\n" + \
                  "? ????? " + key + "Untalkban:on\n" + \
                  "? ????? " + key + "Banlist\n" + \
                  "? ????? " + key + "Talkbanlist\n" + \
                  "? ????? " + key + "Clearban\n" + \
                  "? ????? " + key + "Refresh\n" + \
                  "???????????????????" + "\n" + \
                  "???????????????????" + "\n" + \
                  "? ????? s??? ??? ?? ??x" + "\n" + \
                  "???????????????????"
    return helpMessage1

def helpsettings():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "???????????????????" + "\n" + \
                  "? ????? s??? ??? ?? ??x" + "\n" + \
                  "???????????????????" + "\n" + \
                  "? ?????????? HELP SETTING ?????" + "\n" + \
                  "???????????????????" + "\n" + \
                  "? ????? " + key + "Allpro?on/off?\n" + \
                  "? ????? " + key + "Mentionkick?on/off?\n" + \
                  "? ????? " + key + "Protecturl?on/off?\n" + \
                  "? ????? " + key + "Protectjoin?on/off?\n" + \
                  "? ????? " + key + "Protectkick?on/off?\n" + \
                  "? ????? " + key + "Protectkick1?on/off?\n" + \
                  "? ????? " + key + "Protectcancel?on/off?\n" + \
                  "? ????? " + key + "Protectinvite?on/off?\n" + \
                  "? ????? " + key + "G?on/off?\n" + \
                  "? ????? " + key + "Js?on/off?\n" + \
                  "? ????? " + key + "Js\n" + \
                  "? ????? " + key + "A l l\n" + \
                  "? ????? " + key + "Unsend?on/off?\n" + \
                  "? ????? " + key + "Jointicket?on/off?\n" + \
                  "? ????? " + key + "Sticker?on/off?\n" + \
                  "? ????? " + key + "Respon?on/off?\n" + \
                  "? ????? " + key + "Respongift?on/off?\n" + \
                  "? ????? " + key + "Contact?on/off?\n" + \
                  "? ????? " + key + "Read?on/off?\n" + \
                  "? ????? " + key + "Autojoin?on/off?\n" + \
                  "? ????? " + key + "Autoadd?on/off?\n" + \
                  "? ????? " + key + "Autoblock?on/off?\n" + \
                  "? ????? " + key + "Autoleave?on/off?\n" + \
                  "? ????? " + key + "Welcome?on/off?\n" + \
                  "???????????????????" + "\n" + \
                  "???????????????????" + "\n" + \
                  "? ????? s??? ??? ?? ??x" + "\n" + \
                  "???????????????????"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            aditmadzs.reissueGroupTicket(op.param1)
                            X = aditmadzs.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).updateGroup(X)
                            random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                aditmadzs.reissueGroupTicket(op.param1)
                                X = aditmadzs.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])                            
                                aditmadzs.updateGroup(X)	
                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        pass

        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        aditmadzs.leaveGroup(op.param1)
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        aditmadzs.leaveGroup(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.acceptGroupInvitation(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k2.acceptGroupInvitation(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k3.acceptGroupInvitation(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k4.acceptGroupInvitation(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k5.acceptGroupInvitation(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k6.acceptGroupInvitation(op.param1)
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k7.acceptGroupInvitation(op.param1)
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k8.acceptGroupInvitation(op.param1)
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k9.acceptGroupInvitation(op.param1)
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k10.acceptGroupInvitation(op.param1)
            if Kmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k11.acceptGroupInvitation(op.param1)
            if Lmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k12.acceptGroupInvitation(op.param1)
            if Mmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k13.acceptGroupInvitation(op.param1)
            if Nmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k14.acceptGroupInvitation(op.param1)
            if Omid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k15.acceptGroupInvitation(op.param1)
            if Pmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k16.acceptGroupInvitation(op.param1)
            if Qmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k17.acceptGroupInvitation(op.param1)
            if Rmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k18.acceptGroupInvitation(op.param1)
            if Smid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k19.acceptGroupInvitation(op.param1)
            if Tmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k20.acceptGroupInvitation(op.param1)

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                   wait["blacklist"][op.param2] = True
                   random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                   random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                G = aditmadzs.getGroup(op.param1)	
                G.preventedJoinByTicket = True		
                random.choice(ABC).updateGroup(G)
                random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        aditmadzs.sendText(op.param1, wait["message"])
                        aditmadzs.sendContact(op.param1, "uc14c3d87a1123df7c8ffa9d7402e59a2")

        if op.type == 5:
            print ("[ 5 ] NOTIFIED BLOCK CONTACT")
            if wait["autoBlock"] == True:
                aditmadzs.blockContact(op.param1)
#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                 
        if op.type == 19:
            try:
                if op.param1 in protectkick1:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    	wait["blacklist"][op.param2] = True
                    	try:
                            g1.acceptGroupInvitation(op.param1)
                            g1.inviteIntoGroup(op.param1,[op.param3])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            aditmadzs.acceptGroupInvitationByTicket(op.param1)
                    	except:
                          try:
                                G = g1.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                g1.updateGroup(G)
                                Ticket = g1.reissueGroupTicket(op.param1)
                                aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k10 .acceptGroupInvitationByTicket(op.param1,Ticket)							
                                k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k13.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                k14.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                g1.kickoutFromGroup(op.param1,[op.param2])
                                g1.leaveGroup(op.param1)
                                X = aditmadzs.getGroup(op.param1)
                                X.preventeJoinByTicket = True
                                aditmadzs.updateGroup(X)
                                ginfo = aditmadzs.getGroup(msg.to)
                                aditmadzs.inviteIntoGroup(msg.to, [g1MID])
                                contact = aditmadzs.getContact(msg._from)
                                Ticket = aditmadzs.reissueGroupTicket(op.param1)
                                wait["blacklist"][op.param2] = True
                          except:
                              try:
                              	g1.inviteIntoGroup(op.param1,[op.param3])
                              	aditmadzs.acceptGroupInvitation(op.param1)
                              	g1.kickoutFromGroup(op.param1,[op.param2])
                              except:
                              	pass
						
                if op.param3 in g1MID:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[g1MID])
                        k1.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[g1MID])
                        k1.sendMessage(op.param1,"=AntiJS Invited=")
                                   
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                            random.choice(ABC).sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = aditmadzs.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        aditmadzs.updateGroup(G)
                        invsend = 0
                        Ticket = aditmadzs.reissueGroupTicket(op.param1)
                        g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        g1.kickoutFromGroup(op.param1,[op.param2])
                        g1.leaveGroup(op.param1)
                        X = aditmadzs.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        aditmadzs.updateGroup(X)
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = k1.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            k1.updateGroup(G)
                            invsend = 0
                            Ticket = k1.reissueGroupTicket(op.param1)
                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            g1.leaveGroup(op.param1)
                            X = k1.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            k1.updateGroup(X)
                    except:
                        pass

        if op.type == 19:
            if op.param1 in protectantijs:
                if mid in op.param3:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        try:
                            g1.acceptGroupInvitation(op.param1)
                            g1.inviteIntoGroup(op.param1,[mid])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            aditmadzs.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            aditmadzs.inviteIntoGroup(op.param1,[g1MID])
                        except:
                            pass              
#===========Cancel============#

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).findAndAddContactsByMid(op.param1,[g1MID])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[g1MID])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                aditmadzs.findAndAddContactsByMid(op.param1,[g1MID])
                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                aditmadzs.inviteIntoGroup(op.param1,[g1MID])
                        except:
                            pass
                return

#-------------------------------------------------------------------------------      

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[mid])
                        aditmadzs.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[mid])
                            aditmadzs.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[mid])
                                aditmadzs.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k1.updateGroup(G)
                                    invsend = 0
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[mid])
                                        aditmadzs.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[mid])
                                            aditmadzs.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[Amid])
                        k1.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[Amid])
                            k1.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[Amid])
                                k1.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k2.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k2.updateGroup(G)
                                    invsend = 0
                                    Ticket = k2.reissueGroupTicket(op.param1)
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                    Ticket = k2.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[Amid])
                                        k1.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[Amid])
                                            k1.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[Bmid])
                        k2.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.inviteIntoGroup(op.param1,[Bmid])
                            k2.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[Bmid])
                                k2.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k3.updateGroup(G)
                                    invsend = 0
                                    Ticket = k3.reissueGroupTicket(op.param1)
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k3.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k3.updateGroup(G)
                                    Ticket = k3.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[Bmid])
                                        k2.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k7.kickoutFromGroup(op.param1,[op.param2])
                                            k7.inviteIntoGroup(op.param1,[Bmid])
                                            k2.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.inviteIntoGroup(op.param1,[Cmid])
                        k3.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.inviteIntoGroup(op.param1,[Cmid])
                            k3.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[Cmid])
                                k3.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k4.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k4.updateGroup(G)
                                    invsend = 0
                                    Ticket = k4.reissueGroupTicket(op.param1)
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k4.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k4.updateGroup(G)
                                    Ticket = k4.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[Cmid])
                                        k3.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[Cmid])
                                            k3.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
                        k5.inviteIntoGroup(op.param1,[Dmid])
                        k4.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[Dmid])
                            k4.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[Dmid])
                                k4.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k5.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k5.updateGroup(G)
                                    invsend = 0
                                    Ticket = k5.reissueGroupTicket(op.param1)
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k5.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k5.updateGroup(G)
                                    Ticket = k5.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[Dmid])
                                        k4.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[Dmid])
                                            k4.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.inviteIntoGroup(op.param1,[Emid])
                        k5.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[Emid])
                            k5.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[Emid])
                                k5.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k6.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k6.updateGroup(G)
                                    invsend = 0
                                    Ticket = k6.reissueGroupTicket(op.param1)
                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k6.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k6.updateGroup(G)
                                    Ticket = k6.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                        k9.inviteIntoGroup(op.param1,[Emid])
                                        k5.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.inviteIntoGroup(op.param1,[Emid])
                                            k5.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[Fmid])
                        k6.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[Fmid])
                            k6.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.inviteIntoGroup(op.param1,[Fmid])
                                k6.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k7.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k7.updateGroup(G)
                                    invsend = 0
                                    Ticket = k7.reissueGroupTicket(op.param1)
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k7.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k7.updateGroup(G)
                                    Ticket = k7.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[Fmid])
                                        k6.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.inviteIntoGroup(op.param1,[Fmid])
                                            k6.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[Gmid])
                        k7.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[Gmid])
                            k7.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k10.kickoutFromGroup(op.param1,[op.param2])
                                k10.inviteIntoGroup(op.param1,[Gmid])
                                k7.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k8.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k8.updateGroup(G)
                                    invsend = 0
                                    Ticket = k8.reissueGroupTicket(op.param1)
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k8.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k8.updateGroup(G)
                                    Ticket = k8.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k6.kickoutFromGroup(op.param1,[op.param2])
                                        k6.inviteIntoGroup(op.param1,[Gmid])
                                        k7.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[Gmid])
                                            k7.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.inviteIntoGroup(op.param1,[Hmid])
                        k8.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[Hmid])
                            k8.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[Hmid])
                                k8.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k9.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k9.updateGroup(G)
                                    invsend = 0
                                    Ticket = k9.reissueGroupTicket(op.param1)
                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k9.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k9.updateGroup(G)
                                    Ticket = k9.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                        k7.inviteIntoGroup(op.param1,[Hmid])
                                        k8.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[Hmid])
                                            k8.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[Imid])
                        k9.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k11.kickoutFromGroup(op.param1,[op.param2])
                            k11.inviteIntoGroup(op.param1,[Imid])
                            k9.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k12.kickoutFromGroup(op.param1,[op.param2])
                                k12.inviteIntoGroup(op.param1,[Imid])
                                k9.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k10.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k10.updateGroup(G)
                                    invsend = 0
                                    Ticket = k10.reissueGroupTicket(op.param1)
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k10.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k10.updateGroup(G)
                                    Ticket = k10.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.inviteIntoGroup(op.param1,[Imid])
                                        k9.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[Imid])
                                            k9.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.inviteIntoGroup(op.param1,[Jmid])
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.cancelGroupInvitation(op.param1,[op.param2])
                        k10.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k8.inviteIntoGroup(op.param1,[Jmid])
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.cancelGroupInvitation(op.param1,[op.param2])
                            k10.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k7.inviteIntoGroup(op.param1,[Jmid])
                                k7.kickoutFromGroup(op.param1,[op.param2]) 
                                k7.cancelGroupInvitation(op.param1,[op.param2])
                                k10.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k1.updateGroup(G)
                                    invsend = 0
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.inviteIntoGroup(op.param1,[Jmid])
                                        k10.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[Jmid])
                                            k10.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Kmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k12.kickoutFromGroup(op.param1,[op.param2])
                        k12.inviteIntoGroup(op.param1,[Kmid])
                        k11.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k13.kickoutFromGroup(op.param1,[op.param2])
                            k13.inviteIntoGroup(op.param1,[Kmid])
                            k11.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k14.kickoutFromGroup(op.param1,[op.param2])
                                k14.inviteIntoGroup(op.param1,[Kmid])
                                k11.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k12.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k12.updateGroup(G)
                                    invsend = 0
                                    Ticket = k12.reissueGroupTicket(op.param1)
                                    k12.kickoutFromGroup(op.param1,[op.param2])
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k12.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k12.updateGroup(G)
                                    Ticket = k12.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                        k15.inviteIntoGroup(op.param1,[Kmid])
                                        k11.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                            k16.inviteIntoGroup(op.param1,[Kmid])
                                            k11.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Lmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k13.kickoutFromGroup(op.param1,[op.param2])
                        k13.inviteIntoGroup(op.param1,[Lmid])
                        k12.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k14.kickoutFromGroup(op.param1,[op.param2])
                            k14.inviteIntoGroup(op.param1,[Lmid])
                            k12.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[Lmid])
                                k12.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k13.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k13.updateGroup(G)
                                    invsend = 0
                                    Ticket = k13.reissueGroupTicket(op.param1)
                                    k13.kickoutFromGroup(op.param1,[op.param2])
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k13.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k13.updateGroup(G)
                                    Ticket = k13.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                        k15.inviteIntoGroup(op.param1,[Lmid])
                                        k12.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k17.kickoutFromGroup(op.param1,[op.param2])
                                            k17.inviteIntoGroup(op.param1,[Lmid])
                                            k12.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Mmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k14.kickoutFromGroup(op.param1,[op.param2])
                        k14.inviteIntoGroup(op.param1,[Mmid])
                        k13.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k15.kickoutFromGroup(op.param1,[op.param2])
                            k15.inviteIntoGroup(op.param1,[Mmid])
                            k13.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[Mmid])
                                k13.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k14.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k14.updateGroup(G)
                                    invsend = 0
                                    Ticket = k14.reissueGroupTicket(op.param1)
                                    k14.kickoutFromGroup(op.param1,[op.param2])
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k14.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k14.updateGroup(G)
                                    Ticket = k14.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k12.kickoutFromGroup(op.param1,[op.param2])
                                        k12inviteIntoGroup(op.param1,[Mmid])
                                        k13.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                            k16.inviteIntoGroup(op.param1,[Mmid])
                                            k13.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Nmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k15.kickoutFromGroup(op.param1,[op.param2])
                        k15.inviteIntoGroup(op.param1,[Nmid])
                        k14.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k13.kickoutFromGroup(op.param1,[op.param2])
                            k13.inviteIntoGroup(op.param1,[Nmid])
                            k14.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k11.kickoutFromGroup(op.param1,[op.param2])
                                k11.inviteIntoGroup(op.param1,[Nmid])
                                k14.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k15.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k15.updateGroup(G)
                                    invsend = 0
                                    Ticket = k15.reissueGroupTicket(op.param1)
                                    k15.kickoutFromGroup(op.param1,[op.param2])
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k15.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k15.updateGroup(G)
                                    Ticket = k15.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k15.kickoutFromGroup(op.param1,[op.param2])
                                        k15.inviteIntoGroup(op.param1,[Nmid])
                                        k14.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k16.kickoutFromGroup(op.param1,[op.param2])
                                            k16.inviteIntoGroup(op.param1,[Nmid])
                                            k14.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Omid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k16.kickoutFromGroup(op.param1,[op.param2])
                        k16.inviteIntoGroup(op.param1,[Omid])
                        k15.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k17.kickoutFromGroup(op.param1,[op.param2])
                            k17.inviteIntoGroup(op.param1,[Omid])
                            k15.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k18.kickoutFromGroup(op.param1,[op.param2])
                                k18.inviteIntoGroup(op.param1,[Omid])
                                k15.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k16.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k16.updateGroup(G)
                                    invsend = 0
                                    Ticket = k16.reissueGroupTicket(op.param1)
                                    k16.kickoutFromGroup(op.param1,[op.param2])
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k16.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k16.updateGroup(G)
                                    Ticket = k16.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k19.kickoutFromGroup(op.param1,[op.param2])
                                        k19.inviteIntoGroup(op.param1,[Omid])
                                        k15.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                            k20.inviteIntoGroup(op.param1,[Omid])
                                            k15.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Pmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k17.kickoutFromGroup(op.param1,[op.param2])
                        k17.inviteIntoGroup(op.param1,[Pmid])
                        k16.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k18.kickoutFromGroup(op.param1,[op.param2])
                            k18.inviteIntoGroup(op.param1,[Pmid])
                            k16.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k19.kickoutFromGroup(op.param1,[op.param2])
                                k19.inviteIntoGroup(op.param1,[Pmid])
                                k16.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k17.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k17.updateGroup(G)
                                    invsend = 0
                                    Ticket = k17.reissueGroupTicket(op.param1)
                                    k17.kickoutFromGroup(op.param1,[op.param2])
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k17.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k17.updateGroup(G)
                                    Ticket = k17.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k14.kickoutFromGroup(op.param1,[op.param2])
                                        k14.inviteIntoGroup(op.param1,[Pmid])
                                        k16.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k20.kickoutFromGroup(op.param1,[op.param2])
                                            k20.inviteIntoGroup(op.param1,[Pmid])
                                            k16.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Qmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k18.kickoutFromGroup(op.param1,[op.param2])
                        k18.inviteIntoGroup(op.param1,[Qmid])
                        k17.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k19.kickoutFromGroup(op.param1,[op.param2])
                            k19.inviteIntoGroup(op.param1,[Qmid])
                            k17.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k20.kickoutFromGroup(op.param1,[op.param2])
                                k20.inviteIntoGroup(op.param1,[Qmid])
                                k17.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k18.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k18.updateGroup(G)
                                    invsend = 0
                                    Ticket = k18.reissueGroupTicket(op.param1)
                                    k18.kickoutFromGroup(op.param1,[op.param2])
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k18.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k18.updateGroup(G)
                                    Ticket = k18.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k16.kickoutFromGroup(op.param1,[op.param2])
                                        k16.inviteIntoGroup(op.param1,[Qmid])
                                        k17.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                            k15.inviteIntoGroup(op.param1,[Qmid])
                                            k17.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Rmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k19.kickoutFromGroup(op.param1,[op.param2])
                        k19.inviteIntoGroup(op.param1,[Rmid])
                        k18.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k20.kickoutFromGroup(op.param1,[op.param2])
                            k20.inviteIntoGroup(op.param1,[Rmid])
                            k18.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k16.kickoutFromGroup(op.param1,[op.param2])
                                k16.inviteIntoGroup(op.param1,[Rmid])
                                k18.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k19.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k19.updateGroup(G)
                                    invsend = 0
                                    Ticket = k19.reissueGroupTicket(op.param1)
                                    k19.kickoutFromGroup(op.param1,[op.param2])
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k19.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k19.updateGroup(G)
                                    Ticket = k19.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k17.kickoutFromGroup(op.param1,[op.param2])
                                        k17.inviteIntoGroup(op.param1,[Rmid])
                                        k18.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k13.kickoutFromGroup(op.param1,[op.param2])
                                            k13.inviteIntoGroup(op.param1,[Rmid])
                                            k18.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Smid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k20.kickoutFromGroup(op.param1,[op.param2])
                        k20.inviteIntoGroup(op.param1,[Smid])
                        k19.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k16.kickoutFromGroup(op.param1,[op.param2])
                            k16.inviteIntoGroup(op.param1,[Smid])
                            k19.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k17.kickoutFromGroup(op.param1,[op.param2])
                                k17.inviteIntoGroup(op.param1,[Smid])
                                k19.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k20.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k20.updateGroup(G)
                                    invsend = 0
                                    Ticket = k20.reissueGroupTicket(op.param1)
                                    k20.kickoutFromGroup(op.param1,[op.param2])
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k20.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k20.updateGroup(G)
                                    Ticket = k20.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k18.kickoutFromGroup(op.param1,[op.param2])
                                        k18.inviteIntoGroup(op.param1,[Smid])
                                        k19.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k12.kickoutFromGroup(op.param1,[op.param2])
                                            k12.inviteIntoGroup(op.param1,[Smid])
                                            k19.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Tmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[Tmid])
                        k20.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            k12.kickoutFromGroup(op.param1,[op.param2])
                            k12.inviteIntoGroup(op.param1,[Tmid])
                            k20.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                k15.kickoutFromGroup(op.param1,[op.param2])
                                k15.inviteIntoGroup(op.param1,[Tmid])
                                k20.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k1.updateGroup(G)
                                    invsend = 0
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k20.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k11.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k12.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k13.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k14.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k15.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k16.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k17.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k18.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k19.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = aditmadzs.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    aditmadzs.updateGroup(G)
                                    Ticket = aditmadzs.reissueGroupTicket(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        k13.kickoutFromGroup(op.param1,[op.param2])
                                        k13.inviteIntoGroup(op.param1,[Tmid])
                                        k20.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            k15.kickoutFromGroup(op.param1,[op.param2])
                                            k15.inviteIntoGroup(op.param1,[Tmid])
                                            k20.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Bots in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).findAndAddContactsByMid(op.param1,Bots)
                        random.choice(ABC).inviteIntoGroup(op.param1,Bots)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ABC).findAndAddContactsByMid(op.param1,Bots)
                            random.choice(ABC).inviteIntoGroup(op.param1,Bots)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.choice(ABC).findAndAddContactsByMid(op.param1,Bots)
                                random.choice(ABC).inviteIntoGroup(op.param1,Bots)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                        random.choice(ABC).inviteIntoGroup(op.param1,admin)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                            random.choice(ABC).inviteIntoGroup(op.param1,admin)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                aditmadzs.findAndAddContactsByMid(op.param1,admin)
                                aditmadzs.inviteIntoGroup(op.param1,admin)
                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ADITMADZSreadPoint"]:
                   if op.param2 in Setmain["ADITMADZSreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ADITMADZSreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = aditmadzs.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = aditmadzs.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "SELFBOT BY MAX\nPENGIRIM : "
                                ret_ = "- NAMA GRUP : {}".format(str(ginfo.name))
                                ret_ += "\n- WAKTU NGIRIM : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Aditmadzs.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Aditmadzs.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "PESAN DIHAPUS\n"
                                ret_ += "- PENGIRIM : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n- NAMA GRUP : {}".format(str(ginfo.name))
                                ret_ += "\n- WAKTU NGIRIM : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n- PESANNYA : {}".format(str(msg_dict[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "STICKER DIHAPUS\n"
                                ret_ += "- PENGIRIM : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n- NAMA GRUP : {}".format(str(ginfo.name))
                                ret_ += "\n- WAKTU NGIRIM : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               aditmadzs.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])

               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, wait["Respontag"])
                           aditmadzs.sendMessage(msg.to, None, contentMetadata={"STKID":"21715710","STKPKGID":"9662","STKVER":"2"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           aditmadzs.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           aditmadzs.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, "Jangan tag saya....")
                           aditmadzs.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"Cek ID Sticker\n STKID : " + msg.contentMetadata["STKID"] + "\n STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n STKVER : " + msg.contentMetadata["STKVER"]+ "\n\nLink Sticker" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"NAMA : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nSTATUS : " + contact.statusMessage + "\nPICTURE URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = aditmadzs.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nSticker Info"
                   ret_ += "\n Sticker ID : {}".format(stk_id)
                   ret_ += "\n Sticker Version : {}".format(stk_ver)
                   ret_ += "\n Sticker Package : {}".format(pkg_id)
                   ret_ += "\n Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = aditmadzs.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)
#===========ADD BOT============#
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan anggota Aditmadzs BOT")
#===========ADD STAFF============#
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan staff")
#===========ADD ADMIN============#
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan admin")
#===========ADD BLACKLIST============#
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = aditmadzs.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            aditmadzs.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = aditmadzs.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     aditmadzs.updateGroupPicture(msg.to, path)
                     aditmadzs.sendMessage(msg.to, "Berhasil mengubah foto group")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ADITMADZSfoto"]:
                            path = aditmadzs.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][mid]
                            aditmadzs.updateProfilePicture(path)
                            aditmadzs.sendMessage(msg.to,"Foto berhasil dirubah")
               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ADITMADZSfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Amid]
                            k1.updateProfilePicture(path)
                            k1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ADITMADZSfoto"]:
                            path = k2.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Bmid]
                            k2.updateProfilePicture(path)
                            k2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ADITMADZSfoto"]:
                            path = k3.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Cmid]
                            k3.updateProfilePicture(path)
                            k3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ADITMADZSfoto"]:
                            path = k4.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Dmid]
                            k4.updateProfilePicture(path)
                            k4.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["ADITMADZSfoto"]:
                            path = k5.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Emid]
                            k5.updateProfilePicture(path)
                            k5.sendMessage(msg.to,"Foto berhasil dirubah")			
                        elif Fmid in Setmain["ADITMADZSfoto"]:
                            path = k6.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Fmid]
                            k6.updateProfilePicture(path)
                            k6.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["ADITMADZSfoto"]:
                            path = k7.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Gmid]
                            k7.updateProfilePicture(path)
                            k7.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["ADITMADZSfoto"]:
                            path = k8.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Hmid]
                            k8.updateProfilePicture(path)
                            k8.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Imid in Setmain["ADITMADZSfoto"]:
                            path = k9.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Imid]
                            k9.updateProfilePicture(path)
                            k9.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["ADITMADZSfoto"]:
                            path = k10.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Jmid]
                            k10.updateProfilePicture(path)
                            k10.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Kmid in Setmain["ADITMADZSfoto"]:
                            path = k11.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Kmid]
                            k11.updateProfilePicture(path)
                            k11.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Lmid in Setmain["ADITMADZSfoto"]:
                            path = k12.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Lmid]
                            k12.updateProfilePicture(path)
                            k12.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Mmid in Setmain["ADITMADZSfoto"]:
                            path = k13.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Mmid]
                            k13.updateProfilePicture(path)
                            k13.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Nmid in Setmain["ADITMADZSfoto"]:
                            path = k14.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Nmid]
                            k14.updateProfilePicture(path)
                            k14.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Omid in Setmain["ADITMADZSfoto"]:
                            path = k15.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Omid]
                            k15.updateProfilePicture(path)
                            k15.sendMessage(msg.to,"Foto berhasil dirubah")			
                        elif Pmid in Setmain["ADITMADZSfoto"]:
                            path = k16.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Pmid]
                            k16.updateProfilePicture(path)
                            k16.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Qmid in Setmain["ADITMADZSfoto"]:
                            path = k17.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Qmid]
                            k17.updateProfilePicture(path)
                            k17.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Rmid in Setmain["ADITMADZSfoto"]:
                            path = k18.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Rmid]
                            k18.updateProfilePicture(path)
                            k18.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Smid in Setmain["ADITMADZSfoto"]:
                            path = k19.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Smid]
                            k19.updateProfilePicture(path)
                            k19.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Tmid in Setmain["ADITMADZSfoto"]:
                            path = k20.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Tmid]
                            k20.updateProfilePicture(path)
                            k20.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif g1MID in Setmain["ADITMADZSfoto"]:
                            path = g1.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][g1MID]
                            g1.updateProfilePicture(path)
                            g1.sendMessage(msg.to,"Foto berhasil dirubah")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = k1.downloadObjectMsg(msg_id)
                     path2 = k2.downloadObjectMsg(msg_id)
                     path3 = k3.downloadObjectMsg(msg_id)	
                     path4 = k4.downloadObjectMsg(msg_id)
                     path5 = k5.downloadObjectMsg(msg_id)	
                     path6 = k6.downloadObjectMsg(msg_id)
                     path7 = k7.downloadObjectMsg(msg_id)
                     path8 = k8.downloadObjectMsg(msg_id)
                     path9 = k9.downloadObjectMsg(msg_id)
                     path10 = k10.downloadObjectMsg(msg_id)
                     path11 = k11.downloadObjectMsg(msg_id)
                     path12 = k12.downloadObjectMsg(msg_id)
                     path13 = k13.downloadObjectMsg(msg_id)	
                     path14 = k14.downloadObjectMsg(msg_id)
                     path15 = k15.downloadObjectMsg(msg_id)	
                     path16 = k16.downloadObjectMsg(msg_id)
                     path17 = k17.downloadObjectMsg(msg_id)
                     path18 = k18.downloadObjectMsg(msg_id)
                     path19 = k19.downloadObjectMsg(msg_id)
                     path20 = k20.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     k1.updateProfilePicture(path1)
                     k1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k2.updateProfilePicture(path2)
                     k2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k3.updateProfilePicture(path3)
                     k3.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k4.updateProfilePicture(path4)
                     k4.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k5.updateProfilePicture(path5)
                     k5.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k6.updateProfilePicture(path6)
                     k6.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k7.updateProfilePicture(path7)
                     k7.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k8.updateProfilePicture(path8)
                     k8.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k9.updateProfilePicture(path9)
                     k9.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k10.updateProfilePicture(path10)
                     k10.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k11.updateProfilePicture(path1)
                     k11.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k12.updateProfilePicture(path2)
                     k12.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k13.updateProfilePicture(path3)
                     k13.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k14.updateProfilePicture(path4)
                     k14.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k15.updateProfilePicture(path5)
                     k15.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k16.updateProfilePicture(path6)
                     k16.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k17.updateProfilePicture(path7)
                     k17.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k18.updateProfilePicture(path8)
                     k18.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k19.updateProfilePicture(path9)
                     k19.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k20.updateProfilePicture(path10)
                     k20.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if wait["autoRead"] == True:
                        aditmadzs.sendChatChecked(msg.to, msg_id)
                        k1.sendChatChecked(msg.to, msg_id)
                        k2.sendChatChecked(msg.to, msg_id)
                        k3.sendChatChecked(msg.to, msg_id)
                        k4.sendChatChecked(msg.to, msg_id)
                        k5.sendChatChecked(msg.to, msg_id)
                        k6.sendChatChecked(msg.to, msg_id)
                        k7.sendChatChecked(msg.to, msg_id)
                        k8.sendChatChecked(msg.to, msg_id)
                        k9.sendChatChecked(msg.to, msg_id)
                        k10.sendChatChecked(msg.to, msg_id)
                        k11.sendChatChecked(msg.to, msg_id)
                        k12.sendChatChecked(msg.to, msg_id)
                        k13.sendChatChecked(msg.to, msg_id)
                        k14.sendChatChecked(msg.to, msg_id)
                        k15.sendChatChecked(msg.to, msg_id)
                        k16.sendChatChecked(msg.to, msg_id)
                        k17.sendChatChecked(msg.to, msg_id)
                        k18.sendChatChecked(msg.to, msg_id)
                        k19.sendChatChecked(msg.to, msg_id)
                        k20.sendChatChecked(msg.to, msg_id)
                        g1.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "key":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage = help()
                                ryan = aditmadzs.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "? s?????? ?? ??x ?\n? ?s?? : "
                                ret_ = str(helpMessage)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendReplyMessage(msg_id, to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "key2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage1 = helpbot()
                                ryan = aditmadzs.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "? s?????? ?? ??x ?\n? ?s?? : "
                                ret_ = str(helpMessage1)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendReplyMessage(msg_id, to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                                            
                        elif cmd == "key3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage2 = helpsettings()
                                ryan = aditmadzs.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "? s?????? ?? ??x ?\n? ?s?? : "
                                ret_ = str(helpMessage2)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendReplyMessage(msg_id, to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                aditmadzs.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                aditmadzs.sendMessage(msg.to, "Selfbot dinonaktifkan")

                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "========================\n               S T A T U S\n========================\n"
                                if wait["unsend"] == True: md+="UNSEND - [ ON ]\n"
                                else: md+="UNSEND - [ OFF ]\n"
                                if wait["Mentionkick"] == True: md+="MENTIONKICK - [ ON ]\n"
                                else: md+="MENTIONKICK - [ OFF ]\n"
                                if wait["Mentiongift"] == True: md+="MENTIONGIFT - [ ON ]\n"
                                else: md+="MENTIONGIFT - [ OFF ]\n"
                                if wait["detectMention"] == True: md+="RESPON - [ ON ]\n"
                                else: md+="RESPON - [ OFF ]\n"                   
                                if wait["autoJoin"] == True: md+="AUTOJOIN - [ ON ]\n"
                                else: md+="AUTOJOIN - [ OFF ]\n"
                                if settings["autoJoinTicket"] == True: md+="JOINTICKET - [ ON ]\n"
                                else: md+="JOINTICKET - [ OFF ]\n"                                
                                if wait["autoAdd"] == True: md+="AUTOADD - [ ON ]\n"
                                else: md+="AUTOADD - [ OFF ]\n"                   
                                if wait["autoBlock"] == True: md+="AUTOBLOCK - [ ON ]\n"
                                else: md+="AUTOBLOCK - [ OFF ]\n"
                                if msg.to in welcome: md+="WELCOME - [ ON ]\n"
                                else: md+="WELCOME - [ OFF ]\n"                 
                                if wait["autoLeave"] == True: md+="AUTOLEAVE - [ ON ]\n"
                                else: md+="AUTOLEAVE - [ OFF ]\n"
                                if msg.to in protectqr: md+="PROTECTURL - [ ON ]\n"
                                else: md+="PROTECTURL - [ OFF ]\n"
                                if msg.to in protectjoin: md+="PROTECTJOIN - [ ON ]\n"
                                else: md+="PROTECTJOIN - [ OFF ]\n"
                                if msg.to in protectkick: md+="PROTECTKICK - [ ON ]\n"
                                else: md+="PROTECTKICK - [ OFF ]\n"
                                if msg.to in protectkick1: md+="PROTECTKICK1 - [ ON ]\n"
                                else: md+="PROTECTKICK1 - [ OFF ]\n"
                                if msg.to in protectcancel: md+="PROTECTCANCEL - [ ON ]\n"
                                else: md+="PROTECTCANCEL - [ OFF ]\n"
                                if msg.to in protectinvite: md+="PROTECTINVITE - [ ON ]\n"
                                else: md+="PROTECTINVITE - [ OFF ]\n"
                                if msg.to in protectantijs: md+="JS - [ ON ]\n"
                                else: md+="JS - [ OFF ]\n"  
                                if msg.to in ghost: md+="GHOST - [ ON ]\n"
                                else: md+="GHOST - [ OFF ]\n"
                                aditmadzs.sendReplyMessage(msg.id, to, md+"========================\nTANGGAL : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJAM [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n========================")
     
                        elif text.lower() == "all":
                            if msg._from in admin:
                                gs = ki.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for b in Bots:
                                    if b in targets:
                                        try:
                                            targets.remove(b)
                                        except:
                                            pass
                                aditmadzs.sendText(msg.to,"Leave this group.")
                                for target in targets:
                                    try:
                                        klist = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20]
                                        kicker = random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                    except:
                                        pass 

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                aditmadzs.sendMessage(msg.to,"CREATOR BOT") 
                                ma = ""
                                for i in creator:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "SelfBOT 20 Assist\n")
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                  
                        elif cmd == "me":
                          if msg._from in admin:
                            if msg.toType == 0:
                                aditmadzs.generateReplyMessage(msg.id)
                                aditmadzs.sendReplyMessage(msg_id, to, aditmadzs.getContact(sender).displayName, contentMetadata = {'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(to).pictureStatus, 'MSG_SENDER_NAME': aditmadzs.getContact(to).displayName, 'previewUrl': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~max_pv', 'type': 'mt', 'subText': ""+aditmadzs.getContact(sender).statusMessage, 'a-installUrl': 'https://line.me/ti/p/~max_pv', 'a-installUrl': ' https://line.me/ti/p/~max_pv', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~max_pv', 'i-linkUri': 'https://line.me/ti/p/~max_pv', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~max_pv'}, contentType=19)
                            else:
                                aditmadzs.sendReplyMessage(msg_id, to, aditmadzs.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~'+aditmadzs.getProfile().userid, 'type': 'mt', 'subText': ""+aditmadzs.getContact(sender).statusMessage, 'a-installUrl': 'https://line.me/ti/p/~max_pv', 'a-installUrl': ' https://line.me/ti/p/~max_pv', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~max_pv', 'i-linkUri': 'https://line.me/ti/p/~max_pv', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~max_pv'}, contentType=19)

                        elif cmd == 'me1':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               aditmadzs.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': msg._from}, contentType=13)
                               path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath

                        elif cmd == 'gift':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               aditmadzs.generateReplyMessage(msg.id)
                               aditmadzs.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '6'}, contentType=9)   
                               k1.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '1'}, contentType=9)   
                               k2.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '2'}, contentType=9)   
                               k3.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   
                               k4.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '4'}, contentType=9)   
                               k5.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)   
                               k6.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '4'}, contentType=9)   
                               k7.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   
                               k8.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '1'}, contentType=9)   
                               k9.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '2'}, contentType=9)   
                               k10.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   
                               k11.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '1'}, contentType=9)   
                               k12.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '2'}, contentType=9)   
                               k13.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   
                               k14.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '4'}, contentType=9)   
                               k15.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)   
                               k16.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '4'}, contentType=9)   
                               k17.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   
                               k18.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '1'}, contentType=9)   
                               k19.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '2'}, contentType=9)   
                               k20.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   

                        elif cmd  == "mid all":
                          if msg._from in admin:
                              aditmadzs.sendReplyMessage(msg_id, to,mid)
                              k1.sendReplyMessage(msg_id, to,Amid)
                              k2.sendReplyMessage(msg_id, to,Bmid)
                              k3.sendReplyMessage(msg_id, to,Cmid)
                              k4.sendReplyMessage(msg_id, to,Dmid)
                              k5.sendReplyMessage(msg_id, to,Emid)
                              k6.sendReplyMessage(msg_id, to,Fmid)
                              k7.sendReplyMessage(msg_id, to,Gmid)
                              k8.sendReplyMessage(msg_id, to,Hmid)
                              k9.sendReplyMessage(msg_id, to,Imid)
                              k10.sendReplyMessage(msg_id, to,Jmid)
                              k11.sendReplyMessage(msg_id, to,Kmid)
                              k12.sendReplyMessage(msg_id, to,Lmid)
                              k13.sendReplyMessage(msg_id, to,Mmid)
                              k14.sendReplyMessage(msg_id, to,Nmid)
                              k15.sendReplyMessage(msg_id, to,Omid)
                              k16.sendReplyMessage(msg_id, to,Pmid)
                              k17.sendReplyMessage(msg_id, to,Qmid)
                              k18.sendReplyMessage(msg_id, to,Rmid)
                              k19.sendReplyMessage(msg_id, to,Smid)
                              k20.sendReplyMessage(msg_id, to,Tmid)

                        elif text.lower() == "mid":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "NAME : "+str(mi.displayName)+"\nMID : " +key1)
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "NAME : "+str(mi.displayName)+"\nMID : " +key1+"\nSTATUS : "+str(mi.statusMessage))
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(aditmadzs.getContact(key1)):
                                   aditmadzs.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               aditmadzs.sendMessage1(msg)							   
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Kmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Lmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Mmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Nmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Omid}
                               aditmadzs.sendMessage1(msg)							   
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Pmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Qmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Rmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Smid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Tmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': g1MID}
                               aditmadzs.sendMessage1(msg)	

                        elif text.lower() == "!chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   aditmadzs.removeAllMessages(op.param2)
                                   aditmadzs.sendMessage(msg.to,"Chat dibersihkan")
                               except:
                                   pass

                        elif text.lower() == "!remove":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   k1.removeAllMessages(op.param2)
                                   k1.sendMessage(msg.to,"Chat dibersihkan")
                                   k2.removeAllMessages(op.param2)
                                   k2.sendMessage(msg.to,"Chat dibersihkan")
                                   k3.removeAllMessages(op.param2)
                                   k3.sendMessage(msg.to,"Chat dibersihkan")
                                   k4.removeAllMessages(op.param2)
                                   k4.sendMessage(msg.to,"Chat dibersihkan")
                                   k5.removeAllMessages(op.param2)
                                   k5.sendMessage(msg.to,"Chat dibersihkan")
                                   k6.removeAllMessages(op.param2)	
                                   k6.sendMessage(msg.to,"Chat dibersihkan")
                                   k7.removeAllMessages(op.param2)	
                                   k7.sendMessage(msg.to,"Chat dibersihkan")
                                   k8.removeAllMessages(op.param2)	
                                   k8.sendMessage(msg.to,"Chat dibersihkan")
                                   k9.removeAllMessages(op.param2)	
                                   k9.sendMessage(msg.to,"Chat dibersihkan")
                                   k10.removeAllMessages(op.param2)	
                                   k10.sendMessage(msg.to,"Chat dibersihkan")
                                   k11.removeAllMessages(op.param2)
                                   k11.sendMessage(msg.to,"Chat dibersihkan")
                                   k12.removeAllMessages(op.param2)
                                   k12.sendMessage(msg.to,"Chat dibersihkan")
                                   k13.removeAllMessages(op.param2)
                                   k13.sendMessage(msg.to,"Chat dibersihkan")
                                   k14.removeAllMessages(op.param2)
                                   k14.sendMessage(msg.to,"Chat dibersihkan")
                                   k15.removeAllMessages(op.param2)
                                   k15.sendMessage(msg.to,"Chat dibersihkan")
                                   k16.removeAllMessages(op.param2)	
                                   k16.sendMessage(msg.to,"Chat dibersihkan")
                                   k17.removeAllMessages(op.param2)	
                                   k17.sendMessage(msg.to,"Chat dibersihkan")
                                   k18.removeAllMessages(op.param2)	
                                   k18.sendMessage(msg.to,"Chat dibersihkan")
                                   k19.removeAllMessages(op.param2)	
                                   k19.sendMessage(msg.to,"Chat dibersihkan")
                                   k20.removeAllMessages(op.param2)	
                                   k20.sendMessage(msg.to,"Chat dibersihkan")
                                   g1.removeAllMessages(op.param2)	
                                   aditmadzs.sendMessage(msg.to,"Chat dibersihkan")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = aditmadzs.getGroupIdsJoined()
                               for group in saya:
                                   aditmadzs.sendMessage(group,"=======[ BROADCAST ]=======\n\n"+pesan+"\n\nCreator : line.me/ti/p/~adit_cmct")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               aditmadzs.sendMessage(msg.to, "RESTART SUKSES BOS!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Bot sudah berfungsi " +waktu(eltime)
                               aditmadzs.sendMessage(msg.to,bot)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = aditmadzs.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                aditmadzs.sendMessage(msg.to, "Grup Info\n\n Nama Group : {}".format(G.name)+ "\n ID Group : {}".format(G.id)+ "\n Pembuat : {}".format(G.creator.displayName)+ "\n Waktu Dibuat : {}".format(str(timeCreated))+ "\n Jumlah Member : {}".format(str(len(G.members)))+ "\n Jumlah Pending : {}".format(gPending)+ "\n Group Qr : {}".format(gQr)+ "\n Group Ticket : {}".format(gTicket))
                                aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "Grup Info\n"
                                ret_ += "\n Name : {}".format(G.name)
                                ret_ += "\n ID : {}".format(G.id)
                                ret_ += "\n Creator : {}".format(gCreator)
                                ret_ += "\n Created Time : {}".format(str(timeCreated))
                                ret_ += "\n Member : {}".format(str(len(G.members)))
                                ret_ += "\n Pending : {}".format(gPending)
                                ret_ += "\n Qr : {}".format(gQr)
                                ret_ += "\n Ticket : {}".format(gTicket)
                                ret_ += ""
                                aditmadzs.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "- "+ str(no) + ". " + mem.displayName
                                aditmadzs.sendMessage(to,"Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = aditmadzs.getGroup(i)
                                if ginfo == group:
                                    aditmadzs.leaveGroup(i)
                                    aditmadzs.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getAllContactIds()
                               for i in gid:
                                   G = aditmadzs.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "* " + str(a) + ". " +G.displayName+ "\n"
                               aditmadzs.sendMessage(msg.to,"---[ FRIEND LIST ]---\n\n"+ma+"\n---[ Total"+str(len(gid))+"Friends ]---")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getGroupIdsJoined()
                               for i in gid:
                                   G = aditmadzs.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "* " + str(a) + ". " +G.name+ "\n"
                               aditmadzs.sendMessage(msg.to,"---[ GROUP LIST ]---\n"+ma+"\n---[ Total"+str(len(gid))+"Groups ]---")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = k1.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "* " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"---[ GROUP LIST ]---\n"+ma+"\n---[ Total"+str(len(gid))+"Groups ]---")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = k1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      k1.updateGroup(x)
                                   gurl = k1.reissueGroupTicket(msg.to)
                                   k1.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = aditmadzs.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      aditmadzs.rejectGroupInvitation(gid)
                                  aditmadzs.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  aditmadzs.sendMessage(to, "Tidak ada undangan yang tertunda")
#===========BOT UPDATE============#
                        elif cmd == "cppg":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                k1.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "cpp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["MAXfoto"][mid] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Amid] = True
                                k1.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Bmid] = True
                                k2.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                
                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Cmid] = True
                                k3.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "4up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Dmid] = True
                                k4.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "5up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Emid] = True
                                k5.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "6up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Fmid] = True
                                k6.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "7up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Gmid] = True
                                k7.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "8up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Hmid] = True
                                k8.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "9up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Imid] = True
                                k9.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "10up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Jmid] = True
                                k10.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "11up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Kmid] = True
                                k11.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "12up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Lmid] = True
                                k12.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                
                        elif cmd == "13up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Mmid] = True
                                k13.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "14up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Nmid] = True
                                k14.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "15up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Omid] = True
                                k15.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "16up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Pmid] = True
                                k16.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "17up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Qmid] = True
                                k17.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "18up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Rmid] = True
                                k18.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "19up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Smid] = True
                                k19.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "20up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Tmid] = True
                                k20.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "11up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][g1MID] = True
                                g1.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd.startswith("allname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 50:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k6.getProfile()
                                profile.displayName = string
                                k6.updateProfile(profile)
                                k6.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k8.getProfile()
                                profile.displayName = string
                                k8.updateProfile(profile)
                                k8.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k9.getProfile()
                                profile.displayName = string
                                k9.updateProfile(profile)
                                k9.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k10.getProfile()
                                profile.displayName = string
                                k10.updateProfile(profile)
                                k10.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k11.getProfile()
                                profile.displayName = string
                                k11.updateProfile(profile)
                                k11.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k12.getProfile()
                                profile.displayName = string
                                k12.updateProfile(profile)
                                k12.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k13.getProfile()
                                profile.displayName = string
                                k13.updateProfile(profile)
                                k13.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k14.getProfile()
                                profile.displayName = string
                                k14.updateProfile(profile)
                                k14.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k15.getProfile()
                                profile.displayName = string
                                k15.updateProfile(profile)
                                k15.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k16.getProfile()
                                profile.displayName = string
                                k16.updateProfile(profile)
                                k16.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k17.getProfile()
                                profile.displayName = string
                                k17.updateProfile(profile)
                                k17.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k18.getProfile()
                                profile.displayName = string
                                k18.updateProfile(profile)
                                k18.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k19.getProfile()
                                profile.displayName = string
                                k19.updateProfile(profile)
                                k19.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k20.getProfile()
                                profile.displayName = string
                                k20.updateProfile(profile)
                                k20.sendMessage(msg.to,"Nama diganti jadi " + string + "")
       
                        elif "bio: " in msg.text.lower():
                           if msg._from in admin:
                              proses = text.split(": ")
                              string = text.replace(proses[0] + ": ","")
                              profile_A = aditmadzs.getProfile()
                              profile_A.statusMessage = string
                              aditmadzs.updateProfile(profile_A)
                              aditmadzs.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k1.getProfile()
                              profile_A.statusMessage = string
                              k1.updateProfile(profile_A)
                              k1.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k2.getProfile()
                              profile_A.statusMessage = string
                              k2.updateProfile(profile_A)
                              k2.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k3.getProfile()
                              profile_A.statusMessage = string
                              k3.updateProfile(profile_A)
                              k3.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k4.getProfile()
                              profile_A.statusMessage = string
                              k4.updateProfile(profile_A)
                              k4.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k5.getProfile()
                              profile_A.statusMessage = string
                              k5.updateProfile(profile_A)
                              k5.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k6.getProfile()
                              profile_A.statusMessage = string
                              k6.updateProfile(profile_A)
                              k6.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k7.getProfile()
                              profile_A.statusMessage = string
                              k7.updateProfile(profile_A)
                              k7.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k8.getProfile()
                              profile_A.statusMessage = string
                              k8.updateProfile(profile_A)
                              k8.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k9.getProfile()
                              profile_A.statusMessage = string
                              k9.updateProfile(profile_A)
                              k9.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k10.getProfile()
                              profile_A.statusMessage = string
                              k10.updateProfile(profile_A)
                              k10.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k11.getProfile()
                              profile_A.statusMessage = string
                              k11.updateProfile(profile_A)
                              k11.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k12.getProfile()
                              profile_A.statusMessage = string
                              k12.updateProfile(profile_A)
                              k12.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k13.getProfile()
                              profile_A.statusMessage = string
                              k13.updateProfile(profile_A)
                              k13.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k14.getProfile()
                              profile_A.statusMessage = string
                              k14.updateProfile(profile_A)
                              k14.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k15.getProfile()
                              profile_A.statusMessage = string
                              k15.updateProfile(profile_A)
                              k15.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k16.getProfile()
                              profile_A.statusMessage = string
                              k16.updateProfile(profile_A)
                              k16.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k17.getProfile()
                              profile_A.statusMessage = string
                              k17.updateProfile(profile_A)
                              k17.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k18.getProfile()
                              profile_A.statusMessage = string
                              k18.updateProfile(profile_A)
                              k18.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k19.getProfile()
                              profile_A.statusMessage = string
                              k19.updateProfile(profile_A)
                              k19.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k20.getProfile()
                              profile_A.statusMessage = string
                              k20.updateProfile(profile_A)
                              k20.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)

                        elif cmd.startswith("name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = aditmadzs.getProfile()
                                profile.displayName = string
                                aditmadzs.updateProfile(profile)
                                aditmadzs.sendReplyMessage(msg_id, to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k6.getProfile()
                                profile.displayName = string
                                k6.updateProfile(profile)
                                k6.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k8.getProfile()
                                profile.displayName = string
                                k8.updateProfile(profile)
                                k8.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k9.getProfile()
                                profile.displayName = string
                                k9.updateProfile(profile)
                                k9.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k10.getProfile()
                                profile.displayName = string
                                k10.updateProfile(profile)
                                k10.sendMessage(msg.to,"Nama diganti jadi " + string + "")
								
                        elif cmd.startswith("11name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k11.getProfile()
                                profile.displayName = string
                                k11.updateProfile(profile)
                                k11.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("12name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k12.getProfile()
                                profile.displayName = string
                                k12.updateProfile(profile)
                                k12.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("13name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k13.getProfile()
                                profile.displayName = string
                                k13.updateProfile(profile)
                                k13.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("14name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k14.getProfile()
                                profile.displayName = string
                                k14.updateProfile(profile)
                                k14.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("15name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k15.getProfile()
                                profile.displayName = string
                                k15.updateProfile(profile)
                                k15.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("16name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k16.getProfile()
                                profile.displayName = string
                                k16.updateProfile(profile)
                                k16.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("17name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k17.getProfile()
                                profile.displayName = string
                                k17.updateProfile(profile)
                                k17.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("18name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k18.getProfile()
                                profile.displayName = string
                                k18.updateProfile(profile)
                                k18.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("19name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k19.getProfile()
                                profile.displayName = string
                                k19.updateProfile(profile)
                                k19.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("20name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k20.getProfile()
                                profile.displayName = string
                                k20.updateProfile(profile)
                                k20.sendMessage(msg.to,"Nama diganti jadi " + string + "")
								
                        elif cmd.startswith("botkickname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g1.getProfile()
                                profile.displayName = string
                                g1.updateProfile(profile)
                                g1.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#===========BOT UPDATE============#
                        elif msg.text.lower().startswith("tag"):
                          if msg._from in admin:						
                            data = msg.text[len("tag"):].strip()
                            if data == "":
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == "<":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count > mentargs:
                                                break
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == ">":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                if mentargs >= 0:
                                    strt = len(str(mentargs)) + 2
                                else:
                                    strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count < mentargs:
                                                count += 1
                                                continue
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == "=":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count != mentargs:
                                                count += 1
                                                continue
                                    akh = akh + len(str(count)) + 2 + 5
                                    strt = len(str(count)) + 2
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"Admin BOT\n\nCreator BOT:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal %s " %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +aditmadzs.getGroup(group).name + "\n"                                    
                                aditmadzs.sendMessage(msg.to,"BOT Protection\n\n* PROTECT URL :\n"+ma+"\n* PROTECT KICK :\n"+mb+"\n* PROTECT JOIN :\n"+md+"\n* PROTECT CANCEL:\n"+mc+"\n* PROTECT INVITE :\n"+me+"\nTotal %s Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "!respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sendMention1(msg.to, sender, "KICKER 1 ", "")
                                sendMention2(msg.to, sender, "KICKER 2 ", "")
                                sendMention3(msg.to, sender, "KICKER 3 ", "")
                                sendMention4(msg.to, sender, "KICKER 4 ", "")
                                sendMention5(msg.to, sender, "KICKER 5 ", "")
                                sendMention6(msg.to, sender, "KICKER 6 ", "")
                                sendMention7(msg.to, sender, "KICKER 7 ", "")
                                sendMention8(msg.to, sender, "KICKER 8 ", "")
                                sendMention9(msg.to, sender, "KICKER 9 ", "")
                                sendMention10(msg.to, sender, "KICKER 10 ", "")
                                sendMention11(msg.to, sender, "KICKER 11 ", "")
                                sendMention12(msg.to, sender, "KICKER 12 ", "")
                                sendMention13(msg.to, sender, "KICKER 13 ", "")
                                sendMention14(msg.to, sender, "KICKER 14 ", "")
                                sendMention15(msg.to, sender, "KICKER 15 ", "")
                                sendMention16(msg.to, sender, "KICKER 16 ", "")
                                sendMention17(msg.to, sender, "KICKER 17 ", "")
                                sendMention18(msg.to, sender, "KICKER 18 ", "")
                                sendMention19(msg.to, sender, "KICKER 19 ", "")
                                sendMention20(msg.to, sender, "KICKER 20 ", "")

                        elif cmd == "!name":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                k1.sendMessage(msg.to,responsename1, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k2.sendMessage(msg.to,responsename2, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k3.sendMessage(msg.to,responsename3, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k4.sendMessage(msg.to,responsename4, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k5.sendMessage(msg.to,responsename5, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k6.sendMessage(msg.to,responsename6, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k7.sendMessage(msg.to,responsename7, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k8.sendMessage(msg.to,responsename8, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k9.sendMessage(msg.to,responsename9, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k10.sendMessage(msg.to,responsename10, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})					
                                k11.sendMessage(msg.to,responsename11, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k12.sendMessage(msg.to,responsename12, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k13.sendMessage(msg.to,responsename13, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k14.sendMessage(msg.to,responsename14, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k15.sendMessage(msg.to,responsename15, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k16.sendMessage(msg.to,responsename16, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k17.sendMessage(msg.to,responsename17, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k18.sendMessage(msg.to,responsename18, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k19.sendMessage(msg.to,responsename19, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                k20.sendMessage(msg.to,responsename20, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "inv":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid,g1MID]
                                    aditmadzs.inviteIntoGroup(msg.to, anggota)
                                    k1.acceptGroupInvitation(msg.to)
                                    k2.acceptGroupInvitation(msg.to)
                                    k3.acceptGroupInvitation(msg.to)
                                    k4.acceptGroupInvitation(msg.to)								
                                    k5.acceptGroupInvitation(msg.to)
                                    k6.acceptGroupInvitation(msg.to)
                                    k7.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    k10.acceptGroupInvitation(msg.to)
                                    k11.acceptGroupInvitation(msg.to)
                                    k12.acceptGroupInvitation(msg.to)
                                    k13.acceptGroupInvitation(msg.to)
                                    k14.acceptGroupInvitation(msg.to)								
                                    k15.acceptGroupInvitation(msg.to)
                                    k16.acceptGroupInvitation(msg.to)
                                    k17.acceptGroupInvitation(msg.to)
                                    k18.acceptGroupInvitation(msg.to)
                                    k19.acceptGroupInvitation(msg.to)
                                    k20.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = aditmadzs.getGroup(msg.to)
                                    aditmadzs.inviteIntoGroup(msg.to, [g1MID])
                                    aditmadzs.sendMessage(msg.to,"Grup [ "+str(ginfo.name)+" ] Amax Dari JS")
                                except:
                                    pass

                        elif cmd == "in" or cmd == ".":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                time.sleep(0.006)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)	
                                k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k10.acceptGroupInvitationByTicket(msg.to,Ticket)	
                                time.sleep(0.006)
                                k11.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k12.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k13.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k14.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k15.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)	
                                k16.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k17.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k18.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k19.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.006)
                                k20.acceptGroupInvitationByTicket(msg.to,Ticket)								
                                G = k20.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k20.updateGroup(G)

                        elif cmd == "!outall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    aditmadzs.leaveGroup(i)

                        elif cmd == "outall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    k1.leaveGroup(i)
                                    k2.leaveGroup(i)
                                    k3.leaveGroup(i)
                                    k4.leaveGroup(i)
                                    k5.leaveGroup(i)
                                    k6.leaveGroup(i)
                                    k7.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    k10.leaveGroup(i)		
                                    k11.leaveGroup(i)
                                    k12.leaveGroup(i)
                                    k13.leaveGroup(i)
                                    k14.leaveGroup(i)
                                    k15.leaveGroup(i)								
                                    k16.leaveGroup(i)
                                    k17.leaveGroup(i)
                                    k18.leaveGroup(i)
                                    k19.leaveGroup(i)
                                    k20.leaveGroup(i)

                        elif cmd == "out" or cmd == "..":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                sendMention1(msg.to, sender, "Selamat tinggal, teman kita dulu.\n", " !")
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                                k3.leaveGroup(msg.to)
                                k4.leaveGroup(msg.to)
                                k5.leaveGroup(msg.to)								
                                k6.leaveGroup(msg.to)
                                k7.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                k10.leaveGroup(msg.to)
                                k11.leaveGroup(msg.to)
                                k12.leaveGroup(msg.to)
                                k13.leaveGroup(msg.to)
                                k14.leaveGroup(msg.to)
                                k15.leaveGroup(msg.to)								
                                k16.leaveGroup(msg.to)
                                k17.leaveGroup(msg.to)
                                k18.leaveGroup(msg.to)
                                k19.leaveGroup(msg.to)
                                k20.leaveGroup(msg.to)

                        elif cmd == "!bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                aditmadzs.leaveGroup(msg.to)

                        elif cmd.startswith("outme "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    h = aditmadzs.getGroup(i).name
                                    if h == ng:
                                        aditmadzs.leaveGroup(i)

                        elif cmd == ".in":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = g1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                g1.updateGroup(G)

                        elif cmd == ".out":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                g1.leaveGroup(msg.to)

                        elif cmd.startswith("outbot "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    h = aditmadzs.getGroup(i).name
                                    if h == ng:
                                        k1.leaveGroup(i)
                                        k2.leaveGroup(i)
                                        k3.leaveGroup(i)
                                        k4.leaveGroup(i)
                                        k5.leaveGroup(i)
                                        k6.leaveGroup(i)
                                        k7.leaveGroup(i)
                                        k8.leaveGroup(i)
                                        k9.leaveGroup(i)
                                        k10.leaveGroup(i)		
                                        k11.leaveGroup(i)
                                        k12.leaveGroup(i)
                                        k13.leaveGroup(i)
                                        k14.leaveGroup(i)
                                        k15.leaveGroup(i)								
                                        k16.leaveGroup(i)
                                        k17.leaveGroup(i)
                                        k18.leaveGroup(i)
                                        k19.leaveGroup(i)
                                        k20.leaveGroup(i)					
                                        aditmadzs.sendMessage(to,"Completed " +h)
                                
                        elif cmd == "!cek" or cmd == "cek":
                            if msg._from in admin:
                                try:k1.inviteIntoGroup(to, ["u341f7f5275f7d1cede62c1914211ad4b"]);has = "OK"
                                except:has = "NOT"
                                try:k1.kickoutFromGroup(to, ["u341f7f5275f7d1cede62c1914211ad4b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k1.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k2.inviteIntoGroup(to, ["u3f3acb2be414b688b55a4f9241e7568d"]);has = "OK"
                                except:has = "NOT"
                                try:k2.kickoutFromGroup(to, ["u3f3acb2be414b688b55a4f9241e7568d"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k2.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k3.inviteIntoGroup(to, ["ue12476df736c3465daa1bc651bd71092"]);has = "OK"
                                except:has = "NOT"
                                try:k3.kickoutFromGroup(to, ["ue12476df736c3465daa1bc651bd71092"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k3.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k4.inviteIntoGroup(to, ["u03c50a8d4fc951e5d2c5085f0b85efed"]);has = "OK"
                                except:has = "NOT"
                                try:k4.kickoutFromGroup(to, ["u03c50a8d4fc951e5d2c5085f0b85efed"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k4.sendReplyMessage(msg_id, to,"STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k5.inviteIntoGroup(to, ["u7a98af061da7d696332943ca0bb9ecf1"]);has = "OK"
                                except:has = "NOT"
                                try:k5.kickoutFromGroup(to, ["u7a98af061da7d696332943ca0bb9ecf1"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k5.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k6.inviteIntoGroup(to, ["uae8fad4e69d0f2a20244fc4f442c1643"]);has = "OK"
                                except:has = "NOT"
                                try:k6.kickoutFromGroup(to, ["uae8fad4e69d0f2a20244fc4f442c1643"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k6.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k7.inviteIntoGroup(to, ["ua5e4ce16bd6d339fadd867c01c55030c"]);has = "OK"
                                except:has = "NOT"
                                try:k7.kickoutFromGroup(to, ["ua5e4ce16bd6d339fadd867c01c55030c"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k7.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k8.inviteIntoGroup(to, ["u476519fe4ef4a83cfd8d120c0b9c9a38"]);has = "OK"
                                except:has = "NOT"
                                try:k8.kickoutFromGroup(to, ["u476519fe4ef4a83cfd8d120c0b9c9a38"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k8.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k9.inviteIntoGroup(to, ["u223d33a76a64be357b70a793eb18a1bb"]);has = "OK"
                                except:has = "NOT"
                                try:k9.kickoutFromGroup(to, ["u223d33a76a64be357b70a793eb18a1bb"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k9.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k10.inviteIntoGroup(to, ["u4224a71a152d32a58a6252e8a05581b7"]);has = "OK"
                                except:has = "NOT"
                                try:k10.kickoutFromGroup(to, ["u4224a71a152d32a58a6252e8a05581b7"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k10.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k11.inviteIntoGroup(to, ["u7819a71fecf94e82fc53e639aea7fb95"]);has = "OK"
                                except:has = "NOT"
                                try:k11.kickoutFromGroup(to, ["u7819a71fecf94e82fc53e639aea7fb95"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k11.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k12.inviteIntoGroup(to, ["u4465c7e7ae293d930a9746cdd98a5dae"]);has = "OK"
                                except:has = "NOT"
                                try:k12.kickoutFromGroup(to, ["u4465c7e7ae293d930a9746cdd98a5dae"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k12.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k13.inviteIntoGroup(to, ["u764ca43fe8b3e292c5c43a205bb1b85a"]);has = "OK"
                                except:has = "NOT"
                                try:k13.kickoutFromGroup(to, ["u764ca43fe8b3e292c5c43a205bb1b85a"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k13.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k14.inviteIntoGroup(to, ["ub98cd986d9ab27c6865c2fd79f786b7a"]);has = "OK"
                                except:has = "NOT"
                                try:k14.kickoutFromGroup(to, ["ub98cd986d9ab27c6865c2fd79f786b7a"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k14.sendReplyMessage(msg_id, to,"STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k15.inviteIntoGroup(to, ["ucde8a34cfbe0f5ee7ff2a1b8a1736cfe"]);has = "OK"
                                except:has = "NOT"
                                try:k15.kickoutFromGroup(to, ["ucde8a34cfbe0f5ee7ff2a1b8a1736cfe"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k15.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k16.inviteIntoGroup(to, ["u82e178c344f9105bf7c4ba99f8ce8fcc"]);has = "OK"
                                except:has = "NOT"
                                try:k16.kickoutFromGroup(to, ["u82e178c344f9105bf7c4ba99f8ce8fcc"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k16.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k17.inviteIntoGroup(to, ["u9764a50264b228a7e9096715fd399431"]);has = "OK"
                                except:has = "NOT"
                                try:k17.kickoutFromGroup(to, ["u9764a50264b228a7e9096715fd399431"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k17.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k18.inviteIntoGroup(to, ["u7f9a266188a54cde9d893c5f2e33fe3a"]);has = "OK"
                                except:has = "NOT"
                                try:k18.kickoutFromGroup(to, ["u7f9a266188a54cde9d893c5f2e33fe3a"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k18.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k19.inviteIntoGroup(to, ["u27a5e468fdc3c7a2db75017c794e81b1"]);has = "OK"
                                except:has = "NOT"
                                try:k19.kickoutFromGroup(to, ["u27a5e468fdc3c7a2db75017c794e81b1"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k19.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))
                                try:k20.inviteIntoGroup(to, ["u61cf33d2a8de0fe8529788701b154b2c"]);has = "OK"
                                except:has = "NOT"
                                try:k20.kickoutFromGroup(to, ["u61cf33d2a8de0fe8529788701b154b2c"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ok"
                                else:sil = "no"
                                if has1 == "OK":sil1 = "ok"
                                else:sil1 = "no"
                                time.sleep(0.006)
                                k20.sendReplyMessage(msg_id, to, "STATUS KICK OUT\nKICK : {} \nINVITE : {}".format(sil1,sil))

                        elif cmd == "kicker in":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = g1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                g1.updateGroup(G)

                        elif cmd == "kicker out":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                g1.leaveGroup(msg.to)

                        elif cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                              
                               aditmadzs.sendReplyMessage(msg_id, to, "Progres Speed...")
                               start = time.time() 
                               time.sleep(0.005)  
                               elapsed_time = time.time() - start
                               aditmadzs.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
       
                        elif cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               k1.sendReplyMessage(msg_id, to, "Progres Speed...")
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k1.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k2.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k3.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k4.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k5.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k6.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k7.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k8.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k9.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k10.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k11.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k12.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k13.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k14.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k15.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k16.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k17.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k18.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k19.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.006)  
                               elapsed_time = time.time() - start
                               k20.sendReplyMessage(msg_id, to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ADITMADZSreadPoint'][msg.to] = msg_id
                                 Setmain['ADITMADZSreadMember'][msg.to] = {}
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ADITMADZSreadPoint'][msg.to]
                                 del Setmain['ADITMADZSreadMember'][msg.to]
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cyduk":
                          if msg._from in admin:
                            if msg.to in Setmain['ADITMADZSreadPoint']:
                                if Setmain['ADITMADZSreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['ADITMADZSreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(aditmadzs.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        aditmadzs.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ADITMADZSreadPoint'][msg.to]
                                        del Setmain['ADITMADZSreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ADITMADZSreadPoint'][msg.to] = msg.id
                                    Setmain['ADITMADZSreadMember'][msg.to] = {}
                                else:
                                    aditmadzs.sendMessage(msg.to, "User kosong...")
                            else:
                                aditmadzs.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "cyduk on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  aditmadzs.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "cyduk off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  aditmadzs.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  aditmadzs.sendMessage(msg.to, "Sudak tidak aktif")

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ADITMADZSlimit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ADITMADZSlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                aditmadzs.sendMessage1(msg)
                                            except Exception as e:
                                                aditmadzs.sendMessage(msg.to,str(e))
                                    else:
                                        aditmadzs.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                aditmadzs.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        aditmadzs.sendMessage(msg.to,str(e))
                                else:
                                    aditmadzs.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif cmd.startswith("callto "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              dan = text.split(" ")
                              num = int(dan[1])
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                       if mention["M"] not in lists:
                                              lists.append(mention["M"])
                                  for ls in lists:
                                   for var in range(0,num):
                                        group = aditmadzs.getGroup(to)
                                        members = [ls]
                                        aditmadzs.acquireGroupCallRoute(to)
                                        aditmadzs.inviteIntoGroupCall(to, contactIds=members)
                                  aditmadzs.sendMessage(msg.to, "Spilled into the neck.")
#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  k1.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    k1.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs) 

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
#===========Protection============#                                    
                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT URL ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT URL ]\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT KICK ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT KICK ]\n" + msgs)

                        elif 'Protectkick1 ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick1 ','')
                              if spl == 'on':
                                  if msg.to in protectkick1:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick1.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT KICK1 ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick1:
                                         protectkick1.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT KICK1 ]\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT JOIN ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT JOIN ]\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT CANCEL ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT CANCEL ]\n" + msgs)
                     
                        elif 'Protectcanceljs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcanceljs ','')
                              if spl == 'on':
                                  if msg.to in protectcanceljs:
                                       msgs = "Protect cancel JS sudah aktif"
                                  else:
                                       protectcanceljs[msg.to] = True
                                       f=codecs.open('protectcanceljs.json','w','utf-8')
                                       json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect cancel JS diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT CANCELJS ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcanceljs:
                                         del protectcanceljs[msg.to]
                                         f=codecs.open('protectcanceljs.json','w','utf-8')
                                         json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect cancel JS dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel JS sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT CANCELJS ]\n" + msgs)
               
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT INVITE ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT INVITE ]\n" + msgs)

                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Pro JS sudah aktif"
                                  else:
                                       protectantijs[msg.to] = True
                                       f=codecs.open('protectantijs.json','w','utf-8')
                                       json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Pro JS diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT JS ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         del protectantijs[msg.to]
                                         f=codecs.open('protectantijs.json','w','utf-8')
                                         json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)												 
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Pro JS dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Pro JS sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT JS ]\n" + msgs)

                        elif 'G ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('G ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Ghost diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT GHOST ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Ghost dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT GHOST ]\n" + msgs)                                                 

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)                                      
                                  if msg.to in protectcancel:
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT ALLPROTECT ]\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    aditmadzs.sendMessage(msg.to, "[ STATUS PROTECT ALLPROTECT ]\n" + msgs)

#===========KICKOUT============#
                        elif ("M " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = aditmadzs.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           aditmadzs.updateGroup(G)
                                           invsend = 0
                                           Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                           g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           g1.kickoutFromGroup(msg.to, [target])
                                           g1.leaveGroup(msg.to)
                                           X = aditmadzs.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           aditmadzs.updateGroup(X)
                                       except:
                                           pass
                         
                        elif ("Vk " in msg.text):
                          if msg._from in admin:
                            if msg.toType == 2:
                                prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                                for i in range(len(prov)):
                                    aditmadzs.kickoutFromGroup(msg.to,[prov[i]["M"]])

                        elif ("Bk " in msg.text):
                          if msg._from in admin:
                            if msg.toType == 2:
                                prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                                for i in range(len(prov)):
                                    random.choice(ABC).kickoutFromGroup(msg.to,[prov[i]["M"]])

                        elif text.lower() in ['kickban','killban']:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                gMembMids = [contact.mid for contact in group.members]
                                matched_list = []
                            for tag in wait["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                aditmadzs.sendMessage(msg.to,"There was no blacklist user")
                                return
                            for jj in matched_list:
                                aditmadzs.kickoutFromGroup(msg.to,[jj])
                            aditmadzs.sendMessage(msg.to,"Blacklist kicked out")

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           staff.remove(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           Bots.remove(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                aditmadzs.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                                ma = ""
                                for i in admin:
                                    ma = ki.getContact(i)
                                    random.choice(ABC).sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                                ma = ""
                                for i in staff:
                                    ma = ki.getContact(i)
                                    random.choice(ABC).sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                                ma = ""
                                for i in Bots:
                                    ma = ki.getContact(i)
                                    random.choice(ABC).sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                aditmadzs.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                aditmadzs.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "respongift on" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon gift diaktifkan")

                        elif cmd == "respongift off" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon gift dinonaktifkan")                                

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                aditmadzs.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                aditmadzs.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                aditmadzs.sendMessage(msg.to,"Auto block diaktifkan")

                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                aditmadzs.sendMessage(msg.to,"Auto block dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "read on" or text.lower() == 'read on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi read diaktifkan")

                        elif cmd == "read off" or text.lower() == 'read off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi read dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = aditmadzs.getContact(i)
                                        aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = aditmadzs.getContacts(wait["blacklist"])
                              mc = "[ %i ] User Blacklist" % len(ragets)
                              aditmadzs.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k1.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k2.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k3.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k4.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k5.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k6.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k7.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k8.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k9.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k10.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k11.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k12.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k13.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k14.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k15.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k16.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k17.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k18.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k19.sendMessage(msg.to,"Kalian di maafkan " +mc)
                              k20.sendMessage(msg.to,"Kalian di maafkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  aditmadzs.sendMessage(msg.to, "Pesan Msg\nPesan Message diganti jadi :\n\n[ {} ]".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  aditmadzs.sendMessage(msg.to, "Welcome Msg\nWelcome Message diganti jadi :\n\n[ {} ]".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  aditmadzs.sendMessage(msg.to, "Leave Msg\nLeave Message diganti jadi :\n\n[ {} ]".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  aditmadzs.sendMessage(msg.to, "Respon Msg\nRespon Message diganti jadi :\n\n[ {} ]".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ADITMADZSmessage"] = spl
                                  aditmadzs.sendMessage(msg.to, "Spam Msg\nSpam Message diganti jadi :\n\n[ {} ]".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  aditmadzs.sendMessage(msg.to, "Sider Msg\nSider Message diganti jadi :\n\n[ {} ]".format(str(spl)))

                        elif text.lower() == "pesan":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Pesan Msg\nPesan Message lu :\n\n[ " + str(wait["message"]) + " ]")

                        elif text.lower() == "welcome":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Welcome Msg\nWelcome Message lu :\n\n[ " + str(wait["welcome"]) + " ]")
                               
                        elif text.lower() == "leave":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "Leave Msg\nLeave Message lu :\n\n[ " + str(wait["leave"]) + " ]")                                 

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "?....?\n\n[ " + str(Setmain["ADITMADZSmessage1"]) + " ]")

                        elif text.lower() == "respon":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n[ " + str(wait["Respontag"]) + " ]")

                        elif text.lower() == "sider":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n[ " + str(wait["mention"]) + " ]")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     aditmadzs.sendMessage(msg.to, "GROUP : %s" % str(group.name))
                                     group1 = k1.findGroupByTicket(ticket_id)
                                     k1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group2 = k2.findGroupByTicket(ticket_id)
                                     k2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     group3 = k3.findGroupByTicket(ticket_id)
                                     k3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group4 = k4.findGroupByTicket(ticket_id)
                                     k4.acceptGroupInvitationByTicket(group4.id,ticket_id)                                     
                                     group5 = k5.findGroupByTicket(ticket_id)
                                     k5.acceptGroupInvitationByTicket(group5.id,ticket_id)                                     
                                     group6 = k6.findGroupByTicket(ticket_id)
                                     k6.acceptGroupInvitationByTicket(group6.id,ticket_id)                                     
                                     group7 = k7.findGroupByTicket(ticket_id)
                                     k7.acceptGroupInvitationByTicket(group7.id,ticket_id)                                     
                                     group8 = k8.findGroupByTicket(ticket_id)
                                     k8.acceptGroupInvitationByTicket(group8.id,ticket_id)
                                     group9 = k9.findGroupByTicket(ticket_id)
                                     k9.acceptGroupInvitationByTicket(group9.id,ticket_id)
                                     group10 = k10.findGroupByTicket(ticket_id)
                                     k10.acceptGroupInvitationByTicket(group10.id,ticket_id)
                                     group11 = k11.findGroupByTicket(ticket_id)
                                     k11.acceptGroupInvitationByTicket(group11.id,ticket_id)
                                     group12 = k12.findGroupByTicket(ticket_id)
                                     k12.acceptGroupInvitationByTicket(group12.id,ticket_id)
                                     group13 = k13.findGroupByTicket(ticket_id)
                                     k13.acceptGroupInvitationByTicket(group13.id,ticket_id)
                                     group14 = k14.findGroupByTicket(ticket_id)
                                     k14.acceptGroupInvitationByTicket(group14.id,ticket_id)                                     
                                     group15 = k15.findGroupByTicket(ticket_id)
                                     k15.acceptGroupInvitationByTicket(group15.id,ticket_id)                                     
                                     group16 = k16.findGroupByTicket(ticket_id)
                                     k16.acceptGroupInvitationByTicket(group16.id,ticket_id)                                     
                                     group17 = k17.findGroupByTicket(ticket_id)
                                     k17.acceptGroupInvitationByTicket(group17.id,ticket_id)                                     
                                     group18 = k18.findGroupByTicket(ticket_id)
                                     k18.acceptGroupInvitationByTicket(group18.id,ticket_id)
                                     group19 = k19.findGroupByTicket(ticket_id)
                                     k19.acceptGroupInvitationByTicket(group19.id,ticket_id)
                                     group20 = k20.findGroupByTicket(ticket_id)
                                     k20.acceptGroupInvitationByTicket(group20.id,ticket_id)
            
    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
