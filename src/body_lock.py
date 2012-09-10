
name = "locked"


def doData():
    server_status = getServerStatus()
    lockstatus = server_status["globalLock"]
    # Get the ratio if version 2.0.6 or calculate if newer
    ratio = lockstatus.get("ratio",
        lockstatus["lockTime"] / float(lockstatus["totalTime"]))
    print name + ".value " + str(100 * ratio)
    if "locks" in server_status:
        for k, v in server_status["locks"].iteritems():
            print k, v


def doConfig():
    print "graph_title MongoDB write lock percentage"
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    print name + ".label " + name
