# -*- coding: utf-8 -*-
"""超级英雄观影清单构建器
- DATA: 手工整理的片单(片名/年份/宇宙/类型/分组/必要性/简介)。年份与片单据 Wikipedia 官方列表核对。
- 评分与海报由 OMDb 脚本回灌(enrich.py 写入 data/omdb_cache.json),此处不臆造。
- 运行: python build.py  ->  生成 index.html(自包含单文件)
tier: core=主线必看 rec=推荐 opt=可选 skip=衍生/可跳过
type: film / series / special
universe: mcu / dceu / dcu / elseworlds
"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))

def F(id, zh, en, year, universe, group, tier, note, syn, type="film"):
    return dict(id=id, title_zh=zh, title_en=en, year=year, universe=universe,
                group=group, tier=tier, note=note, synopsis=syn, type=type)

DATA = []

# ============ MCU 电影 · 无限传奇 (Infinity Saga) ============
DATA += [
 F("mcu-iron-man","钢铁侠","Iron Man",2008,"mcu","第一阶段","core",
   "整个宇宙的起点,不看无法理解托尼·斯塔克这条贯穿始终的主线。",
   "军火商托尼·斯塔克被绑架后造出动力装甲逃生,决心用钢铁侠的身份赎罪,拉开漫威宇宙序幕。"),
 F("mcu-incredible-hulk","无敌浩克","The Incredible Hulk",2008,"mcu","第一阶段","opt",
   "浩克后来换了演员,剧情关联很弱,想快速追主线可跳过,只看片尾彩蛋即可。",
   "科学家班纳博士为躲避军方追捕、寻找变身绿巨人的解药而流亡,漫威早期较独立的一部。"),
 F("mcu-iron-man-2","钢铁侠2","Iron Man 2",2010,"mcu","第一阶段","rec",
   "引入黑寡妇和神盾局'复仇者计划',是团队集结的重要铺垫。",
   "托尼身患重病又遭对手觊觎装甲技术,神盾局借机接触,为复仇者联盟埋线。"),
 F("mcu-thor","雷神","Thor",2011,"mcu","第一阶段","core",
   "索尔和洛基的起源,洛基是贯穿多部的关键反派/角色,必看。",
   "傲慢的神域王子索尔被贬下凡间学会谦卑,弟弟洛基则暗中夺权。"),
 F("mcu-cap-first-avenger","美国队长","Captain America: The First Avenger",2011,"mcu","第一阶段","core",
   "美队起源 + 宇宙魔方(空间宝石)首次登场,主线核心。",
   "二战期间瘦弱青年史蒂夫·罗杰斯接受超级士兵血清成为美国队长,对抗九头蛇。"),
 F("mcu-avengers","复仇者联盟","The Avengers",2012,"mcu","第一阶段","core",
   "第一次团队集结,第一阶段的收官,绝对必看。",
   "洛基入侵地球,神盾局召集钢铁侠、美队、雷神、浩克等组成复仇者联盟。"),
]
DATA += [
 F("mcu-iron-man-3","钢铁侠3","Iron Man 3",2013,"mcu","第二阶段","rec",
   "刻画纽约之战后托尼的创伤应激,理解他后续心态的关键。",
   "托尼在复联大战后深陷焦虑,又遭'满大人'恐怖袭击,独自面对危机。"),
 F("mcu-thor-dark-world","雷神2:黑暗世界","Thor: The Dark World",2013,"mcu","第二阶段","opt",
   "口碑偏弱,但引入现实宝石(以太),想集齐无限宝石线索可看。",
   "宇宙五族联结之际,黑暗精灵欲用以太之力毁灭世界,索尔联手洛基迎战。"),
 F("mcu-cap-winter-soldier","美国队长2:冬日战士","Captain America: The Winter Soldier",2014,"mcu","第二阶段","core",
   "神盾局崩塌、九头蛇渗透的重磅转折,深刻影响整个宇宙格局,必看。",
   "美队发现神盾局内部被九头蛇渗透,并撞上失忆的老友'冬日战士'。"),
 F("mcu-gotg","银河护卫队","Guardians of the Galaxy",2014,"mcu","第二阶段","core",
   "开辟宇宙侧故事线,引入力量宝石与灭霸背景,主线必看。",
   "星爵等一群边缘人组成银河护卫队,为争夺一颗神秘宝球对抗宇宙威胁。"),
 F("mcu-avengers-ultron","复仇者联盟2:奥创纪元","Avengers: Age of Ultron",2015,"mcu","第二阶段","core",
   "引入幻视、绯红女巫、快银,承接后续多条线,必看。",
   "托尼创造的人工智能奥创失控意图灭绝人类,复联再度集结。"),
 F("mcu-ant-man","蚁人","Ant-Man",2015,"mcu","第二阶段","rec",
   "引入量子领域,这是《终局之战》时间旅行和后续多元宇宙的关键设定。",
   "前小偷斯科特穿上能缩小的蚁人战衣,卷入一场高科技窃案。"),
]
DATA += [
 F("mcu-cap-civil-war","美国队长3:内战","Captain America: Civil War",2016,"mcu","第三阶段","core",
   "复联分裂的重大事件,引入黑豹和新蜘蛛侠,必看。",
   "因平民伤亡引发的监管争议,让复仇者分裂成美队和钢铁侠两派对抗。"),
 F("mcu-doctor-strange","奇异博士","Doctor Strange",2016,"mcu","第三阶段","core",
   "引入魔法与时间宝石,奇异博士是后续多元宇宙主线的核心,必看。",
   "傲慢的神经外科医生车祸失去双手,前往东方习得神秘魔法。"),
 F("mcu-gotg-2","银河护卫队2","Guardians of the Galaxy Vol. 2",2017,"mcu","第三阶段","rec",
   "深化护卫队成员关系与星爵身世,情感线重要但对主线非必需。",
   "护卫队一边被追杀一边探寻星爵的亲生父亲之谜。"),
 F("mcu-spiderman-homecoming","蜘蛛侠:英雄归来","Spider-Man: Homecoming",2017,"mcu","第三阶段","core",
   "蜘蛛侠个人线开端,与托尼的师徒情是重要情感线,必看。",
   "高中生彼得·帕克在钢铁侠指导下学做英雄,对抗军火贩秃鹫。"),
 F("mcu-thor-ragnarok","雷神3:诸神黄昏","Thor: Ragnarok",2017,"mcu","第三阶段","core",
   "索尔线关键转折,直接衔接《无限战争》开场,必看。",
   "索尔失去神锤、家园将亡,被困竞技星球,联手浩克逃出生天。"),
 F("mcu-black-panther","黑豹","Black Panther",2018,"mcu","第三阶段","core",
   "引入瓦坎达与振金,后续多次登场,主线必看。",
   "特查拉回国继承王位成为黑豹,却遭遇争夺王权的挑战者。"),
 F("mcu-infinity-war","复仇者联盟3:无限战争","Avengers: Infinity War",2018,"mcu","第三阶段","core",
   "灭霸集齐无限宝石的高潮,绝对核心,必看。",
   "灭霸为集齐六颗无限宝石横扫宇宙,全体英雄拼死阻止。"),
 F("mcu-ant-man-wasp","蚁人2:黄蜂女现身","Ant-Man and the Wasp",2018,"mcu","第三阶段","rec",
   "彩蛋与量子领域设定衔接《终局之战》,主线看彩蛋即可。",
   "蚁人与黄蜂女深入量子领域营救初代黄蜂女。"),
 F("mcu-captain-marvel","惊奇队长","Captain Marvel",2019,"mcu","第三阶段","rec",
   "惊奇队长起源,解释《无限战争》片尾呼叫她的伏笔,推荐看。",
   "1995年,失忆的克里战士卡罗尔逐渐找回自己是地球人惊奇队长的记忆。"),
 F("mcu-endgame","复仇者联盟4:终局之战","Avengers: Endgame",2019,"mcu","第三阶段","core",
   "无限传奇的终章,情感与剧情双高潮,绝对必看。",
   "幸存英雄用时间旅行逆转灭霸的响指,与命运做最后一搏。"),
 F("mcu-spiderman-ffh","蜘蛛侠:英雄远征","Spider-Man: Far From Home",2019,"mcu","第三阶段","core",
   "无限传奇正式收尾,直接引出后续蜘蛛侠身份危机,必看。",
   "彼得欧洲修学旅行途中被神盾局拉去对抗'神秘客',并面对失去导师的余痛。"),
]

# ============ MCU 电影 · 多元宇宙传奇 (Multiverse Saga) ============
DATA += [
 F("mcu-black-widow","黑寡妇","Black Widow",2021,"mcu","第四阶段","opt",
   "剧情设定在《内战》之后,是黑寡妇的补完与告别,对当前主线影响有限。",
   "娜塔莎在《内战》后逃亡期间回归自己的间谍'家庭',清算红房子的过往。"),
 F("mcu-shang-chi","尚气与十环传奇","Shang-Chi and the Legend of the Ten Rings",2021,"mcu","第四阶段","rec",
   "引入十环与新英雄尚气,后续会回归,推荐看。",
   "尚气逃离父亲的十环帮多年后被迫回归,直面家族的黑暗秘密。"),
 F("mcu-eternals","永恒族","Eternals",2021,"mcu","第四阶段","opt",
   "引入一批新神级角色,自成一体,与当前主线交集不多,可选。",
   "隐居地球数千年的永恒族在天神巨变来临时重新集结。"),
 F("mcu-spiderman-nwh","蜘蛛侠:英雄无归","Spider-Man: No Way Home",2021,"mcu","第四阶段","core",
   "正式打开多元宇宙,情怀与剧情双爆点,必看。",
   "彼得请奇异博士施咒抹除身份泄露的后果,却撕裂多元宇宙,引来历代反派。"),
 F("mcu-doctor-strange-2","奇异博士2:疯狂多元宇宙","Doctor Strange in the Multiverse of Madness",2022,"mcu","第四阶段","core",
   "多元宇宙主线关键,承接《旺达幻视》与《英雄无归》,必看。",
   "奇异博士护送能穿越宇宙的少女,对抗被暗黑魔典腐蚀的绯红女巫。"),
 F("mcu-thor-love-thunder","雷神4:爱与雷霆","Thor: Love and Thunder",2022,"mcu","第四阶段","opt",
   "索尔个人线延续,口碑分化,对主线影响不大,可选。",
   "索尔面对旧爱简变身女雷神,并对抗屠神者格尔。"),
 F("mcu-black-panther-2","黑豹2:瓦坎达万岁","Black Panther: Wakanda Forever",2022,"mcu","第四阶段","rec",
   "特查拉演员去世后的传承之作,引入海王纳摩,推荐看。",
   "瓦坎达在失去国王后,面对来自海底王国的新威胁并寻找新黑豹。"),
]
DATA += [
 F("mcu-quantumania","蚁人3:量子狂潮","Ant-Man and the Wasp: Quantumania",2023,"mcu","第五阶段","core",
   "正式引入大反派'征服者康',是《复联5》原定主线的关键铺垫,必看。",
   "蚁人一家误入量子领域,遭遇被流放的时间征服者康。"),
 F("mcu-gotg-3","银河护卫队3","Guardians of the Galaxy Vol. 3",2023,"mcu","第五阶段","rec",
   "护卫队的情感收官,火箭浣熊身世揭晓,系列粉必看。",
   "为救濒死的火箭浣熊,护卫队最后一次并肩,揭开它的悲惨来历。"),
 F("mcu-the-marvels","惊奇队长2","The Marvels",2023,"mcu","第五阶段","opt",
   "衔接《惊奇队长》《惊奇少女》《能量爆发》等剧集,主线影响有限,可选。",
   "惊奇队长、惊奇少女与莫妮卡三人力量纠缠、被迫换位并肩作战。"),
 F("mcu-deadpool-wolverine","死侍与金刚狼","Deadpool & Wolverine",2024,"mcu","第五阶段","rec",
   "死侍正式进入漫威宇宙、打通福斯变种人资产的标志作,推荐看。",
   "死侍拉上一个厌世版金刚狼,穿越多元宇宙拯救自己的世界线。"),
 F("mcu-cap-brave-new-world","美国队长4:美丽新世界","Captain America: Brave New World",2025,"mcu","第五阶段","rec",
   "山姆接棒美国队长的首部个人电影,衔接后续政治线,推荐看。",
   "新任美国队长山姆卷入一场牵动总统的国际阴谋。"),
 F("mcu-thunderbolts","雷霆特攻队","Thunderbolts*",2025,"mcu","第五阶段","core",
   "反英雄团队集结、直接引向《复联5》新阵容,必看。",
   "一群各怀过往的反英雄被迫组队,卷入一场政府阴谋。"),
]
DATA += [
 F("mcu-fantastic-four","神奇四侠:初露锋芒","The Fantastic Four: First Steps",2025,"mcu","第六阶段","core",
   "神奇四侠正式加入,第六阶段开篇、直通《复联5》,必看。",
   "在复古未来风的世界里,神奇四侠面对吞星与银影侠的威胁。"),
 F("mcu-spiderman-bnd","蜘蛛侠:新的一天","Spider-Man: Brand New Day",2026,"mcu","第六阶段","core",
   "蜘蛛侠新篇(2026年上映),主线延续,必看。",
   "在身份被世界遗忘之后,彼得·帕克重新开始他的英雄之路。"),
 F("mcu-avengers-doomsday","复仇者联盟5:末日决战","Avengers: Doomsday",2026,"mcu","第六阶段","core",
   "你复习的终点站——多元宇宙传奇的团队大集结,绝对必看。",
   "面对末日博士级别的全新威胁,横跨多元宇宙的英雄们再度集结。"),
 F("mcu-avengers-secret-wars","复仇者联盟6:秘密战争","Avengers: Secret Wars",2027,"mcu","第六阶段","core",
   "多元宇宙传奇的终章(2027年上映)。",
   "多元宇宙的命运走向终局之战。"),
]

# ============ MCU 剧集 · Disney+ 正史 (多元宇宙传奇) ============
DATA += [
 F("mcu-wandavision","旺达幻视","WandaVision",2021,"mcu","剧集·第四阶段","core",
   "直接引出《奇异博士2》的绯红女巫,主线关键,必看。",
   "旺达用魔法把小镇变成情景喜剧,借此逃避幻视之死的悲痛。","series"),
 F("mcu-tfatws","猎鹰与冬兵","The Falcon and the Winter Soldier",2021,"mcu","剧集·第四阶段","rec",
   "解释山姆如何接棒美国队长,是《美队4》的前置,推荐看。",
   "山姆与巴基联手对抗激进组织,山姆纠结是否接过美队盾牌。","series"),
 F("mcu-loki-s1","洛基 第一季","Loki (Season 1)",2021,"mcu","剧集·第四阶段","core",
   "引入时间变异管理局(TVA)与'征服者康',多元宇宙主线的总开关,必看。",
   "变体洛基被时间管理局抓获,被迫追捕另一个更危险的自己。","series"),
 F("mcu-what-if-s1","假如…? 第一季","What If...? (Season 1)",2021,"mcu","剧集·第四阶段","opt",
   "动画短片集,探索平行宇宙可能性,趣味补充,可选。",
   "旁观者观察者讲述一系列'如果历史走向不同'的多元宇宙故事。","series"),
 F("mcu-hawkeye","鹰眼","Hawkeye",2021,"mcu","剧集·第四阶段","opt",
   "引入新鹰眼凯特与金并(黑帮教父),支线人物铺垫,可选。",
   "克林特想赶回家过圣诞,却被卷入年轻射手凯特的麻烦里。","series"),
 F("mcu-moon-knight","月光骑士","Moon Knight",2022,"mcu","剧集·第四阶段","opt",
   "引入相对独立的新英雄月光骑士,与主线交集少,可选。",
   "患有分离性身份障碍的男子发现自己是埃及月神的化身。","series"),
 F("mcu-ms-marvel","惊奇少女","Ms. Marvel",2022,"mcu","剧集·第四阶段","rec",
   "引入卡玛拉,直接衔接《惊奇队长2》,想看那部就推荐先看。",
   "巴基斯坦裔美国少女卡玛拉获得超能力,成为惊奇队长的粉丝英雄。","series"),
 F("mcu-she-hulk","律政俏佳人绿巨人","She-Hulk: Attorney at Law",2022,"mcu","剧集·第四阶段","opt",
   "轻喜剧风格、打破第四面墙,支线角色,可选。",
   "律师珍妮弗意外获得绿巨人能力,一边打官司一边适应新身份。","series"),
 F("mcu-werewolf-night","狼人之夜","Werewolf by Night",2022,"mcu","剧集·第四阶段","opt",
   "黑白恐怖风特别篇,引入恐怖侧角色,可选。",
   "一群怪物猎人在葬礼之夜争夺一件神秘遗物。","special"),
 F("mcu-gotg-holiday","银河护卫队:圣诞特别篇","The Guardians of the Galaxy Holiday Special",2022,"mcu","剧集·第四阶段","opt",
   "轻松小品,衔接《银河护卫队3》,粉丝向,可选。",
   "护卫队想为星爵找回圣诞快乐,跑去地球绑架'传奇人物'。","special"),
]
DATA += [
 F("mcu-secret-invasion","秘密入侵","Secret Invasion",2023,"mcu","剧集·第五阶段","opt",
   "尼克·弗瑞主线,口碑偏弱,与《美队4》有关联,可选。",
   "弗瑞回到地球揭露变形斯克鲁人渗透人类社会的阴谋。","series"),
 F("mcu-loki-s2","洛基 第二季","Loki (Season 2)",2023,"mcu","剧集·第五阶段","core",
   "多元宇宙格局的定盘之作,直接决定《复联5》的世界观,必看。",
   "洛基在时间线崩解中拼命稳住多元宇宙,直面'征服者康'的真相。","series"),
 F("mcu-echo","回声","Echo",2024,"mcu","剧集·第五阶段","opt",
   "《鹰眼》衍生,街头英雄侧,较独立,可选。",
   "失聪的原住民杀手玛雅回到家乡,与犯罪教父金并决裂。","series"),
 F("mcu-agatha","阿加莎:一路同行","Agatha All Along",2024,"mcu","剧集·第五阶段","opt",
   "《旺达幻视》衍生,女巫题材,粉丝向,可选。",
   "失去法力的女巫阿加莎踏上'女巫之路'夺回力量。","series"),
 F("mcu-your-friendly-spiderman","我们身边的蜘蛛侠","Your Friendly Neighborhood Spider-Man",2025,"mcu","剧集·第六阶段","opt",
   "动画剧集,重述蜘蛛侠早期成长,较独立,可选。",
   "动画视角讲述彼得·帕克成为蜘蛛侠的另一种起点。","series"),
 F("mcu-daredevil-born-again","超胆侠:重生","Daredevil: Born Again",2025,"mcu","剧集·第六阶段","rec",
   "把Netflix《超胆侠》正式并入主宇宙,街头英雄线的重头,推荐看。",
   "盲人律师马特与市长金并在纽约展开法律与暴力的对决。","series"),
 F("mcu-ironheart","钢铁之心","Ironheart",2025,"mcu","剧集·第六阶段","opt",
   "《黑豹2》衍生,引入新天才少女钢铁之心,可选。",
   "天才少女莉莉造出比肩钢铁侠的战衣,却卷入魔法与科技的冲突。","series"),
]

# ============ MCU 衍生 · 了解向(早期剧集,基本可跳过) ============
DATA += [
 F("mcu-agents-shield","神盾局特工","Agents of S.H.I.E.L.D.",2013,"mcu","衍生·了解向","skip",
   "曾与电影松散联动(尤其配合《冬日战士》),后期基本独立,可跳过不影响主线。",
   "科尔森探员带领神盾局小队处理各种超自然与外星威胁,共7季。","series"),
 F("mcu-agent-carter","特工卡特","Agent Carter",2015,"mcu","衍生·了解向","skip",
   "美队旧爱佩姬的战后故事,情怀向,对当前主线无影响,可跳过。",
   "二战后佩姬·卡特一边被职场轻视一边执行秘密任务。","series"),
 F("mcu-daredevil-netflix","超胆侠(网飞版)","Daredevil (Netflix)",2015,"mcu","衍生·了解向","skip",
   "Netflix街头英雄宇宙,现已被《超胆侠:重生》接续,想追新版可选看老版。",
   "盲人律师马特白天打官司、夜晚化身超胆侠惩恶,共3季。","series"),
 F("mcu-jessica-jones","杰西卡·琼斯","Jessica Jones",2015,"mcu","衍生·了解向","skip",
   "Netflix街头线,较独立,可跳过。",
   "有超能力的私家侦探杰西卡对抗能操控人心的反派。","series"),
 F("mcu-luke-cage","卢克·凯奇","Luke Cage",2016,"mcu","衍生·了解向","skip",
   "Netflix街头线,较独立,可跳过。",
   "刀枪不入的卢克·凯奇守护哈莱姆街区。","series"),
 F("mcu-iron-fist","铁拳","Iron Fist",2017,"mcu","衍生·了解向","skip",
   "Netflix街头线,口碑偏弱,可跳过。",
   "富家子丹尼掌握'铁拳'武学归来夺回家族企业。","series"),
 F("mcu-defenders","捍卫者联盟","The Defenders",2017,"mcu","衍生·了解向","skip",
   "Netflix四位街头英雄的集结,粉丝向,可跳过。",
   "超胆侠、杰西卡、卢克与铁拳联手对抗'手'组织。","series"),
 F("mcu-punisher","惩罚者","The Punisher",2017,"mcu","衍生·了解向","skip",
   "Netflix街头线,暴力风格,可跳过。",
   "退伍军人弗兰克为家人复仇,化身惩罚者。","series"),
]

# ============ DC · DCEU 老宇宙 (2013-2023, 主追线) ============
DATA += [
 F("dc-man-of-steel","超人:钢铁之躯","Man of Steel",2013,"dceu","DCEU 主线","core",
   "DCEU的起点,超人起源,主追线必看。",
   "克里斯托弗从氪星孤儿成长为地球守护者超人,对抗同族反派佐德将军。"),
 F("dc-bvs","蝙蝠侠大战超人:正义黎明","Batman v Superman: Dawn of Justice",2016,"dceu","DCEU 主线","core",
   "引入蝙蝠侠、神奇女侠,搭建正义联盟,必看。",
   "蝙蝠侠视超人为威胁而与之对决,幕后黑手却在酝酿更大阴谋。"),
 F("dc-suicide-squad","自杀小队","Suicide Squad",2016,"dceu","DCEU 主线","opt",
   "引入哈莉·奎茵等反派团队,口碑偏弱,对主线影响有限,可选。",
   "政府招募一群被关押的超级罪犯执行敢死任务。"),
 F("dc-wonder-woman","神奇女侠","Wonder Woman",2017,"dceu","DCEU 主线","core",
   "DCEU口碑最佳之一,神奇女侠起源,必看。",
   "亚马逊公主戴安娜离开神秘岛,投身第一次世界大战拯救人类。"),
 F("dc-justice-league","正义联盟","Justice League",2017,"dceu","DCEU 主线","rec",
   "DCEU的团队集结(院线版口碑一般),想追主线推荐看。",
   "超人牺牲后,蝙蝠侠召集神奇女侠、闪电侠、海王与钢骨对抗荒原狼。"),
 F("dc-zsjl","扎克·施奈德版正义联盟","Zack Snyder's Justice League",2021,"dceu","DCEU 主线","opt",
   "院线版《正义联盟》的4小时导演剪辑版,内容更完整但很长,二选一即可。",
   "导演原始版本的正义联盟,情节与角色刻画大幅扩展,片长约4小时。"),
 F("dc-aquaman","海王","Aquaman",2018,"dceu","DCEU 主线","rec",
   "DCEU票房最高,海王个人线,推荐看。",
   "半人半亚特兰蒂斯血统的亚瑟争夺海底王位,阻止兄弟发动海陆战争。"),
 F("dc-shazam","雷霆沙赞!","Shazam!",2019,"dceu","DCEU 主线","opt",
   "轻松合家欢风格,较独立,可选。",
   "寄养少年比利喊出'沙赞'即可变身成大人超级英雄。"),
 F("dc-birds-of-prey","猛禽小队","Birds of Prey",2020,"dceu","DCEU 主线","opt",
   "哈莉·奎茵衍生,较独立,可选。",
   "与小丑分手的哈莉组建女性团队对抗黑面具。"),
 F("dc-ww-1984","神奇女侠1984","Wonder Woman 1984",2020,"dceu","DCEU 主线","opt",
   "神奇女侠续作,口碑不及前作,对主线影响有限,可选。",
   "冷战年代的戴安娜面对能实现愿望却索取代价的反派。"),
 F("dc-suicide-squad-2021","X特遣队:全员集结","The Suicide Squad",2021,"dceu","DCEU 主线","rec",
   "James Gunn执导的软重启,引入和平使者(后延续到新DCU),推荐看。",
   "新一批超级罪犯被派往小岛摧毁一处纳粹时期实验设施。"),
 F("dc-black-adam","黑亚当","Black Adam",2022,"dceu","DCEU 主线","opt",
   "巨石强森主演,原计划开新线但已随重启作废,较独立,可选。",
   "沉睡数千年的黑亚当苏醒,以暴制暴令正义社会不安。"),
 F("dc-shazam-2","雷霆沙赞!众神之怒","Shazam! Fury of the Gods",2023,"dceu","DCEU 主线","opt",
   "沙赞续作,较独立,可选。",
   "沙赞一家面对愤怒的希腊众神之女。"),
 F("dc-the-flash","闪电侠","The Flash",2023,"dceu","DCEU 主线","rec",
   "用多元宇宙'重置'了DCEU时间线,是老宇宙收尾、通向新DCU的关键,推荐看。",
   "闪电侠回到过去改写母亲之死,却撕裂时间线、引发多元宇宙危机。"),
 F("dc-blue-beetle","蓝甲虫","Blue Beetle",2023,"dceu","DCEU 主线","opt",
   "主角蓝甲虫会延续到新DCU,但本片较独立,可选。",
   "墨西哥裔青年海梅意外与外星圣甲虫结合,获得蓝甲虫战甲。"),
 F("dc-aquaman-2","海王2:失落的王国","Aquaman and the Lost Kingdom",2023,"dceu","DCEU 主线","opt",
   "DCEU的收官之作,较独立,可选。",
   "海王联手宿敌弟弟对抗手握黑暗三叉戟的复仇者黑蝠鲼。"),
]

# ============ DC · 新 DCU (2024起, James Gunn 重启, 全新未来线) ============
DATA += [
 F("dcu-creature-commandos","怪物特工队","Creature Commandos",2024,"dcu","DCU·诸神与怪物","rec",
   "新DCU的开篇(动画剧集),James Gunn亲写,想追新宇宙从这里起,推荐看。",
   "沃勒组建一支怪物特攻队执行秘密任务,新DCU正式开张。","series"),
 F("dcu-superman","超人","Superman",2025,"dcu","DCU·诸神与怪物","core",
   "新DCU真正意义上的起点电影,重塑超人,想追新宇宙必看。",
   "全新版本的超人在人性与神性、理想与现实之间寻找自己的位置。"),
 F("dcu-peacemaker-s2","和平使者 第二季","Peacemaker (Season 2)",2025,"dcu","DCU·诸神与怪物","rec",
   "第一季属老宇宙、第二季正式并入新DCU,承前启后,推荐看。",
   "和平使者在新的宇宙格局下继续他啼笑皆非又暴力的'和平'事业。","series"),
 F("dcu-supergirl","超女","Supergirl",2026,"dcu","DCU·诸神与怪物","rec",
   "2026年上映(上映日期请以官方为准),新DCU重要一环,推荐看。",
   "比超人更沧桑的少女超女,踏上一段充满酒气与复仇的太空冒险。"),
 F("dcu-lanterns","绿灯军团","Lanterns",2026,"dcu","DCU·诸神与怪物","opt",
   "2026年HBO剧集(上映时间请以官方为准),侦探悬疑风的绿灯侠,可选。",
   "两代绿灯侠像'真探'一样在地球调查一桩牵动宇宙的谋杀案。","series"),
 F("dcu-clayface","黏土脸","Clayface",2026,"dcu","DCU·诸神与怪物","opt",
   "2026年恐怖片方向(上映时间请以官方为准),较独立,可选。",
   "一名演员因实验变成能任意变形的怪物黏土脸。"),
]

# ============ DC · 独立/非宇宙 (Elseworlds, 了解向精品) ============
DATA += [
 F("dc-joker","小丑","Joker",2019,"elseworlds","独立·Elseworlds","rec",
   "不属于任何连续宇宙,独立神作,拿下威尼斯金狮与奥斯卡,单独看即可,强烈推荐。",
   "潦倒的喜剧演员亚瑟在冷漠社会中一步步堕落为小丑。"),
 F("dc-joker-2","小丑2:双重妄想","Joker: Folie à Deux",2024,"elseworlds","独立·Elseworlds","opt",
   "《小丑》续作,歌舞片形式,口碑分化,可选。",
   "被关押受审的亚瑟遇见同样疯狂的哈莉,陷入一段妄想恋曲。"),
 F("dc-the-batman","新蝙蝠侠","The Batman",2022,"elseworlds","独立·Elseworlds","rec",
   "马特·里夫斯执导的独立蝙蝠侠线(帕丁森版),黑色侦探风,自成一体,强烈推荐。",
   "上任第二年的蝙蝠侠追查连环杀手谜语人,揭开哥谭腐败的黑幕。"),
]

# ============ 剧情时间线顺序 (仅供参考, MCU 官方时间线本身存在争议) ============
CHRONO = {}
def set_chrono(ids):
    for i, _id in enumerate(ids):
        CHRONO[_id] = i

# MCU 时间线(电影为主, 关键剧集插入; 大致推断)
set_chrono([
 "mcu-cap-first-avenger","mcu-captain-marvel","mcu-iron-man","mcu-iron-man-2",
 "mcu-incredible-hulk","mcu-thor","mcu-avengers","mcu-iron-man-3",
 "mcu-thor-dark-world","mcu-cap-winter-soldier","mcu-gotg","mcu-gotg-2",
 "mcu-avengers-ultron","mcu-ant-man","mcu-cap-civil-war","mcu-black-widow",
 "mcu-spiderman-homecoming","mcu-doctor-strange","mcu-black-panther","mcu-thor-ragnarok",
 "mcu-ant-man-wasp","mcu-infinity-war","mcu-endgame",
 "mcu-wandavision","mcu-tfatws","mcu-loki-s1","mcu-what-if-s1","mcu-spiderman-ffh",
 "mcu-shang-chi","mcu-eternals","mcu-hawkeye","mcu-spiderman-nwh",
 "mcu-moon-knight","mcu-ms-marvel","mcu-doctor-strange-2","mcu-thor-love-thunder",
 "mcu-she-hulk","mcu-werewolf-night","mcu-black-panther-2","mcu-gotg-holiday",
 "mcu-quantumania","mcu-gotg-3","mcu-secret-invasion","mcu-loki-s2","mcu-echo",
 "mcu-the-marvels","mcu-agatha","mcu-ironheart","mcu-deadpool-wolverine",
 "mcu-daredevil-born-again","mcu-cap-brave-new-world","mcu-thunderbolts",
 "mcu-your-friendly-spiderman","mcu-fantastic-four","mcu-spiderman-bnd",
 "mcu-avengers-doomsday","mcu-avengers-secret-wars",
])
# DCEU 时间线
set_chrono([
 "dc-wonder-woman","dc-ww-1984","dc-man-of-steel","dc-bvs","dc-suicide-squad",
 "dc-justice-league","dc-zsjl","dc-aquaman","dc-shazam","dc-birds-of-prey",
 "dc-suicide-squad-2021","dc-black-adam","dc-shazam-2","dc-blue-beetle",
 "dc-the-flash","dc-aquaman-2",
])

TIER_META = {
 "core": {"label":"主线必看","color":"#e5484d","dot":"🔴"},
 "rec":  {"label":"推荐",    "color":"#f5a623","dot":"🟡"},
 "opt":  {"label":"可选",    "color":"#9aa0a6","dot":"⚪"},
 "skip": {"label":"衍生/可跳过","color":"#5c6066","dot":"⚫"},
}
UNIVERSE_META = {
 "mcu":{"label":"漫威 MCU","short":"MCU","color":"#e23636",
   "full":"Marvel Cinematic Universe","cn":"漫威电影宇宙",
   "gloss":"迪士尼/漫威影业旗下的主线连续宇宙，2008《钢铁侠》开启，含无限传奇、多元宇宙传奇及 Disney+ 正史剧集。"},
 "dceu":{"label":"DC 老宇宙 (DCEU)","short":"DCEU","color":"#0476f2",
   "full":"DC Extended Universe","cn":"DC 扩展宇宙",
   "gloss":"华纳 2013《超人：钢铁之躯》至 2023《海王2》的旧连续宇宙，现已终结，被 DCU 取代。"},
 "dcu":{"label":"DC 新宇宙 (DCU)","short":"DCU","color":"#00a8e1",
   "full":"DC Universe","cn":"DC 新宇宙",
   "gloss":"James Gunn 与 Peter Safran 2024 年起主导的重启宇宙，2025《超人》为大银幕开篇。"},
 "elseworlds":{"label":"DC 独立 (Elseworlds)","short":"独立","color":"#8b5cf6",
   "full":"Elseworlds","cn":"独立故事",
   "gloss":"不属于任何连续宇宙的独立 DC 影片，如《小丑》系列、《新蝙蝠侠》，各讲各的、互不联动。"},
}
ALL_GLOSS = "本页按四个宇宙归类：MCU 漫威电影宇宙、DCEU DC 老宇宙、DCU DC 新宇宙、独立 Elseworlds。点上方任一标签可看该宇宙的全称与说明。"
TYPE_META = {"film":"电影","series":"剧集","special":"特别篇"}

def enrich():
    """合并 OMDb 缓存(海报+评分); 无缓存则字段为空。"""
    cache_path = os.path.join(HERE, "data", "omdb_cache.json")
    cache = {}
    if os.path.exists(cache_path):
        cache = json.load(open(cache_path, encoding="utf-8"))
    for d in DATA:
        c = cache.get(d["id"], {})
        d["poster"] = c.get("poster")
        d["imdb"] = c.get("imdb")
        d["rt"] = c.get("rt")
        d["metacritic"] = c.get("metacritic")
        d["chrono"] = CHRONO.get(d["id"], 999)
        d["saga"], d["sagaKey"] = saga_of(d)

SAGA_META = {
 "infinity":  {"zh":"无限传奇",   "en":"The Infinity Saga",    "sub":"第一~三阶段 · 2008–2019", "color":"#e23636","order":1},
 "multiverse":{"zh":"多元宇宙传奇","en":"The Multiverse Saga",   "sub":"第四~六阶段 · 2021–2027", "color":"#b0203a","order":2},
 "mcu-legacy":{"zh":"漫威衍生宇宙","en":"Legacy / Street-Level", "sub":"早期联动剧集 · 了解向",   "color":"#7a2a2a","order":3},
 "dceu":      {"zh":"DC 扩展宇宙", "en":"DC Extended Universe",  "sub":"老宇宙 · 2013–2023",     "color":"#0476f2","order":4},
 "dcu":       {"zh":"DC 新宇宙",   "en":"DC Universe",           "sub":"James Gunn 重启 · 2024–","color":"#00a8e1","order":5},
 "elseworlds":{"zh":"独立故事",    "en":"Elseworlds",            "sub":"不属于任何连续宇宙",     "color":"#8b5cf6","order":6},
}

def saga_of(d):
    if d["universe"] == "mcu":
        if d["group"].startswith("衍生"): return SAGA_META["mcu-legacy"], "mcu-legacy"
        if d["group"] in ("第一阶段","第二阶段","第三阶段"): return SAGA_META["infinity"], "infinity"
        return SAGA_META["multiverse"], "multiverse"
    return SAGA_META[d["universe"]], d["universe"]

def render():
    enrich()
    logos = {}
    logos_path = os.path.join(HERE, "data", "logos.json")
    if os.path.exists(logos_path):
        logos = json.load(open(logos_path, encoding="utf-8"))
    banners = {}
    banners_path = os.path.join(HERE, "data", "banners.json")
    if os.path.exists(banners_path):
        banners = json.load(open(banners_path, encoding="utf-8"))
    payload = {
        "titles": DATA,
        "tierMeta": TIER_META,
        "universeMeta": UNIVERSE_META,
        "typeMeta": TYPE_META,
        "sagaMeta": SAGA_META,
        "logos": logos,
        "banners": banners,
        "allGloss": ALL_GLOSS,
        "updated": "2026-09-28",
    }
    data_json = json.dumps(payload, ensure_ascii=False)
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    out = tpl.replace("/*__PAYLOAD__*/", data_json)
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)
    n = len(DATA)
    filled = len([d for d in DATA if d.get("poster")])
    print(f"index.html 生成完毕: {n} 部, 已带海报 {filled} 部")

if __name__ == "__main__":
    render()
