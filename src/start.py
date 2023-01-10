#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：OPGG 
@File    ：start.py
@IDE     ：PyCharm 
@Author  ：离开流沙河的坚定大土豆
@Date    ：2022/12/8 22:07 
'''

import pandas as pd
import bs4
import time
import random
from bs4 import BeautifulSoup
import urllib.request
import requests
import json

def askurl(urlbase, params):
    params = urllib.parse.urlencode(params)
    url = urlbase + '?' + params
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    request = urllib.request.Request(url, headers=header)
    try:
        response = urllib.request.urlopen(request, timeout=5)
        html = response.read().decode("utf-8")
    except Exception as a:
        print(a)
    return html

def test():
    champion_names = {}
    url = 'https://www.op.gg/champions/{champion_name}/{position}/{content}' + '?' + 'region={}' + '&tier={}' + '&role={}' + '&patch={}'
    positions = {'top':'top', 'jungle':'jungle', 'middle':'middle', 'bottom':'bottom', 'support':'support'}
    region = {}
    params = {"region":"global","tier":"platinum_plus"}
    # https: // www.op.gg / champions / zac / jungle / build?region = global & tier = platinum_plus
    html = askurl(url, params)
    soup = BeautifulSoup(html,"html.parser")

    print(html)

    # result = []
    #
    # for tr in soup.find(name = "tbody"):
    #     tmp_result = []
    #     if isinstance(tr, bs4.element.Tag):
    #         tds = tr('td')
    #         rank = int(tds[0]('span')[0].string)
    #         print(rank)
    #         tmp_result.append(rank)
    #
    #         print(tds[1])


championname = {'阿卡丽 ': 'akali', '牛头': 'alistar', '阿木木': 'amumu', '冰鸟': 'anivia', '安妮': 'annie',
                '艾希': 'ashe', '机器人': 'blitzcrank', '火男': 'brand', '女警': 'caitlyn',
                '蛇女': 'cassiopeia', '大虫子': 'chogath', '飞机': 'corki', '诺手': 'darius', '皎月': 'diana',
                '蒙多': 'drmundo', '德莱文': 'delevin', '蜘蛛': 'elise',
                '寡妇': 'evelynn', 'ez': 'ezreal', '稻草人': 'fiddlesticks', '剑姬': 'fiora', '鱼人': 'fizz',
                '加里奥': 'galio', '船长': 'gangplank', '盖伦': 'garen',
                '酒桶': 'gragas', '人马': 'hecarim', '大头': 'heimerdinger', '刀妹': 'irelia', '凤女': 'janna',
                '皇子': 'jarvaniv', '贾克斯': 'jax', '杰斯': 'jayce', '卡尔玛': 'karma',
                '死歌': 'karthus', '卡萨丁': 'kassadin', '卡特': 'katarina', '天使': 'kayle', '凯南': 'kennen',
                '螳螂': 'khazix', '大嘴': 'kogmaw', '妖姬': 'leblanc', '盲僧': 'leesin', '女坦': 'Leona',
                '露露': 'lulu', '拉克丝': 'Lux',
                '石头人': 'Malphite', '马尔扎哈': 'Malzahar', '大树': 'Maokai', '剑圣': 'Yi', '女枪': 'MissFortune',
                '猴子': 'Monkeyking', '铁男': 'Mordekaiser', '莫甘娜': 'Morgana'
    , '娜美': 'Nami', '狗头': 'Nasus', '泰坦': 'Nautilus', '豹女': 'Nidalee', '梦魇': 'Nocturne', '雪人': 'Nunu',
                '奥拉夫': 'Olaf', '发条': 'Orianna', '潘森': 'Pantheon', '波比': 'Poopy', '龙龟': 'Rammus',
                '鳄鱼': 'Renekton', '狮子狗': 'Rengar',
                '瑞文': 'Rivan', '兰博': 'Rumble', '瑞兹': 'Ryze', '猪女': 'Sejuani', '小丑': 'Shaco', '慎': 'Shen',
                '龙女': 'Shyvana', '炼金': 'Singed', '塞恩': 'Sion', '希维尔': 'Sivir', '蝎子': 'Skarner',
                '琴女': 'Sona', '奶妈': 'Soraka', '乌鸦': 'Swain', '辛德拉': 'Syndra'
    , '男刀': 'Talon', '宝石': 'Taric', '提莫': 'Teemo', '锤石': 'Thresh', '小炮': 'Tristana', '巨魔': 'Trundle',
                '蛮王': 'Tryndamere', '卡牌': 'TwistedFate', '老鼠': 'Twitch', '乌迪尔': 'Udyr', '厄加特': 'Urgot',
                '维鲁斯': 'Varus', '薇恩': 'Vayne',
                '小法': 'Veigar', '蔚': 'Vi', '维克托': 'Viktor', '吸血鬼': 'Vladimir', '狗熊': 'Volibear',
                '狼人': 'Warwick', '泽拉斯': 'Xerath', '赵信': 'XinZhao', '掘墓': 'Yorick', '劫': 'Zed',
                '炸弹人': 'Ziggs', '时光': 'Zilean', '婕拉': 'Zyra', '佐伊': 'zoe', '永恩': 'yone', '萨米拉': 'samira',
                '亚索': 'yasuo',
                '塞拉斯': 'sylas', '卢锡安': 'lucian', '艾克': 'ekko', '阿狸': 'ahri', '瑟提': 'sett',
                '奇亚娜': 'qiyana', '龙王': 'aurelionsol', '克烈': 'kled', '妮蔻': 'neeko'

                }


def collect_build_data(champion_name, tier, version):
    # 配置信息
    # urlbase = 'https://www.op.gg/champions/'
    # header = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    #     "Accept-Language": "zh-CN,zh;q=0.9"
    # }
    #
    # for key, value in championname.items():
    #
    #     # 遍历英雄名称字典，对每个英雄信息进行爬取
    #
    #     url = urlbase + 'value'
    #     res = requests.get(url=url, headers=header)
    #
    #     print("正在爬取英雄 “{}” 的信息页面：{}".format(key, url))
    #
    #     soup = BeautifulSoup(res.text, "html.parser")
    #
    #     for item in soup.find_all('div', attrs={"class":["css-brbf14 ew1oorz6","css-oxevym ew1oorz5"]}):
    #         print(item.contents[0])
    #
    #     # 爬取一个英雄后，睡眠随机时间，防止被反爬虫机制挂掉
    #     time.sleep(random.random()*3)

    result = {}

    url = 'https://www.op.gg/champions/{}'.format(champion_name)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    params = {
        'region': 'global',
        'tier': tier,
        'patch': version
    }

    result['region'] = params['region']
    result['tier'] = params['tier']
    result['patch'] = params['patch']

    res = requests.get(url=url, headers=header, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    # print(soup)
    # 1.英雄总体情况
    # for item in soup.find_all('div',attrs={"class":["css-brbf14 ew1oorz6","css-oxevym ew1oorz5"]}):
    #     print(item.contents[0])
    # 2.英雄位置
    positions = []
    result['positions'] = {}
    for items in soup.find_all('div', class_='css-8b90v4 e1uquoo1'):
        pos = items.select('a')
        for i in pos:
            positions.append(i.get('data-value'))
            result['positions'][positions[-1]] = {}
            # print(i.get('data-value'))
    print(positions)

    for sub_pos in positions:
        sub_url = 'https://www.op.gg/champions/{}/{}/build'.format(champion_name, sub_pos)
        sub_res = requests.get(url=sub_url, headers=header, params=params)
        sub_soup = BeautifulSoup(sub_res.text, "html.parser")
        # print('英雄 {} 在 {} 位置的总体信息：'.format(champion_name, sub_pos))

        # 1.英雄总体情况
        tmpdict = {}
        for item in sub_soup.find('div', class_='tier-icon'):
            tmpdict['level'] = item['alt']
        for i, item in enumerate(sub_soup.find_all('div', attrs={"class": ["css-oxevym ew1oorz5"]})):
            if i == 0:
                tmpdict['win_rate'] = float(item.contents[0])
            elif i == 1:
                tmpdict['pick_rate'] = float(item.contents[0])
            elif i == 2:
                tmpdict['ban_rate'] = float(item.contents[0])
            # print(item.contents[0])
        # result['positions'][sub_pos] = tmpdict
        # 2.英雄符文以及选择率、胜率
        # print('------英雄符文及其胜率------')
        tmplist = []
        for index, items in enumerate(sub_soup.find_all('li', attrs={"class":["css-vg8zeo e12igh9s3", "css-1vrxlx9 e12igh9s3"]})):
            # print(items)
            # print(items.find_all('div', class_='css-1soapw6 e12igh9s6'))
            tmpdict2 = {}
            for subitem in items.find_all('div', class_='css-1soapw6 e12igh9s6'):
                # print(subitem)
                # print([i.get('alt') for i in subitem.find_all('img')])
                tmpdict2['rune'] = [i.get('alt') for i in subitem.find_all('img')]
                for i in items.find_all('span', attrs={'class':['pick-rate', 'win-rate']}):
                    # print(i)
                    if i.find('small'):
                        # print(i.contents[0])
                        # print(i.find('small').contents[0])
                        tmpdict2['pick_rate'] = float(i.contents[0])
                        tmpdict2['games'] = (i.find('small').contents[0].replace(',', ''))
                    if i.find('em'):
                        # print(i.find('em').contents[0])
                        tmpdict2['win_rate'] = float(i.find('em').contents[0])
            tmplist.append(tmpdict2)
        tmpdict['runes'] = tmplist
        # result['positions'][sub_pos] = tmpdict

        # 3. 英雄出装及其胜率
        # print('---------英雄出装及其胜率---------')
        tmplist = []
        for items in sub_soup.find_all('tbody')[2]:
            tmpdict3 = {}
            for index, td in enumerate(items.find_all('td')):
                if index % 3 == 0:
                    altlist = [img.get('alt') for img in td.find_all('img', class_='bg-image')]
                    srclist = [img.get('src') for img in td.find_all('img', class_='bg-image')]
                    tmpdict3['equip'] = altlist
                    tmpdict3['img_src'] = srclist
                else:
                    if td.find('strong'):
                        # print(td.find('strong').contents[0])
                        if index % 3 == 1:
                            tmpdict3['pick_rate'] = float(td.find('strong').contents[0])
                        if index % 3 == 2:
                            tmpdict3['win_rate'] = float(td.find('strong').contents[0])
                    if td.find('small'):
                        # print(td.find('small').contents[0].replace(',', ''))
                        tmpdict3['games'] = (td.find('small').contents[0].replace(',', ''))
                if index % 3 == 2:
                    # 更新
                    tmplist.append(tmpdict3)
                    tmpdict3 = {}
        tmpdict['equipments'] = tmplist
        # print(tmpdict)

        # 4. 英雄反制信息
        counter_res = collect_counters_data(champion_name, sub_pos, tier, version)
        tmpdict['counters'] = counter_res
        # print(tmpdict)
        result['positions'][sub_pos] = tmpdict

        time.sleep(random.random() * 3)

    return result



def collect_counters_data(champion_name, position, tier, version):
    url = 'https://www.op.gg/champions/{}/{}/counters'.format(champion_name, position)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    params = {
        'region': 'global',
        'tier': tier,
        'patch': version
    }
    res = requests.get(url=url, headers=header, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    # 搜集反制英雄
    resultlist = []
    for i, items in enumerate(zip(soup.find_all('div', class_='css-aj4kza eocu2m71'), soup.find_all('span', class_='css-ekbdas eocu2m73'), soup.find_all('span', class_='css-1nfew2i eocu2m75'))):
        # print(items[0])
        # print(items[1])
        # print(items[2])
        tmpdict = {}
        src, name = items[0].contents[0].get('src'), items[0].contents[1]
        win_rate = float(items[1].contents[0])
        games = (items[2].contents[0].replace(',', ''))
        tmpdict['name'] = name
        tmpdict['src'] = src
        tmpdict['win_rate'] = win_rate
        tmpdict['games'] = games
        resultlist.append(tmpdict)
    return resultlist[0:10]


if __name__ == "__main__":
    '''
    names = ['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu', 'anivia',
             'annie', 'aphelios', 'ashe', 'aurelionsol', 'azir', 'bard', 'belveth',
             'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'chogath',
             'corki', 'darius', 'diana', 'drmundo', 'draven', 'ekko', 'elise',
             'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank',
             'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger',
             'illaoi', 'irelia', 'ivern', 'janna', 'jarvaniv', 'jax', 'jayce',
             'jhin', 'jinx', 'ksante', 'kaisa', 'kalista', 'karma', 'karthus',
             'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', 'khazix', 'kindred',
             'kled', 'kogmaw', 'leblanc', 'leesin', 'leona', 'lillia', 'lissandra',
             'lucian', 'lulu', 'lux', 'malphite', 'malzahar', 'maokai', 'masteryi',
             'missfortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko',
             'nidalee', 'nilah', 'nocturne', 'nunu', 'olaf', 'orianna', 'ornn',
             'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus',
             'reksai', 'rell', 'renata', 'renekton', 'rengar', 'riven', 'rumble',
             'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco',
             'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona',
             'soraka', 'swain', 'sylas', 'syndra', 'tahmkench', 'taliyah', 'talon',
             'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate', 
             '', '', '', '', '', '', '',
             'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate',
             'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate',
             'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate',]
    '''
    names = ['drmundo', 'fiora', 'aatrox', 'ksante', 'camille', 'mordekaiser',
             'darius', 'shen', 'gangplank', 'warwick', 'irelia', 'olaf', 'nasus', 'illaoi',
             'zac', 'singed', 'kled', 'jax', 'garen', 'sett', 'riven', 'malphite',
             'quinn', 'urgot', 'tryndamere', 'ornn', 'kayle', 'wukong', 'akshan', 'renekton', 'teemo',
             'pantheon', 'rengar', 'tahmkench', 'gwen', 'jayce', 'yorick', 'maokai', 'chogath', 'heimerdinger',
             'poppy', 'sion', 'gnar', 'yone', 'vayne', 'sejuani', 'lillia', 'volibear', 'gragas',
             'kennen', 'vladimir', 'rumble', 'yasuo', 'swain', 'graves', 'akali', 'trundle', 'ryze']

    # tier = ['all', 'challenger', 'grandmaster', 'master_plus', 'master',
    #         'diamond_plus', 'diamond', 'platinum_plus', 'platinum',
    #         'gold_plus', 'gold', 'silver', 'bronze', 'iron']

    tier = ['all', 'diamond', 'platinum', 'gold', 'silver']

    version = ['12.23', '12.22', '12.21']
    print('开始爬取opgg英雄联盟信息...')

    result = {}

    for sub_name in names:
        start_time = time.time()
        result[sub_name] = []
        for sub_version in version:
            for sub_tier in tier:
                print('----------正在爬取 英雄{} 版本{} 段位{} 信息--------'.format(sub_name, sub_version, sub_tier))
                tmp_res_dict = collect_build_data(sub_name, sub_tier, sub_version)
                result[sub_name].append(tmp_res_dict)
                print('爬取结果：',tmp_res_dict)
        print('爬取{}总耗时 {}s'.format(sub_name, (time.time() - start_time)))

    with open("../data/result2.json", "w", encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)  # 写为多行
