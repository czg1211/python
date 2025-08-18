import requests
import execjs

headers = {

    'cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1755526410; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1755526410; HMACCOUNT=2274A12610CEB2C0; sessionid=a0ytblt1c8x925reb444hzes9ea047hh; qpfccr=true; no-alert3=true; tk=-44118752669246578',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',

}

s = 0  # 每一页的机票价格之和
times = 0  # 一共有多少次班机

js_compile = execjs.compile(open("problem1.js", encoding="utf-8").read())
for i in range(1, 6):
    m = js_compile.call("run")
    params = {
        'page': i,
        'm': m,
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/1', params=params, headers=headers)
    # print(response.json())
    json_data = response.json()
    s += sum([_.get("value") for _ in json_data.get("data")])
    times += len(json_data.get("data"))
    # print(s,times)
# print(s // times)
result = s // times
print(result)
