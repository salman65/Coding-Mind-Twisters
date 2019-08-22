import ipdb


def rti(r):
    s = r.split('-')
    return (int(s[0]), int(s[1]))


def is_ol(r1, r2):
    s1 = rti(r1)
    s2 = rti(r2)
    if s1[0] <= s2[0] and s1[1] >= s2[1]:
        return (r1, "r1")
    elif s2[0] <= s1[0] and s2[1] >= s1[1]:
        return (r2, "r2")
    elif s1[0] <= s2[0] and (s1[1] >= s2[0] and s1[1] <= s2[1]):
        return (r2, "r1-r2")
    elif s2[0] <= s1[0] and (s2[1] >= s1[0] and s2[1] <= s1[1]):
        return (r2, "r2-r1")
    else:
        return (r2, None)


def is_empty(dic):
    return len(dic.keys()) == 0


def solution(positions):
        res = {}
        ans = []
        pr = f"{positions[0][0]}-{positions[0][0]+positions[0][1]-1}"
        res[pr] = positions[0][1]
        ans.append(positions[0][1])
        max_calc = positions[0][1]
        for pos in positions[1:]:
            pr = f"{pos[0]}-{pos[0]+pos[1]-1}"
            calc = None
            for item in sorted(res, key=res.get, reverse=True):
                ol = is_ol(item, pr)
                if ol[1] == "r2-r1" or ol[1] == "r1-r2":
                    res[ol[0]] = res[item] + pos[1]
                    calc = res[ol[0]]
                    break
                elif ol[1] == "r2":
                    res[ol[0]] = res[item] + pos[1]
                    res.pop(item, None)
                    calc = res[ol[0]]
                    break
                elif ol[1] == "r1":
                    res[pr] = res[item] + pos[1]
                    calc = res[pr]
                    break
                else:
                    res[ol[0]] = pos[1]
                    calc = res[ol[0]]
            if calc > max_calc:
                ans.append(calc)
                max_calc = calc
            else:
                ans.append(max_calc)
        return ans

