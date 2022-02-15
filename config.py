class basevars():
    url = 'http://data.fixer.io/api/latest'
    key = '23a6adad66c705a6af5c284c8e1d347e'
    brokenkey = '23a6adad66c705a6af5c284c8e1d347e23232323' #was using this for error testing
    base = 'EUR' #only base allowed on this api at free tier
    sym = 'GBP,USD' #cant be a list documentation was outdated, pass in as one string
