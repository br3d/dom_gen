import whois, time
from threading import Thread
from Queue import Queue

dm_list = open("name.txt").read().split('\n')
good = open("good.txt", "a+")
thread_num = 5
q = Queue()

def dom_check():
	for x in(dm_list):
	    time.sleep(1)
	    print 'check - ',x
	    domain = whois.query(x)
	    try:
	        domain.name
	    except Exception, detail:
	        print "Domain %s non occupied" %x
		good.write(x+"\n")
	    #return 0

def dom_chk(x):
	time.sleep(1)
	print 'check - ',x
	domain = whois.query(x)
	try:
	    domain.name
	except Exception, detail:
	    print "Domain %s non occupied" %x
	    good.write(x+"\n")

def worker():
	while True:
		item = q.get()
		dom_chk(item)
		q.task_done()


for i in range (thread_num):
	t = Thread(target=worker)
	t.setDaemon(True)
	t.start()

for item in dm_list:
	q.put(item)

q.join()
