import scraperwiki
from scrapemark import scrape
import scraperwiki
count = 0

FormatList = ["Managed","Native", "Mobile", "iPad", "iPhone","Android", "Salesforce1","Lightning Ready"]
FilterList = ["9","6","10","11","12","13","14","15"]

for Filter0 in FilterList:
  print count
  for page in range(1,40):
    URLPath = URLRoot.format(str(page))
    URL = URLPath+Filter0
    print URL
  
    html = scraperwiki.scrape(URL)
    scrape_data = scrape("""
     {*
     
     <a class="tile-title" href="{{ [mobile].[link] }}" id="{{ [mobile].[id] }}" title="{{ [mobile].[title1] }}"></a>
     
     *}
     """, html=html);
  
    data = [{'Title':p['title1'][0], 'URL':p['link'][0], 'ID':p['id'][0], 'Format':FormatList[count]} for p in scrape_data['mobile']]
  
    scraperwiki.sqlite.save(unique_keys=["URL"], data=data)
  count = count+1
  if count>2:
    break