q = [[13259169,614936],[633696,602282],[34120526,531664],[909832,846630],[5790720,608795],[50628732,941784],[13382424,834960],[3596245,629947],[11687192,602370],[20752810,532662],[3661596,662521],[389620,544310],[7276211,680822],[25400940,724224],[72010620,534619],[28823814,532085],[65363118,525203],[32558064,542361],[28662822,653781],[46168239,608501],[19230438,996255],[11325145,983261],[53008956,825525],[29985984,828506],[4259255,566068],[13064058,945083],[14911314,862276],[31666647,736232],[18493605,987495],[33962139,870960],[5216062,824892],[5970550,581687],[3540537,685142],[20715660,644765],[12519892,761178],[11990168,544692],[10070912,796927],[2778193,946403],[57953418,577733],[29813250,986048],[7432348,793255],[7801759,520672],[22139741,509679],[9978363,187880],[21592246,908704],[25269636,578732],[31617715,984068],[6178722,859064],[21040052,532656],[19916014,889662],[30441276,932956],[2701074,569671],[30925440,547675],[30616562,334798],[3630120,677482],[1802446,784350],[15985200,266955],[18567636,745369],[50528027,893653],[22711776,815955],[9309861,961224],[31503284,673468],[11758114,736624],[37015836,959685],[26915537,753418],[44955580,602637],[5690568,969903],[1765140,612589],[55711380,793015],[35385950,789450],[57388480,657067],[58046919,587835],[12474412,844468],[9350250,557772],[1893160,976964],[47407600,513773],[29855145,546096],[5454162,814021],[5985510,720373],[36706477,548662],[51356472,606157],[1518646,870286],[23592704,704550],[145695,843824],[41341568,601818],[58985556,626118],[59731383,759395],[49629600,806289],[1766475,521543],[1477732,7682],[2136150,649264],[59908244,827720],[15464520,528857],[36105059,38849],[6270015,935254],[47752299,752910],[39716820,578800],[31292424,596857],[23671152,758181],[7671956,914213],[85356539,884542],[20132564,964818],[4433920,735652],[17050706,945250],[7976140,723236],[20794995,826492],[5230456,865646],[56392856,530738],[78646324,651182],[60586131,533290],[2585120,549647],[75774272,518869],[24207538,504969],[9580236,277588],[5387620,620101],[9500512,551600],[5330588,594439],[34850816,534534],[37735618,428526],[2128956,798497],[16207360,856350],[27071931,618836],[73232966,537677],[2467328,523038],[37580,523507],[54847864,901871],[5515776,560752],[42120286,542404],[1237198,301140],[2841600,526268],[1305255,521665],[42422940,647469],[21020342,502291],[13864446,920685],[45314936,972624],[8444535,676610],[4195485,581906],[1270479,832865],[2938540,857764],[76584573,597560],[45441,602828],[9078486,659199],[39588252,509079],[20709566,698931],[30341511,580999],[6926040,707316],[47422715,641019],[2734916,969969],[1244524,943365],[28600446,764159],[45195311,811345],[6094080,585949],[673260,790187],[56200600,563969],[27026820,515280],[18664184,677445],[36818797,679360],[36725052,808199],[30002672,914373],[1712595,708487],[18736090,893810],[14994990,516287],[11437172,725206],[10472452,511518],[15536548,443332],[72447490,930300],[59471102,705456],[33433020,618148],[18246148,959652],[17907344,559822],[59653986,43424],[33069500,967959],[5703951,770189],[29383650,526309],[11142626,931527],[8510931,894507],[502414,599381],[19561050,582058],[41369889,887086],[39672811,515455],[2586432,531000],[23279536,993537],[81822354,983794],[11856040,181908],[11499246,677127],[2606947,797473],[46122912,614043],[33534774,584064],[13180725,733414],[5899440,64780],[15895607,694129],[18374355,753197],[4213110,664665],[28462083,791742],[7321626,776565],[3767904,806695],[2075216,686805],[13551104,737698],[49246785,563617],[22632552,563257],[49324198,667792],[20225130,605517],[939504,996360],[77042400,660291],[4405884,568924],[360258,787152],[32270154,586549],[19560286,539058],[33807895,657735],[24713964,867627],[67041788,858556],[4110243,927214],[6211163,752867],[27191580,862612],[30215700,743075],[12329646,634508],[22097472,669844],[42793384,691334],[48217700,501725],[12527280,546728],[56889456,667871],[69579216,590872],[27536352,198720],[27113968,531853],[52402324,615659],[6300174,745345],[3188770,692222],[2435940,623626],[71693578,579341],[3287544,961608],[35103145,655787],[23166837,723022],[1655220,897412],[2790958,643027],[51009098,894218],[22129408,735093],[17389640,713355],[1999375,585174],[25018420,649448],[68903136,875086],[10683545,581518],[25153170,742902],[93346,737600],[228021,898084],[6815802,834921],[27627980,740847],[27506592,830904],[4934760,986746],[9094245,670352],[25501056,891616],[13491150,969271],[870672,535840],[2328612,575723],[63054270,505813],[31162356,579991],[199410,525239],[13038390,974943],[37818900,536248],[19288710,547648],[53562022,802320],[18497736,738230],[12272680,791912],[38867073,697261],[23085048,870672],[2623000,897464],[31728320,704018],[27146886,775424],[71886080,829629],[12012858,564108],[11629354,955139],[14656680,50328],[35333120,649275],[32490636,503318],[45559778,942281],[16793152,581962],[43579122,691133],[17856188,964183],[1442112,979192],[68515848,818400],[12149328,592275],[18274482,540843],[48180335,956792],[15257306,509273],[19495539,780167],[14810298,520705],[55487042,776460],[21112522,867722],[17004100,611420],[12898731,647541],[27162135,548257],[4072530,972465],[4244828,635831],[23614808,13764],[18589389,509517],[52806228,515542],[34464990,785590],[31626675,918456],[33273450,834139],[74797344,621253],[2048136,537530],[6677222,876502],[1707750,563151],[8788392,512659],[10039620,619729],[26242139,852612],[43899440,546453],[24282996,725625],[48434007,751549],[33880830,550722],[61733727,618579],[49302512,579627],[80220840,955839],[34726894,842886],[26110546,552902],[1365684,795205],[3450876,534054],[6418146,648795],[4947748,743542],[32791972,888336],[49657712,862057],[46307312,702125],[17590640,563369],[13253400,821040],[83152343,781952],[27186560,325360],[85304795,607799],[31944260,568545],[5701528,723394],[3828864,638146],[32532788,972238],[67168625,994926],[8679169,910337],[7743008,694525],[57708459,943964],[40440852,648427],[18844632,621403],[38122984,622523],[2216256,828672],[24355260,843050],[66655336,619944],[7962978,807750],[14026122,712518],[10387610,534177],[94462872,753984],[19820622,563617],[42353103,87674],[12204948,586549],[196354,968495],[4607432,606312],[29687114,961520],[17566560,933439],[23828140,962744],[27816822,525533],[649380,504681],[8104941,652315],[12953148,657882],[73775840,988689],[27814752,690360],[35927844,512941],[4152312,902225],[6753438,813576],[69697380,693524],[21689080,594352],[1130787,606186],[5402025,764421],[23881668,860822],[1650545,634111],[31295400,651144],[4627596,552380],[29177733,775489],[4878414,797700],[35179722,582075],[8245718,694563],[11576525,777000],[45232184,742375],[48454186,506633],[506230,549450],[7400902,585207],[80556070,514185],[35999979,684143],[11093452,778904],[15190104,511008],[11975280,508850],[17125515,732485],[9418894,972098],[4240809,665192],[5145624,627978],[30542750,678291],[41592858,791803],[6064270,982444],[27137528,942687],[13220064,399156],[2097294,904754],[14755983,776619],[63434208,900046],[60830848,881892],[2776936,714189],[1252083,525670],[5528380,568845],[36345036,707334],[1684870,549281],[23759560,691079],[72947520,521453],[1314240,835049],[13011198,688705],[5547462,555053],[6093912,804770],[37702875,642296],[81248952,530768],[1865816,939129],[178068,698955],[69603060,740328],[18255636,710149],[381376,868154],[37185337,560706],[306356,588655],[7921560,701007],[10037508,659704],[2343033,571449],[10299240,968069],[32790149,614328],[6468792,899322],[2880110,739698],[86728290,809100],[4474960,753303],[16246575,522553],[5721192,744111],[48252147,713829],[35167335,727027],[67858494,629059],[7676539,842893],[30179440,927841],[1474018,536665],[47885797,508059],[72480466,872566],[10429317,993221],[48844088,665073],[3303542,790617],[5265542,565318],[38575103,720849],[1117339,635712],[23390080,805164],[78069546,670784],[94278,767620],[6278949,919868],[40210780,752180],[36446469,560504],[43023585,645190],[33661014,692010],[17640535,718820],[45273660,689775],[9275577,950235],[567932,940776],[1396116,674970],[14105104,800044],[10203325,700245],[21954452,570176],[48612156,573597],[9745148,942745],[3659045,546768],[64717719,559416],[19894826,658215],[32520474,908747],[11990823,593134],[73245384,603860],[54627755,711541],[12594996,651652],[379308,738640],[629506,836036],[20592540,970490],[47800130,30303],[3280581,335820],[23653224,677103],[13538975,916443],[15330540,858058],[52996535,631400],[7408380,851980],[18524328,516613],[8342996,801211],[52992500,968567],[32744936,973123],[6542060,520853],[22321152,768265],[81454269,816439],[32815590,725800],[4956160,680824],[39300192,763466],[4131400,979623],[12044850,504070],[41030022,623086],[70838340,608552],[6770400,950281],[29295238,552631],[38820,627598],[16610976,718544],[16447995,799153],[709222,813026],[58170384,650745],[18682500,861681],[33656280,552851],[20800,554652],[54585118,959542],[27796608,703961],[18352512,537463],[9496795,746006],[25715845,557048],[31243565,822785],[24334242,942489],[12237520,826948],[11868642,610239],[12655770,873932],[14940831,537242],[15453317,723233],[36295210,821031],[310496,765341],[33124590,598394],[4291936,634065],[4571008,576940],[17686494,963313],[24487675,853514],[53840112,832176],[18503976,543697],[9185430,980338],[15080768,888076],[19890387,500685],[6492584,751734],[42781312,973965],[2160196,628023],[1253370,690887],[1759060,879675],[33245496,690899],[4701614,940715],[83813621,968632],[12389080,652675],[23967216,665884],[5410039,942084],[31984004,850256],[55162224,953819],[72106740,896743],[44499427,878602],[51876069,755377],[12621123,800429],[23848370,937807],[17216905,528965],[6283043,768548],[11581592,970397],[38542336,534681],[13087960,554094],[25260450,703222],[15736138,693399],[12799224,581810],[34030695,762083],[20174952,780999],[11396700,974383],[21194047,626173],[16037798,260022],[5309816,669542],[13986266,548003],[12896260,542092],[37055172,705005],[1292595,595200],[9497248,761254],[34135200,678873],[13202820,722214],[20174109,533157],[31652062,500334],[24840060,698533],[3800384,592784],[56448996,854483],[10914464,916480],[59507964,847594],[16274524,680344],[55560514,860854],[8794304,846004],[10962035,756375],[17274656,538745],[39822120,615887],[5999850,723565],[1852176,347384],[45248806,510862],[6462958,683625],[25941060,663263],[1971318,562842],[85849921,943740],[2243976,743980],[20670753,644598],[14684320,811015],[31446960,668175],[16263990,682048],[23077600,647736],[901468,54510],[1705536,734083],[15418182,696444],[9258403,741084],[3769600,532240],[31674150,526163],[9895752,628196],[87058400,834908],[14900242,507851],[36907719,776826],[27996540,546687],[2271282,548243],[65834124,606811],[30639840,996790],[2682680,804056],[57757880,820727],[4487720,728805],[26626330,817421],[25948520,719194],[19814316,529032],[24275592,602407],[20280312,595536],[48362978,639405],[33170534,645253],[55869234,647981],[6643728,613837],[3627674,560469],[18327037,647770],[18982425,962613],[3189970,801642],[12235545,718847],[74628864,705318],[9834960,379240],[794964,735690],[53633020,595612],[4362479,976779],[34294932,875070],[31868094,778085],[17283960,873490],[85015458,671448],[18318852,605561],[31580640,657635],[12594400,554599],[19835350,991736],[270930,631306],[75709218,960323],[16523775,632363],[20777526,955172],[87201730,500614],[22008545,983022],[40829096,861311],[11780439,804580],[4867182,510142],[200046,538475],[3505356,570826],[11214880,655492],[20555262,965459],[15613984,635605],[32874626,822483],[8237775,880698],[3408700,709170],[14757425,812782],[8556256,599459],[15212900,540680],[97511269,925035],[9057550,530431],[30820698,501669],[7702240,634119],[34140800,943258],[7309485,588627],[17543591,521080],[62524,636494],[14983552,552387],[14708556,707065],[47396750,532614],[7669695,831329],[8819004,560256],[14011326,821145],[16252986,926891],[21073754,693918],[12349298,29232],[12701565,848804],[70357405,593072],[17864652,585610],[45050412,351960],[326610,615254],[21981752,818057],[711852,595186],[2322762,90000],[23182896,583366],[20623625,652739],[11182724,759230],[9472000,596877],[66925584,607271],[84852952,712770],[10002942,658605],[64085153,920695],[822081,856772],[5655535,744383],[1516223,698246],[2032105,912832],[860160,590296],[4374600,910695],[14407936,865282],[7017192,599044],[11702544,647851],[29648220,757873],[4730616,982196],[2921142,935812],[1189818,859489],[4861227,507250],[11601928,596189],[68657342,535500],[4850515,602616],[28437255,679458],[13131068,960858],[388871,840904],[9627033,643570],[8823375,975063],[576096,802776],[34161534,901151],[54607960,700432],[936096,633832],[8294832,509105],[32809200,563072],[7145899,531454],[1298592,823622],[56805945,570391],[30495,71192],[4967946,772440],[895104,741252],[57616104,826030],[3497104,531610],[4756656,830295],[10734042,562452],[3107940,549708],[46948564,527501],[15267780,567138],[46199088,530476],[59637642,966937],[14681680,948285],[8086776,983623],[47528478,712856],[8143744,648330],[4198220,626368],[29055510,736440],[16216368,898767],[63898380,734039],[26451600,558191],[8206308,725246],[27944114,896327],[21635042,925213],[28210419,319424],[38420882,811150],[6713364,502223],[8251092,948675],[30847252,989813],[732940,617531],[61239728,600255],[3922976,525765],[35796288,586953],[80428425,751390],[33125750,662199],[15029118,579253],[30487296,861064],[31861920,160752],[11050182,522944],[41239512,795110],[11223555,532041],[12816496,739660],[71570840,560083],[37356930,910245],[15604320,526197],[16130480,516250],[228656,321776],[65242200,633972],[43704125,598697],[55078302,428309],[25346871,807895],[669693,960531],[28341000,673194],[13160142,996327],[8205868,848388],[23179064,609305],[13689126,615835],[13686918,502250],[4131666,588981],[24059301,641565],[5222516,591781],[4116768,870199],[59260796,501639],[53050762,558510],[34587550,992531],[13119603,741256],[15323256,873237],[11376478,270270],[13626231,528658],[68715156,737377],[27715922,646616],[9609056,834038],[16628345,545845],[1905750,911216],[25813425,760237],[9010503,752197],[31435520,567113],[45516940,975374],[17702186,11270],[63098518,760067],[35381400,505800],[3766955,892776],[5032750,596068],[33725940,750296],[20265630,857463],[47120040,943686],[8901162,566227],[32231472,662496],[3196522,538436],[24696251,574980],[63622328,737232],[13815322,506761],[50522976,822090],[19182283,276675],[26348913,748034],[5900864,706502],[27031617,943019],[8995086,612126],[14420282,716362],[27762952,543743],[57992193,640659],[10355760,786258],[45812375,535354],[780763,519091],[3728816,725647],[11567066,544722],[44281348,500966],[1597024,981853],[18931878,503672],[9744594,847630],[19137500,670160],[14897220,791463],[32298354,966590],[4521625,541777],[8410058,653493],[27757092,603286],[17402028,684387],[71634736,698888],[9045052,608826],[5129289,991042],[7784118,906989],[92446689,876532],[8426985,561554],[15595341,946738],[59711835,675530],[497768,603405],[54996480,892426],[6300954,706140],[2148061,571524],[5813720,756679],[20800150,718180],[153716,767570],[29406000,637115],[1624221,561702],[4668743,322115],[14060924,676985],[15606544,640694],[41093767,921989],[3064446,856818],[30496563,662464],[13230166,586760],[7898946,672330],[2109411,700225],[76529460,694652],[29124528,769841],[47274586,636324],[11700292,786600],[3004992,698700],[35457354,582946],[2078648,677490],[32774184,666919],[47840812,653945],[6657510,733596],[30163757,924602],[12396100,845744],[14393186,753867],[49281466,684036],[5287401,521453],[2456775,543089],[5000472,507322],[18928761,895737],[27742656,546412],[11351395,502441],[49358280,581275],[36815384,893930],[13401522,942925],[16824468,504916],[19169450,613893],[40702012,516803],[10047626,881923],[31889010,764626],[16203408,626832],[346455,819694],[48846756,614215],[21003268,965219],[18831223,512724],[18138510,845490],[49747470,957412],[7076784,20064],[41399568,426398],[2069480,656085],[10497920,978755],[19840780,579414],[24953822,765400],[3346760,531892],[22448500,575915],[11974410,765105],[28652701,638194],[33498872,878143],[41958736,544033],[3433144,979154],[1311975,638542],[10119910,580686],[65799360,539760],[17814384,582218],[24441728,725494],[20344392,736939],[24988040,555488],[49572590,612434],[15036280,944690],[51076032,614079],[15660216,962477],[17263953,949689],[28397612,771858],[5437632,557142],[72509796,678466],[68854968,545878],[9457140,718960],[40172758,706753],[15758600,746194],[20830644,652333],[7442060,568216],[41869398,741779],[11942013,566699],[1831170,677344],[25974622,931296],[79484072,608625],[18237132,969951],[44925913,618982],[2854365,796588],[81380453,812759],[12113877,912145],[380378,816199],[18843708,553829],[7430610,849084],[7239672,579340],[38961250,824886],[5362620,714886],[4934293,621527],[10832528,595517],[21856170,610685],[24260236,955456],[53378068,536946],[11160632,796463],[2709516,764293],[10750575,993870],[22110487,401422],[11193273,537140],[28306806,502087],[7572474,870231],[15431472,932228],[40679962,667432],[2765040,576980],[48814494,31296],[16641903,534627],[11778024,715159],[22718715,992469],[19645680,507382],[28966520,941598],[29388177,741879],[31592142,826864],[42553920,874039],[81280108,848616],[21557520,599440],[51676975,603075],[23343372,824671],[1122888,559248],[193128,949403],[74420320,715121],[37732940,922785],[1724491,938772],[19350472,602665],[712530,685152],[2939664,688323],[48773152,775656],[17972808,808428],[825588,507275],[36673692,786523],[214809,675462],[25729194,771960],[2799460,672575],[110360,583115],[34248445,774493],[22853585,714224],[65484370,767928],[35777076,737103],[500193,713878],[70096270,509022],[31786032,801120],[1484726,983711],[27639664,796789],[25183396,763529]]

