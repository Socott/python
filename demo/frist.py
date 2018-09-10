import requests
import re
page = 0
while(page < 100):
    page = page+1
    content = requests.get('http://www.gyyqcloud.com/buy/list.php?page='+str(page)).text
    pattern = re.compile('<div.*?need_list.*?</a>.*?goShow\((\d+).*?class="need_title">(.*?)</a>',re.S)
    results = re.findall(pattern,content)
    for item in results:
        content_1 = requests.get('http://www.gyyqcloud.com/buy/show.php?itemid=' + str(item[0])).text
        pattern_1 = re.compile('<div.*?"need_info_con".*?<h1.*?"info_title">(.*?)</h1>.*?"info_li">'
                               '.*?<p>(.*?)</p>.*?"company_box".*?"com_name">(.*?).*?"com_contact"'
                               '(.*?)<a.*?<br>(.*?)<br>(.*?)<br>(.*?)<br>(.*?)</div>',re.S)
        results_1 = re.findall(pattern_1,content_1)
        for item_1 in results_1:
            print(item_1)