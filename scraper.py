import scraperwiki
import lxml.html
import urllib


def parse(url):
    print url
    #reader = urllib.urlopen(url).read()
    #tree = lxml.html.fromstring( reader )
    
    #title = tree.find_class('header_adview')[0].cssselect('h2')[0].text_content()

    #data = { 'annonce_url': url, 'title': title }
    #scraperwiki.sqlite.save(unique_keys=['annonce_url'],data=data)

    

url = "http://www.mistersmoke.com/mods-c-311.html"
reader = urllib.urlopen(url).read()
tree = lxml.html.fromstring( reader )

list_annonces = tree.find_class('desc')
annonces = list_annonces.cssselect('a')

for a in annonces:
    parse( a.get('href') )
