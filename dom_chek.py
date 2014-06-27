import whois, time

dm_list = open("name_w.txt").read().split('\n')
good = open("good.txt", "a+")
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


