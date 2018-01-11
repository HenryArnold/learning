import shodan
SHODAN_API_KEY = "i3t9YPT0YQwBHFTRC5L88A1HzqQImb3l"
api = shodan.Shodan(SHODAN_API_KEY)
try:
    results = api.search('apache')
    print 'Results found: %s' %results['total']
    for result in results['matches']:
        print 'IP: %s' %result['ip_str']
        print result['data']
        print ''
except shodan.APIError, e:
    print 'Error: %s' % e 
