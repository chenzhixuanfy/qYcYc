import requests
import re
 
cookie = "acw_tc=700f019817126239226453381e2aa565356abdb1f11af31b2cd0f89b7c; QCCSESSID=f29c08d49a448b017bbd736157; qcc_did=a81874db-1845-4b56-b6c6-d686864e628c; UM_distinctid=18ec0575e12109e-06e0f0252bfe53-26001a51-e1000-18ec0575e1311fe; tfstk=fGqSC5gGbQAW-wyjt4B4CGCqkAnCQ7sNdpMLIJKyp0nJ9BetgYrPZJhQOSlDaz7n2XKQTJrzT0QodeFUguzzAJxIpJFhEXWlu82oxDCN_ksaE8xjxifgV2hvH-DHvv3A75vxxDCNg4ZTStm3_HM6r_wAhvkBeXFKy-KxUjdpvWh-kIHsIDhL9DBjkYkZpeHJyI3xCAeAlxQSg81nvz2m06LbFjtpfdc-yF2W8hKTcYg7E8hbF8ZjF4GtuYaUZuF4puroo6OKx-z_OyFOgUl85ANj7z16V5NopSizX9boo2E72maVjdGYVJZjrrRJyAiSNVE-5M6Tn2Ubc0rRtF24hb3s0r7ca2o7NPciyZf0O-Gz9ugvNslU7-r-l5C2cW0QJuoY2sI14ctZ1r3BRGn2AxGNhtTH8BpM5BTNydEsyxDDQt6X7e0-nxGNhtTH-4HmndWfhF8h.; CNZZDATA1254842228=1356444683-1712623935-%7C1712624221"
 
def get_pid_tid():
    url = 'https://www.qcc.com/web/search/advance?hasState=true'
 
    headers = {
        'accept-encoding': 'gzip, deflate, br'
        ,'accept-language': 'zh-CN,zh;q=0.9'
        ,'cache-control': 'max-age=0'
        ,'cookie': cookie
        ,'referer': 'https://www.qcc.com/'
        ,'sec-fetch-dest': 'document'
        ,'sec-fetch-mode': 'navigate'
        ,'sec-fetch-site': 'same-origin'
        ,'sec-fetch-user': '?1'
        ,'upgrade-insecure-requests': '1'
        ,'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'''
    }
 
    res = requests.get(url, headers=headers).text
    try:
        pid = re.findall("pid='(.*?)'", res)[0]
        tid = re.findall("tid='(.*?)'", res)[0]
    except:
        pid = ''
        tid = ''
 
    return pid, tid

pid, tid = get_pid_tid()
print(pid)
print(tid)