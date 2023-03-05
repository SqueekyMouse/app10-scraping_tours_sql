import requests
import selectorlib
# commit: track new events in file Sec38

URL='http://programmer100.pythonanywhere.com/tours/'
# some servers dont allow scraping so supply headers if necessary!!!
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the page source from the url"""
    response=requests.get(url, headers=HEADERS)
    source=response.text
    return(source)

def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file('extract.yaml')
    value=extractor.extract(source)['tours'] # tours key is set in the yaml file val is tag '#displaytimer'
    # #displaytimer - copied from firefox > page > inspector > copy css selector!!!
    return(value)

def send_email():
    print('emails sent')

def store(extracted):
    with open('data.txt','a') as file:
        file.write(f'{extracted}\n')

def read(extracted):
    with open('data.txt','r') as file:
        return(file.read())

if __name__=='__main__':
    scraped=scrape(URL)
    extracted=extract(scraped)
    print(extracted)
    content=read(extracted)

    if extracted!='No upcoming tours':
        if extracted not in content: # dont send multiple mails for smae event
            store(extracted) # store emailed events in file
            send_email()
            