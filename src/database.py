#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：OPGG 
@File    ：database.py
@IDE     ：PyCharm 
@Author  ：离开流沙河的坚定大土豆
@Date    ：2022/12/24 11:22 
'''
import csv
import json

name_dict = {"暗裔剑魔":"aatrox",
"九尾妖狐":"ahri",
"离群之刺":"akali",
"牛头酋长":"alistar",
"殇之木乃伊":"amumu",
"冰晶凤凰":"anivia","影哨":"akshan",
"黑暗之女":"annie","残月之肃":"aphelios",
"寒冰射手":"ashe",
"铸星龙王":"aurelionsol",
"沙漠皇帝":"azir",
"星界游神":"bard","虚空女皇":"belveth",
"蒸汽机器人":"blitzcrank",
"复仇焰魂":"brand",
"弗雷尔卓德之心":"braum",
"皮城女警":"caitlyn","青钢影":"camille",
"魔蛇之拥":"cassiopeia",
"虚空恐惧":"chogath",
"英勇投弹手":"corki",
"诺克萨斯之手":"darius",
"皎月女神":"diana",
"祖安狂人":"drmundo",
"荣耀行刑官":"draven",
"时间刺客":"ekko",
"蜘蛛女皇":"elise",
"痛苦之拥":"evelynn",
"探险家":"ezreal",
"远古恐惧":"fiddlesticks",
"无双剑姬":"fiora",
"潮汐海灵":"fizz",
"哨兵之殇":"galio",
"海洋之灾":"gangplank",
"德玛西亚之力":"garen",
"迷失之牙":"gnar",
"酒桶":"gragas",
"法外狂徒":"graves",
"战争之影":"hecarim","灵罗娃娃":"gwen",
"大发明家":"heimerdinger",
"海兽祭司":"illaoi",
"刀锋舞者":"irelia",
"翠神":"ivern",
"风暴之怒":"janna",
"德玛西亚皇子":"jarvaniv",
"武器大师":"jax",
"未来守护者":"jayce",
"戏命师":"jhin",
"暴走萝莉":"jinx","纳祖芒荣耀":"ksante","虚空之女":"kaisa",
"复仇之矛":"kalista",
"天启者":"karma",
"死亡颂唱者":"karthus",
"虚空行者":"kassadin",
"不祥之刃":"katarina",
"审判天使":"kayle","影流之镰":"kayn",
"狂暴之心":"kennen",
"虚空掠夺者":"khazix",
"永猎双子":"kindred",
"暴怒骑士":"kled",
"深渊巨口":"kogmaw",
"诡术妖姬":"leblanc",
"盲僧":"leesin",
"曙光女神":"leona","含羞蓓蕾":"lillia",
"冰霜女巫":"lissandra",
"圣枪游侠":"lucian",
"仙灵女巫":"lulu",
"光辉女郎":"lux",
"熔岩巨兽":"malphite",
"虚空先知":"malzahar",
"扭曲树精":"maokai",
"无极剑圣":"masteryi",
"赏金猎人":"missfortune",
"铁铠冥魂":"mordekaiser",
"堕落天使":"morgana",
"唤潮鲛姬":"nami",
"沙漠死神":"nasus",
"深海泰坦":"nautilus","万花通灵":"neeko",
"狂野女猎手":"nidalee","不羁之悦":"nilah",
"永恒梦魇":"nocturne",
"雪人骑士":"nunu",
"狂战士":"olaf",
"发条魔灵":"orianna","山隐之焰":"ornn",
"战争之王":"pantheon","血港鬼影":"pyke",
"钢铁大使":"poppy","元素女皇":"qiyana",
"德玛西亚之翼":"quinn",
"披甲龙龟":"rammus","幻翎":"rakan",
"虚空遁地兽":"reksai","炼金男爵":"renata","镕铁少女":"rell",
"荒漠屠夫":"renekton",
"傲之追猎者":"rengar",
"放逐之刃":"riven",
"机械公敌":"rumble",
"符文法师":"ryze","沙漠玫瑰":"samira",
"北地之怒":"sejuani","腕豪":"sett","星籁歌姬":"seraphine","涤魂圣枪":"senna",
"恶魔小丑":"shaco",
"暮光之眼":"shen",
"龙血武姬":"shyvana",
"炼金术士":"singed",
"亡灵战神":"sion",
"战争女神":"sivir",
"水晶先锋":"skarner",
"琴瑟仙女":"sona",
"众星之子":"soraka",
"诺克萨斯统领":"swain","解脱者":"sylas",
"暗黑元首":"syndra",
"岩雀":"taliyah",
"刀锋之影":"talon",
"河流之王":"tahmkench",
"宝石骑士":"taric",
"迅捷斥候":"teemo",
"魂锁典狱长":"thresh",
"麦林炮手":"tristana",
"巨魔之王":"trundle",
"蛮族之王":"tryndamere",
"卡牌大师":"twistedfate",
"瘟疫之源":"twitch",
"兽灵行者":"udyr",
"首领之傲":"urgot",
"惩戒之箭":"varus",
"暗夜猎手":"vayne",
"邪恶小法师":"veigar",
"虚空之眼":"velkoz","愁云使者":"vex",
"皮城执法官":"vi","破败之王":"viego",
"机械先驱":"viktor",
"猩红收割者":"vladimir",
"雷霆咆哮":"volibear",
"祖安怒兽":"warwick",
"齐天大圣":"wukong","逆羽":"xayah",
"远古巫灵":"xerath",
"德邦总管":"xinzhao",
"疾风剑豪":"yasuo","封魔剑魂":"yone",
"牧魂人":"yorick","魔法猫咪":"yuumi",
"生化魔人":"zac",
"影流之主":"zed","祖安花火":"zeri",
"爆破鬼才":"ziggs",
"时光守护者":"zilean","暮光星灵":"zoe",
"荆棘之兴":"zyra"}

top_names = ['drmundo', 'fiora', 'aatrox', 'ksante', 'camille', 'mordekaiser',
             'darius', 'shen', 'gangplank', 'warwick', 'irelia', 'olaf', 'nasus', 'illaoi',
             'zac', 'singed', 'kled', 'jax', 'garen', 'sett', 'riven', 'malphite',
             'quinn', 'urgot', 'tryndamere', 'ornn', 'kayle', 'wukong', 'akshan', 'renekton', 'teemo',
             'pantheon', 'rengar', 'tahmkench', 'gwen', 'jayce', 'yorick', 'maokai', 'chogath', 'heimerdinger',
             'poppy', 'sion', 'gnar', 'yone', 'vayne', 'sejuani', 'lillia', 'volibear', 'gragas',
             'kennen', 'vladimir', 'rumble', 'yasuo', 'swain', 'graves', 'akali', 'trundle', 'ryze']


def json2list(data):
    result = []
    for champion_name, value in data.items():
        print(champion_name)
        for i, item_1 in enumerate(value):
            # print(i)
            # print(item_1['region'])
            # print(item_1['tier'])
            # print(item_1['patch'])
            for j, subitem in enumerate(item_1['positions'].items()):
                # print(j)
                # print(subitem[0])
                # print(subitem[1]['level'])
                # print(subitem[1]['win_rate'])
                # print(subitem[1]['pick_rate'])
                # print(subitem[1]['ban_rate'])
                # tmp_result = [champion_name, item_1['region'], item_1['tier'], item_1['patch'], subitem[0], subitem[1]['level'], subitem[1]['win_rate'], subitem[1]['pick_rate'], subitem[1]['ban_rate']]
                tmp_result = [champion_name, item_1['tier'], item_1['patch'], subitem[0]]
                tmp_dict = {}
                for counter in subitem[1]['counters']:
                    # print(counter['name'])
                    # print(counter['src'])
                    # print(counter['win_rate'])
                    # print(counter['games'])
                    # tmp_result.append(name_dict[counter['name']])
                    # tmp_result.append(counter['win_rate'])
                    # tmp_result.append(counter['games'])
                    tmp_dict[name_dict[counter['name']]] = counter['win_rate']
                tmp_result.append(tmp_dict)
                # if len(subitem[1]['counters']) != 10:
                #     for i in range(0, 10 - len(subitem[1]['counters'])):
                #         tmp_result.append('')
                #         tmp_result.append('')
                #         tmp_result.append('')
                # for equip in subitem[1]['equipments']:
                #     print(equip['equip'])
                #     string = ','
                #     print(string.join(equip['equip']))
                #     tmp_result.append(string.join(equip['equip']))
                #     print(equip['pick_rate'])
                #     tmp_result.append(equip['pick_rate'])
                result.append(tmp_result)
                print(tmp_result)
    print(len(result))
    return result


if __name__ == "__main__":
    path = '../data/result2.json'
    with open(path, 'rb') as load_f:
        load_dict = json.load(load_f)
    # result = json2list(load_dict)

    nums = 0
    for key, item in load_dict.items():
        for i in item:
            nums += 1

    print(nums)

    # nums = 0

    # tmp_names_21 = []
    # tmp_names_22 = []
    # tmp_names_23 = []
    # result1 = []
    # result2 = []
    # result3 = []
    # for item in result:
    #     if item[1] == 'diamond' and item[2] == '12.21' and item[3] == 'top' and item[0] not in tmp_names_21:
    #         tmp_names_21.append(item[0])
    #     if item[1] == 'diamond' and item[2] == '12.22' and item[3] == 'top' and item[0] not in tmp_names_22:
    #         tmp_names_22.append(item[0])
    #     if item[1] == 'diamond' and item[2] == '12.23' and item[3] == 'top' and item[0] not in tmp_names_23:
    #         tmp_names_23.append(item[0])
    # print(len(tmp_names_21))
    # print(len(tmp_names_22))
    # print(len(tmp_names_23))
    # for item in result:
    #     tmp_list21 = []
    #     res_dict_21 = {}
    #     if item[1] == 'diamond' and item[2] == '12.21' and item[3] == 'top':
    #         for key, value in enumerate(sorted(item[-1].items(), key = lambda kv:(kv[1], kv[0]), reverse=True)):
    #             if value[0] in tmp_names_21:
    #                 tmp_list21.append('top.'+value[0])
    #         res_dict_21['name'] = 'top.' + item[0]
    #         res_dict_21['strongAgainst'] = tmp_list21
    #         result1.append(res_dict_21)
    #
    #     tmp_list22 = []
    #     res_dict_22 = {}
    #     if item[1] == 'diamond' and item[2] == '12.22' and item[3] == 'top':
    #         for key, value in enumerate(sorted(item[-1].items(), key=lambda kv: (kv[1], kv[0]), reverse=True)):
    #             if value[0] in tmp_names_22:
    #                 tmp_list22.append('top.' + value[0])
    #         res_dict_22['name'] = 'top.' + item[0]
    #         res_dict_22['strongAgainst'] = tmp_list22
    #         result2.append(res_dict_22)
    #
    #     tmp_list23 = []
    #     res_dict_23 = {}
    #     if item[1] == 'diamond' and item[2] == '12.23' and item[3] == 'top':
    #         for key, value in enumerate(sorted(item[-1].items(), key=lambda kv: (kv[1], kv[0]), reverse=True)):
    #             if value[0] in tmp_names_23:
    #                 tmp_list23.append('top.' + value[0])
    #         res_dict_23['name'] = 'top.' + item[0]
    #         res_dict_23['strongAgainst'] = tmp_list23
    #         result3.append(res_dict_23)
    # print(result1)
    # print(result2)
    # print(result3)
    #
    # with open("../data/view1_diamond_1221.json", "w", encoding='utf-8') as f:
    #     json.dump(result1, f, indent=2, ensure_ascii=False)  # 写为多行
    # with open("../data/view1_diamond_1222.json", "w", encoding='utf-8') as f:
    #     json.dump(result2, f, indent=2, ensure_ascii=False)  # 写为多行
    # with open("../data/view1_diamond_1223.json", "w", encoding='utf-8') as f:
    #     json.dump(result3, f, indent=2, ensure_ascii=False)  # 写为多行




    # with open('../data/database2.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     # 先写入columns_name
    #     writer.writerow(["champion_name", "region", 'tier', 'patch', 'position', 'level',
    #                      'win_rate', 'pick_rate', 'ban_rate', 'counters1_name', 'counters1_win_rate', 'counters1_games',
    #                      'counters2_name', 'counters2_win_rate', 'counters2_games', 'counters3_name', 'counters3_win_rate', 'counters3_games',
    #                      'counters4_name', 'counters4_win_rate', 'counters4_games',
    #                      'counters5_name', 'counters5_win_rate', 'counters5_games',
    #                      'counters6_name', 'counters6_win_rate', 'counters6_games',
    #                      'counters7_name', 'counters7_win_rate', 'counters7_games',
    #                      'counters8_name', 'counters8_win_rate', 'counters8_games',
    #                      'counters9_name', 'counters9_win_rate', 'counters9_games',
    #                      'counters10_name', 'counters10_win_rate', 'counters10_games',
    #                      'equip1_name', 'equip1_pick_rate', 'equip2_name', 'equip2_pick_rate',
    #                      'equip3_name', 'equip3_pick_rate', 'equip4_name', 'equip4_pick_rate',
    #                      'equip5_name', 'equip5_pick_rate'])
    #     # 写入多行用writerows
    #     writer.writerows(result)
