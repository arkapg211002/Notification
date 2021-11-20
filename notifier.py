import time
import notify2
import dbus_next
from topnews import topStories
#icon image
icpath="D:\pythonIsFun\notify\icon.png"
newsitems=topStories()
#notifier name
notify2.init("News_Feed")
news=notify2.Notification(None,icon=icpath)
news.set_urgency(notify2.URGENCY_NORMAL)
#dispaly duration
news.set_timeout(10000)
for items in newsitems:
    #dictionary to store title and description of news
    news.update(items['TITLE'],items['DESCRIPTION'])
    news.show()
    time.sleep(15)