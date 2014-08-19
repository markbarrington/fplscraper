from urllib2 import Request, urlopen, URLError

url="http://fantasy.premierleague.com/web/api/elements/"

f = open('playerdata', 'w')

# Loop continues while valid data is returned.
i=1
while True:
    # Construct URL

    thisurl = url + str(i) + "/"
    req = Request(thisurl)

    # Request URL
    try:
        response = urlopen(req)

    # Report Error and exit
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            break
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            break

    # Read responses and write them to output file
    else:
        data = response.read()
        print i
        f.write(data + '\n')
        i += 1

f.close()

