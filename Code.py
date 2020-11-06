import requests
from bs4 import BeautifulSoup
def get_live(symbol):
    url = 'https://finance.yahoo.com/quote/'+symbol+'/history?p='+symbol
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        'button',
        'font'
    ]



    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    output=output[output.find('Currency in USD'):]
    output=output[output.find('/react-text'):]
    output=output[:output.find('Market open')]
    output=output[output.find('react-text:'):]
    output=output[output.find('/react-text'):]
    output=output[output.find(' '):]
    output=output[:output.find('react-text')]
    output2=output[::-1]
    output2=output2[output2.find("TSE"):]
    output=output2[::-1]
    return(output)
    
def get_past(symbol,days):
    if(days>=45):
        print("Unfortunately, only 44 days of the past are available")
    else:
        url = 'https://finance.yahoo.com/quote/'+symbol+'/history?p='+symbol
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)
        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            'button',
            'font'
        ]
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)

        output=output[output.find('Volume'):]
        output=output[:output.find('*Close')]
        prices= output.split(" ")
        prices.remove("Volume")
        prices.remove("")
        x=0
        length=len(prices)
        x=0
        terms=days*9
        length=len(prices)
        count=length-terms
        while(x<count):
            prices.pop(terms)
            x+=1
        x=0
        length=len(prices)
        length=length-8
        while(x<=length):
            prices[x]=prices[x]+" "+prices[x+1]
            prices.pop(x+1)
            prices[x]=prices[x]+prices[x+1]
            prices.pop(x+1)
            length-=2
            x+=7
        prices.insert(0,"Volume")
        prices.insert(0,"Adj. Close")
        prices.insert(0,"Close")
        prices.insert(0,"Low")
        prices.insert(0,"High")
        prices.insert(0,"Open")
        prices.insert(0,"Date")
        return(prices)