# q = [[5106368,519652],[40800528,729463],[34276915,724957],[14880034,641015],[34368080,927877],[55989836,647349],[40115680,993025],[683046,949091],[191318,668608],[20136942,230856],[18004232,771207],[21018775,653696],[4211196,570968],[92231028,646015],[20934216,583167],[41833660,632449],[3226422,601920],[14572210,910215],[4684519,870734],[9784368,671033],[17042432,536774],[11178624,916081],[1199287,695945],[30289518,905966],[2864687,934896],[83368376,884428],[679040,713464],[27254528,752280],[21117558,802010],[15927480,844313],[24057822,750263],[3545358,869657],[11251177,798576],[2087038,963316],[28325380,581940],[16355232,804344],[22866158,26855],[32737536,574382],[20556918,914631],[10517361,825995],[76260,738323],[16172530,423360],[20160475,605061],[24391410,967765],[34938,869130],[26428701,638391],[21053832,802894],[6702234,737484],[48448167,906348],[4460340,737143],[23623328,753802],[72925682,685608],[25804800,709669],[1964556,608802],[24895850,812401],[26942007,760110],[47186106,954720],[25768688,825708],[36199072,553302],[41311802,618563],[15260104,544345],[83957328,661509],[2542050,869802],[56097720,848145],[43397106,604575],[69642752,834290],[40417764,812782],[2704482,612871],[42983388,703109],[275373,682103],[24722253,593790],[2823273,832947],[41578692,915124],[3506048,934650],[19419817,717875],[621840,642735],[1427355,955155],[36517088,915985],[1948438,853531],[47947005,591395],[28750683,833170],[17955665,809065],[11103802,704699],[73969123,594128],[54714300,673404],[11059713,750326],[22060030,923684],[5667586,978200],[28739382,886180],[27776152,774562],[24585804,845705],[38414824,95235],[4370520,508026],[25049587,531770],[2184218,932901],[5491890,553784],[34435076,942840],[29903770,606480],[3489020,540520],[65546100,310411],[11041500,550348],[9789450,650945],[17814429,963724],[47075015,659836],[22677177,686968],[2078592,502928],[20407905,904622],[32385600,905655],[23768,817315],[39779867,666148],[7207117,640768],[2394100,510347],[7607600,769063],[62961157,846407],[42743477,574141],[50290520,656782],[38497146,938719],[2910075,957251],[27473161,991945],[5769864,507532],[5068827,999782],[1060024,676863],[19235840,862438],[4762270,728727],[25706760,577566],[46160100,724791],[23788262,406269],[6090000,763136],[14782728,607456],[42161340,921726],[7472905,980712],[9927152,649395],[36934200,782132],[287358,572269],[38205200,548223],[3011295,527201],[2272550,822959],[38907540,692342],[17154226,686536],[26789057,710289],[4128,626073],[37033210,863242],[5403376,619636],[1583004,705012],[24952086,825858],[4424184,565900],[25038000,782992],[50528966,517314],[39538422,673232],[61094880,500620],[1188621,813867],[74548270,581293],[71370665,921251],[1810542,746144],[555552,946624],[53091930,512842],[52044993,762242],[76464873,661525],[632104,536338],[1781696,535262],[39896838,671346],[6654455,925224],[21731955,663321],[64713870,832005],[4384630,862477],[12635844,733922],[30817738,878440],[38564498,835077],[25238549,574882],[8251446,747318],[35437375,900781],[22329892,869553],[59136220,527260],[51534488,972910],[20590625,502506],[18658920,646440],[50060970,524346],[25069458,211824],[6655320,927473],[2481116,694942],[10476126,558818],[9604172,829210],[38776992,727626],[10047849,898569],[32990023,521160],[3684662,585892],[11749326,756114],[15590228,609159],[281792,836113],[15846175,810552],[17415393,717117],[16744092,887605],[264600,817680],[5388614,746660],[21526274,507500],[11297286,500914],[43297112,576593],[1635900,837875],[43794816,530806],[6070899,792072],[16935346,622210],[12297987,805704],[767550,927844],[977898,743207],[12346380,535536],[12609970,817168],[18095395,537073],[24952056,996859],[36591198,730396],[11569911,760097],[4944105,605709],[4357951,837334],[10744870,528177],[2174304,827549],[33325695,758906],[49531578,328782],[31509075,500788],[31131374,654515],[24597958,505936],[4189923,594319],[28377828,518943],[4423382,646282],[1262250,785701],[23486208,510484],[63433858,769730],[75192106,978307],[20576017,866183],[78436186,910933],[76264740,879545],[17919000,750802],[37571148,669634],[43747299,826503],[6888976,997360],[16913312,515889],[11505114,631400],[1996722,827040],[1268757,545097],[29221479,681898],[15582106,546365],[42139680,569441],[5195120,744659],[79553435,738834],[10032813,680485],[18191172,584100],[3506048,936031],[35007994,926900],[2478300,547804],[65206050,517472],[13754360,969965],[31927189,816511],[11546484,710081],[17179470,664583],[2074260,895446],[16263288,585862],[54463878,705390],[6025698,673868],[97889027,818720],[24386274,771959],[79200,622191],[8606750,661802],[13935818,676420],[31743666,705893],[9077631,720521],[6638914,557363],[79452900,596727],[30279627,149480],[46578600,633617],[22081000,725414],[11295990,789207],[31010280,724070],[32970,632520],[10898272,765076],[16595540,526466],[2797395,602294],[10033604,813400],[60235517,558166],[29991372,735693],[39937983,500279],[3239299,812996],[22443668,536393],[29610776,699644],[2308743,715034],[5248,656401],[51830454,509392],[6428805,587043],[31876042,353772],[184277,656730],[20710830,553295],[36559600,739046],[91776,926370],[2928162,580086],[50630736,201040],[10585260,620654],[20195507,731315],[30872049,563560],[88047792,974236],[44104320,596557],[29721005,546921],[7458186,998280],[23110347,607579],[24031130,796715],[56036796,621320],[30927910,713255],[5888740,581604],[1019872,871156],[5513763,773294],[4628520,593082],[30700449,711354],[1016025,947266],[2387946,606478],[21851436,731960],[9614836,939435],[11602188,603171],[20937222,951047],[48991842,590121],[21024432,853464],[7496448,828743],[23491106,661641],[39274729,924852],[2217880,774364],[44784378,744807],[33466818,513037],[12418160,914742],[4359040,879978],[4742010,292026],[9090688,877087],[37013320,690070],[38825150,863853],[12160001,792149],[38171520,667647],[66045463,985583],[25683097,652925],[9626240,536190],[26843544,679736],[79230492,985044],[29131674,572840],[12126972,440748],[48268682,819024],[11798416,971784],[31104276,656149],[98147688,583428],[1801764,781471],[13017056,500980],[34374970,760266],[31060679,445876],[40285960,692067],[77704,557901],[24172638,856538],[12723293,584070],[33787250,609355],[2690408,653812],[2651190,937045],[20890776,933187],[32449090,980647],[20734896,501528],[14916630,529932],[3871791,559424],[12191500,560637],[63066492,976601],[74711736,514414],[29303339,518896],[58908799,525014],[18107600,995482],[18931968,815790],[2927250,669160],[255943,982170],[33663188,921537],[19973504,581310],[16768936,669210],[40857600,989310],[17150192,590467],[9635946,695506],[8842600,662009],[24445343,773147],[34682980,931270],[39776844,947233],[10605434,564642],[85567902,567492],[14555156,837965],[36222170,623238],[43197944,689924],[280784,942646],[15493520,799683],[79148000,702698],[20674590,661727],[33459058,562624],[12117724,669519],[2785920,702056],[24673782,820363],[29642690,528700],[15714600,721928],[4359560,722856],[27203770,709507],[9256040,552258],[26573176,965889],[988038,691880],[9038860,860626],[35289524,695984],[1384086,769875],[2003774,567823],[83680680,810195],[25264803,665543],[28581733,535543],[5343130,761751],[11120794,850020],[7348555,891351],[3340495,844198],[15297204,567162],[14240440,540137],[7954105,585945],[70875805,787421],[15390408,565139],[8753470,529945],[6632845,508282],[21523722,995261],[16344916,685414],[65360220,660048],[31486879,769296],[18796416,581446],[66195271,562975],[5328692,654777],[60174473,845494],[10604166,941338],[50857984,869417],[24828896,635177],[29782558,935130],[4945824,546296],[474881,702008],[47534452,596018],[30448575,958698],[2910388,752405],[80347331,566797],[50641514,239094],[30084045,585277],[2759485,581440],[45288918,702794],[11534489,741730],[15298920,957361],[1220940,574078],[1411794,735590],[67867250,579018],[93037620,902391],[26522625,870073],[5743854,672489],[59394618,536550],[9091480,820534],[1222893,560918],[63024488,510241],[17292052,600882],[3179475,971578],[6823710,504828],[39221280,560352],[1386320,923086],[20936556,900330],[21759660,899024],[30044633,665210],[29432523,562251],[34027200,726042],[36347776,988598],[36524891,688415],[47344215,520871],[14934720,508565],[9125020,465102],[25017775,949497],[17016012,611912],[6587084,535882],[9552636,787510],[53999931,533547],[2571128,835119],[21260645,517188],[27028302,514645],[83915429,994452],[1768221,655434],[26250714,589174],[12529749,624462],[19303977,929099],[10296105,822830],[10125605,803390],[11480625,504398],[28493906,963224],[4710225,514936],[2697541,527527],[6564480,589960],[61414136,975096],[32523513,849416],[163056,696146],[1002919,732648],[6644870,585067],[10134000,658244],[33765985,605630],[14995134,563575],[10031584,606993],[4774209,869115],[14607600,528189],[19960754,563951],[12119394,925683],[7557410,687202],[38345058,607937],[63956265,513135],[21432695,534899],[23258804,682649],[57610806,735182],[12005928,502515],[714204,527959],[54009600,670040],[9891060,811162],[13864095,637181],[86832040,863911],[4003560,681453],[45992365,547069],[23227092,525708],[5351840,911985],[28718697,634385],[7572086,964550],[8749093,829435],[29888432,957859],[2855660,712333],[6873025,620940],[26542230,841016],[20945897,686088],[10348800,735407],[23345840,565628],[491462,790632],[3232736,629123],[15898161,819525],[14713365,582938],[40761378,608647],[27803640,893920],[3386382,792158],[58971297,837352],[24695874,923344],[60209730,965906],[7348926,518183],[1104246,590547],[15837070,559275],[1528534,717761],[28515456,521971],[14080030,664373],[2710809,686528],[33691941,726975],[1853525,503415],[7609136,503924],[38287563,826072],[30540075,527182],[3220276,561629],[53177285,619394],[34774635,515642],[28541858,677460],[89013472,721320],[21153876,567162],[1392365,545887],[4155350,699239],[5857046,700920],[3792020,838442],[42562288,663200],[41632332,928024],[29718192,785941],[6011202,583123],[167535,580387],[58849512,666108],[37124465,845106],[41895432,737543],[69842499,934032],[13225535,648444],[4592364,641858],[3827403,824415],[568512,753610],[6324209,933570],[18144204,565582],[59221206,750141],[3728934,543485],[54941544,970264],[11305403,451200],[17784917,719381],[42842184,670916],[11528652,647918],[80453086,536578],[12719196,641940],[5255670,889630],[18662218,675688],[9045684,260337],[37664640,508139],[5031516,588938],[9143912,801643],[24239440,608718],[56935856,852758],[49302575,557998],[4006242,670541],[3318245,949452],[20654244,804560],[7353668,526689],[62182882,919886],[4650744,601089],[29246480,575522],[2555238,508866],[11645989,865867],[13719420,900460],[45384000,783525],[45637095,843574],[28710,833546],[37110762,675633],[554092,650999],[9949354,720145],[6801886,787221],[10433870,652002],[14267077,718706],[2450473,556239],[2081115,629096],[13670832,511805],[77715459,659438],[41161308,716875],[47476614,874243],[40511226,805365],[32038220,605627],[52172694,829001],[10360592,796235],[49439445,593971],[3003000,657888],[14106702,926152],[9105800,776074],[49412142,559758],[13931424,517385],[4619592,503625],[2906180,773381],[4598588,513598],[11765264,771524],[21939408,546161],[1733550,755399],[14191940,534087],[1673718,791742],[78334830,843698],[16914192,585399],[47164788,981456],[54666120,844468],[13377306,530176],[6376488,713632],[853554,751952],[12307905,941382],[1606275,663853],[8767512,685928],[10108602,761799],[68841675,703665],[15525675,765804],[43957956,549252],[67445125,663146],[5540320,522050],[32089689,789106],[2474940,660978],[4774029,637000],[1476792,609568],[52569548,277886],[62461388,608243],[39820110,631877],[32987094,637071],[29955893,708064],[85636515,759895],[1962720,817435],[2159784,736170],[6472006,546273],[25986136,603163],[50039451,875497],[2408000,661971],[31618334,616450],[31536201,932376],[7139284,536554],[29145096,956229],[32732829,802280],[13740156,667717],[33741328,718497],[1091545,666615],[91650468,696027],[79906680,276276],[61257168,897220],[110422,516128],[683050,994032],[4714875,559870],[5677166,880919],[5211708,501726],[36186865,585706],[3060442,523945],[29830380,646885],[3646188,111706],[1164384,813298],[33368010,742458],[687987,818358],[27266304,571926],[77667412,853471],[49917978,678487],[1161635,678848],[4778928,888968],[47080596,628108],[13970035,857475],[65526436,926973],[70008664,901860],[11829104,979986],[21224072,841072],[13039272,621196],[11092086,916641],[46376289,577535],[19840088,718965],[65300128,651316],[26096480,636091],[25032004,942795],[18150864,747738],[849600,644280],[32160302,759532],[2095952,561627],[27142245,542821],[1087020,648181],[11194572,880866],[3075252,609239],[18511500,764253],[15400438,785798],[3060850,864381],[15120900,991974],[63735064,512427],[5594852,863100],[62554050,658047],[31122831,733687],[28315532,656336],[9255720,545575],[3412406,576994],[17004389,587444],[65679208,729496],[35910176,787907],[8401785,739866],[1689772,556305],[7980260,633015],[6883696,524560],[14189574,737954],[83180412,722513],[6525960,805068],[53411274,900572],[127428,804438],[62800352,501193],[3978140,566722],[4582359,946763],[3724280,758103],[31436174,781485],[14807312,909830],[85661106,521825],[25784495,749006],[4105647,683215],[5001120,660883],[32452342,933613],[77752108,787242],[59045194,743753],[3085992,580937],[22482240,727910],[2907284,533218],[4720127,968610],[9117160,761978],[568875,717108],[36687987,755521],[18392799,668745],[4829890,801160],[7224550,588673],[3697643,579000],[37177710,548107],[25172453,533277],[8176024,802509],[16132363,780826],[17395545,792633],[63449760,942197],[24611840,558007],[20923836,573126],[24147939,519412],[34040040,597192],[4090944,647971],[13317024,975612],[14657406,633848],[1800090,675520],[31657430,783100],[35463930,371856],[901824,644128],[8878842,722902],[24237820,988162],[47655508,555521],[8281836,622369],[42340905,538637],[6382956,685448],[5364450,813613],[11181344,670350],[12714534,879455],[1171968,892897],[7370865,817371],[545916,587437],[11692209,551072],[51399173,964863],[4133478,664572],[13037064,857546],[60053227,575556],[4606312,789339],[13872657,603820],[16757010,548451],[20634561,598589],[32082183,784901],[55847190,45040],[28239696,527800],[12951495,950844],[7099038,800276],[12578055,622648],[597870,533501],[16447136,522365],[44511460,591664],[1619046,779862],[80285907,764621],[21829056,139749],[39766580,613967],[8467239,515602],[7516125,596782],[15755340,979980],[15616467,682691],[49614994,788120],[4072299,798185],[1149450,813450],[18070191,855413],[8134516,791956],[18249084,548099],[48415425,849408],[30509030,666826],[25125312,877372],[42661872,682268],[50543636,711621],[63029990,545937],[27218598,520291],[3073008,556730],[13220712,720360],[44649994,846532],[17646750,807628],[1470096,801062],[13490307,681486],[11376688,789375],[16718744,638949],[18724500,831080],[10620531,825712],[34667840,669212],[1376728,648275],[11909328,564888],[47851712,846930],[5117360,793925],[9123192,642773],[2966425,673415],[88330861,602234],[59133412,906870],[33756426,569790],[45605106,662806],[18249264,996256],[13921392,782110],[7271160,524875],[7892472,539787],[28880698,635676],[61579440,860618],[56643040,693818],[50336298,475664],[322453,613243],[12793928,513922],[34978212,965971],[14600779,948608],[3670300,859261],[57675780,565175],[33904308,893539],[73619018,836496],[1795800,509746],[6338478,912492],[33390756,990832],[15680508,869376],[8251320,731172],[67319914,596222],[80386370,560595],[62843869,572064],[57626465,643170],[6296325,516539],[2034120,754570],[37427754,989474],[19552264,862011],[20936905,598714],[72604480,565730],[74546502,740300],[13132260,673682],[18350409,924302],[17568444,621935],[13230016,697215],[4214988,589803],[50467152,766868],[5242720,539423],[67151112,584640],[65891520,626982],[29676780,716850],[34919118,568986],[2722320,639129],[28333767,759810],[3108048,836025],[12157968,714110],[25531797,924752],[38323992,594028],[4568816,814338],[5681736,596045],[19486653,668200],[33777611,710856],[7703531,588841],[20116902,630125],[3039885,420300],[23714,337092],[31708704,663602],[19071405,533791],[1994988,799420],[28897568,609653],[6047454,756212],[59693205,899288],[427632,662194],[50314264,503132],[10608598,896481],[49783230,738307],[17450784,643186],[13391840,502019],[6273827,817141],[80244120,875875],[12949933,683497],[37993746,604754],[16803486,876328],[15960384,817401],[40817152,681067],[30035097,915442],[32937587,961891],[23094342,672130],[44015047,590103],[5702046,94385],[7224158,652076],[38303120,848165],[26620240,780877],[41189027,739683],[9580080,794403],[256668,595556],[3220404,875720],[4992834,563972],[23493208,551056],[31853248,839966],[11599335,996688],[12402390,629311],[69198705,642330],[4073998,685568],[85972680,551505],[883461,979688],[20036636,619774],[38445600,704505],[14633918,884032],[625856,550293],[16318152,928337],[35989034,610483],[4023918,708442],[5652110,558330],[4212960,863814],[64849248,544518],[9565540,683156],[7302701,770544],[49288218,633707],[17664749,155558],[33546744,982410],[617232,553876],[20773220,747076],[3448170,932141],[2002044,997524],[30969705,706834],[30826899,799542],[58271628,631006],[56803872,957909],[66186270,640214],[11063997,707306],[36865180,634698],[6770694,614327],[31723360,654306],[5102790,520803],[16697496,820890],[29314955,579325],[6684720,641863],[40406080,538755],[39379655,576066],[50221830,538016],[331776,610302],[1761000,797423],[16387800,712631],[8252448,619295],[54139288,657630],[6397281,574238],[1354450,862760],[70122400,559374],[20795295,915230],[25276966,970463],[13380133,963388],[50553506,597005],[38320310,820940],[38392704,595597],[2898144,576517],[12880347,834171],[3032704,917450],[7495290,926156],[7862188,751911],[10845250,776361],[4491368,996111]]

# q = [[2, 82], [57, 22], [16, 66], [46, 15], [5, 11], [9, 83], [1, 32], [87, 91], [64, 61], [87, 53]]
ans = solution(q)
print(ans)
