
import numpy as np
import random

start = 11

transition = np.array([[ 0.09285317,  0.00223766,  0.06241161,  0.02256873,  0.0006458 ,  0.01843322,  0.0090679 ,  0.02591128,  0.05087769,  0.0138873 ,  0.09632514,  0.07752052,  0.12392577,  0.18275999,  0.00727814,  0.00044787,  0.03742012,  0.01970911,  0.02072066,  0.04258322,  0.00228894,  0.00255877,  0.01396281,  0.01044132,  0.02752625,  0.00737219,  0.0006239 ,  0.02306293,  0.0023363 ,  0.00224167],
                       [ 0.08861901,  0.00293229,  0.06237102,  0.02216681,  0.00094623,  0.01873985,  0.0090679 ,  0.02597765,  0.04480148,  0.01351014,  0.09631053,  0.08182738,  0.12265207,  0.19021007,  0.00759073,  0.00119695,  0.03504917,  0.01949183,  0.02220375,  0.04188481,  0.00225855,  0.00254611,  0.01454535,  0.01049945,  0.02737826,  0.00730973,  0.00065974,  0.02222591,  0.00268111,  0.00234608],
                       [ 0.09338907,  0.00237404,  0.0619504 ,  0.02410458,  0.00074701,  0.01846096,  0.0090679 ,  0.02642046,  0.04785953,  0.01361932,  0.09390505,  0.07981534,  0.12313903,  0.18373384,  0.00740528,  0.00065927,  0.03720375,  0.02064817,  0.02033187,  0.04297396,  0.00224173,  0.00253013,  0.01376135,  0.01033281,  0.02742218,  0.0073208 ,  0.00063445,  0.02318375,  0.00246001,  0.00230395],
                       [ 0.09185249,  0.00264118,  0.06237428,  0.02263804,  0.00093711,  0.01860036,  0.0090679 ,  0.02518234,  0.04523213,  0.0136649 ,  0.09573779,  0.08059081,  0.12350673,  0.1874277 ,  0.0071734 ,  0.00092945,  0.03528328,  0.01895627,  0.02164833,  0.04228783,  0.00229518,  0.00253618,  0.01444508,  0.0104295 ,  0.02817562,  0.00738555,  0.0006472 ,  0.02338059,  0.00262404,  0.00234872],
                       [ 0.09007078,  0.00274115,  0.062262  ,  0.02237839,  0.00085938,  0.01851682,  0.0090679 ,  0.02375223,  0.04536858,  0.01365692,  0.09589107,  0.08057707,  0.12357215,  0.18862656,  0.00743059,  0.00120379,  0.03488976,  0.01962649,  0.02204891,  0.04286953,  0.00231556,  0.00261168,  0.01485877,  0.01054237,  0.02769889,  0.00726231,  0.00067519,  0.02353274,  0.0026877 ,  0.00240472],
                       [ 0.09407328,  0.00252314,  0.06187271,  0.02186972,  0.00083714,  0.01886191,  0.0090679 ,  0.02749525,  0.044325  ,  0.0137055 ,  0.09544024,  0.07999366,  0.12311753,  0.18616643,  0.00731062,  0.00126533,  0.03442526,  0.01897227,  0.02164971,  0.04283029,  0.00229068,  0.00253501,  0.01468497,  0.01044856,  0.02854393,  0.00727429,  0.0006414 ,  0.02269518,  0.00270033,  0.00238278],
                       [ 0.0913753 ,  0.0027881 ,  0.06216451,  0.02140157,  0.00097423,  0.01851888,  0.0090679 ,  0.02552787,  0.04558543,  0.01329335,  0.09659079,  0.08165601,  0.12386901,  0.18617924,  0.00728697,  0.00107523,  0.03495913,  0.01872271,  0.02251752,  0.04276321,  0.00230847,  0.00250869,  0.01483725,  0.01036017,  0.02779868,  0.00742925,  0.00067636,  0.02290106,  0.00254294,  0.00232015],
                       [ 0.08977617,  0.0026824 ,  0.06216439,  0.02548206,  0.00075624,  0.01891177,  0.0090679 ,  0.02660932,  0.04436229,  0.0133805 ,  0.09729091,  0.0786756 ,  0.12283092,  0.18649701,  0.00743091,  0.00094918,  0.03511857,  0.01931154,  0.02256922,  0.04284651,  0.00230568,  0.00254349,  0.01481973,  0.01024517,  0.02749732,  0.00747902,  0.00067851,  0.02285373,  0.00253687,  0.00232706],
                       [ 0.09624901,  0.00254138,  0.06207019,  0.02193481,  0.00071568,  0.01843177,  0.0090679 ,  0.0249899 ,  0.04619224,  0.01398545,  0.09628258,  0.07928424,  0.12333489,  0.1846409 ,  0.00717738,  0.00094537,  0.03655297,  0.01898214,  0.0214979 ,  0.0424633 ,  0.00226127,  0.00251086,  0.01466096,  0.0104105 ,  0.02771139,  0.0073213 ,  0.00067111,  0.02226243,  0.00251468,  0.00233549],
                       [ 0.09171965,  0.00269725,  0.06208108,  0.02246003,  0.00089931,  0.01861508,  0.0090679 ,  0.02527737,  0.04489643,  0.01363175,  0.09590663,  0.08055573,  0.12374844,  0.18726771,  0.00732911,  0.00132764,  0.03465975,  0.01913594,  0.02223076,  0.0427405 ,  0.00225977,  0.00253625,  0.01535768,  0.01059707,  0.0275393 ,  0.00736334,  0.00064787,  0.02240717,  0.00273022,  0.00231324],
                       [ 0.09264199,  0.00251755,  0.06216917,  0.02410274,  0.00061832,  0.01850569,  0.0090679 ,  0.02674545,  0.04757491,  0.01342211,  0.09454803,  0.07826803,  0.12360648,  0.1852859 ,  0.00738884,  0.00047012,  0.03661898,  0.0206132 ,  0.02043267,  0.04293598,  0.00231216,  0.00250845,  0.01359266,  0.01046895,  0.027897  ,  0.00738338,  0.00058638,  0.02299963,  0.00234087,  0.00237647],
                       [ 0.12202604,  0.00036845,  0.0585566 ,  0.03090111,  0.        ,  0.02099084,  0.00969305,  0.035444  ,  0.06162386,  0.0164624 ,  0.0801562 ,  0.0560992 ,  0.11842066,  0.16589068,  0.00404475,  0.        ,  0.04484186,  0.02617838,  0.00896799,  0.04677374,  0.00117687,  0.0037917 ,  0.00674829,  0.00818727,  0.032534  ,  0.00898763,  0.        ,  0.02979284,  0.0003703 ,  0.00097132],
                       [ 0.09324785,  0.00226543,  0.06214682,  0.02240643,  0.00044212,  0.018456  ,  0.0090679 ,  0.02647061,  0.04664737,  0.01386319,  0.09591179,  0.0817095 ,  0.12382913,  0.18360067,  0.00718792,  0.00033614,  0.03475058,  0.02039965,  0.02008643,  0.04254739,  0.00224285,  0.00256583,  0.01435681,  0.01058704,  0.02917994,  0.00726878,  0.0005875 ,  0.02351736,  0.00205501,  0.00226595],
                       [ 0.09382602,  0.00172448,  0.06225647,  0.02451012,  0.00027328,  0.01878906,  0.0090679 ,  0.0271938 ,  0.04756822,  0.01396094,  0.09185504,  0.07722021,  0.12335757,  0.18882084,  0.00710338,  0.00002667,  0.03678655,  0.02130457,  0.0180225 ,  0.04329245,  0.00217755,  0.00240166,  0.0126072 ,  0.01031578,  0.02945673,  0.00732203,  0.00053415,  0.02404676,  0.00196904,  0.00220904],
                       [ 0.08732455,  0.00282201,  0.06185917,  0.02275521,  0.00102026,  0.01872319,  0.0090679 ,  0.02578083,  0.04573099,  0.01367218,  0.09783896,  0.08250476,  0.12331494,  0.18591082,  0.00767206,  0.00109938,  0.03513663,  0.01912476,  0.02233775,  0.04200301,  0.00230229,  0.00262574,  0.01415441,  0.01037127,  0.0282956 ,  0.00738203,  0.00064483,  0.02361585,  0.00262794,  0.00228069],
                       [ 0.08830023,  0.00274117,  0.06203244,  0.02175028,  0.00088772,  0.01844149,  0.0090679 ,  0.02484741,  0.04441615,  0.01366516,  0.09509586,  0.08388089,  0.12344291,  0.1877422 ,  0.00764006,  0.00160988,  0.03570184,  0.01968244,  0.02281553,  0.04235688,  0.00232851,  0.0024947 ,  0.0148043 ,  0.0105314 ,  0.02739511,  0.00721107,  0.00067298,  0.02333887,  0.00278495,  0.00231967],
                       [ 0.09166121,  0.00271643,  0.0617476 ,  0.02281615,  0.00086299,  0.01885232,  0.0090679 ,  0.02536715,  0.04781916,  0.01359708,  0.09545621,  0.08177891,  0.12365185,  0.18378782,  0.00709599,  0.0010056 ,  0.03437899,  0.01858127,  0.02260744,  0.04244274,  0.00229771,  0.0025531 ,  0.01489245,  0.01046908,  0.02757243,  0.00732655,  0.00065426,  0.02412974,  0.00257179,  0.00223807],
                       [ 0.0924805 ,  0.0027403 ,  0.06216503,  0.02192656,  0.00084175,  0.01840325,  0.0090679 ,  0.02629784,  0.04518925,  0.01379864,  0.09542026,  0.08106194,  0.12394086,  0.18699197,  0.00774729,  0.00134999,  0.03278725,  0.01886988,  0.02248048,  0.04260678,  0.00232312,  0.00264785,  0.01496563,  0.01048684,  0.02681028,  0.00731037,  0.00066188,  0.02360581,  0.00272346,  0.00229701],
                       [ 0.09077955,  0.00257482,  0.06203224,  0.02207334,  0.00093844,  0.0185044 ,  0.0090679 ,  0.02636786,  0.0470137 ,  0.01362856,  0.09557463,  0.08230301,  0.12325734,  0.18320805,  0.00731111,  0.00123322,  0.0366022 ,  0.01942819,  0.02276819,  0.04281577,  0.00229891,  0.00259363,  0.0147708 ,  0.01050825,  0.0271113 ,  0.0074037 ,  0.00066641,  0.0223832 ,  0.00260812,  0.00217318],
                       [ 0.08818208,  0.00252547,  0.06216641,  0.0218309 ,  0.00077606,  0.0187262 ,  0.0090679 ,  0.02701812,  0.0431736 ,  0.01341656,  0.09801607,  0.08315526,  0.12339248,  0.1887604 ,  0.0073875 ,  0.0008197 ,  0.03594903,  0.01931809,  0.02145353,  0.04232872,  0.00232655,  0.00259332,  0.01399838,  0.0102978 ,  0.02788968,  0.00738055,  0.00066479,  0.0225794 ,  0.00256137,  0.00224409],
                       [ 0.08956867,  0.00256433,  0.06197572,  0.02226618,  0.0009576 ,  0.01874285,  0.0090679 ,  0.02562295,  0.04383928,  0.0137876 ,  0.09565533,  0.07926315,  0.12378479,  0.19023587,  0.00750308,  0.00139078,  0.03485272,  0.01931067,  0.02281811,  0.04268318,  0.00229828,  0.00255915,  0.01441774,  0.01046551,  0.02787124,  0.00738531,  0.00066907,  0.02364569,  0.00250356,  0.00229367],
                       [ 0.09170159,  0.00286943,  0.06242348,  0.02186803,  0.00086361,  0.01862247,  0.0090679 ,  0.02572762,  0.04647678,  0.01355894,  0.09646782,  0.07921483,  0.12290006,  0.18604198,  0.00729329,  0.00115614,  0.03658668,  0.01890703,  0.02295463,  0.04321221,  0.00230384,  0.00255475,  0.01463856,  0.01043509,  0.026839  ,  0.00737818,  0.00070707,  0.02245435,  0.00250719,  0.00226745],
                       [ 0.08990879,  0.00262185,  0.06206472,  0.0226325 ,  0.00082142,  0.01872795,  0.0090679 ,  0.02616071,  0.04374308,  0.01385171,  0.09634374,  0.08006556,  0.12304881,  0.18917788,  0.00733943,  0.00132922,  0.03469997,  0.02017345,  0.02239047,  0.04261402,  0.00235612,  0.00255601,  0.01476848,  0.01047445,  0.02728667,  0.00747824,  0.00067386,  0.02265932,  0.00264075,  0.00232294],
                       [ 0.09091283,  0.00273242,  0.06191903,  0.02169473,  0.00080021,  0.01859412,  0.0090679 ,  0.02544375,  0.04464484,  0.0135166 ,  0.09645115,  0.08181104,  0.1235138 ,  0.18707575,  0.00747054,  0.00119977,  0.03569719,  0.02063754,  0.02242507,  0.04238548,  0.00230094,  0.00257439,  0.01477268,  0.01044111,  0.0277199 ,  0.0072608 ,  0.00069039,  0.02125999,  0.00267429,  0.00231174],
                       [ 0.09293146,  0.00273476,  0.06220092,  0.02405753,  0.00091935,  0.0186273 ,  0.0090679 ,  0.0248047 ,  0.0449825 ,  0.01382657,  0.09621282,  0.07862384,  0.12345585,  0.18414417,  0.00747431,  0.00098298,  0.0361652 ,  0.01947477,  0.0229855 ,  0.04240102,  0.00230442,  0.00259378,  0.01408976,  0.01051316,  0.02821205,  0.00740865,  0.000664  ,  0.02337174,  0.00247714,  0.00229185],
                       [ 0.09057597,  0.0027093 ,  0.06219292,  0.02308425,  0.00097258,  0.01861383,  0.0090679 ,  0.02443732,  0.04532125,  0.01360601,  0.09596177,  0.08004616,  0.12308597,  0.18795074,  0.00759698,  0.0012768 ,  0.03463049,  0.01929736,  0.02350042,  0.04243354,  0.00222764,  0.00261582,  0.01399825,  0.01052742,  0.02808343,  0.00746045,  0.00068594,  0.02296515,  0.00273465,  0.00233969],
                       [ 0.09303495,  0.00269764,  0.06197141,  0.02155112,  0.00096374,  0.01867602,  0.0090679 ,  0.02552936,  0.04522768,  0.01382011,  0.09674114,  0.08215877,  0.12340033,  0.18338232,  0.00736706,  0.00117352,  0.03503989,  0.02059159,  0.02230166,  0.04242186,  0.00236052,  0.00255252,  0.01524996,  0.0104277 ,  0.02765173,  0.00725119,  0.00067399,  0.02180105,  0.00258749,  0.00232577],
                       [ 0.09107159,  0.00266933,  0.06243008,  0.02203644,  0.00084825,  0.018599  ,  0.0090679 ,  0.02580955,  0.04733641,  0.01375998,  0.0949941 ,  0.08128923,  0.12302905,  0.18359479,  0.00729246,  0.0010219 ,  0.03654777,  0.01916174,  0.02267383,  0.04297163,  0.00228681,  0.00261155,  0.01472641,  0.01028117,  0.02830554,  0.00724662,  0.0006371 ,  0.02287057,  0.00255059,  0.0022786 ],
                       [ 0.09014059,  0.00285379,  0.06177245,  0.02055939,  0.00092797,  0.01864803,  0.0090679 ,  0.02579573,  0.0422949 ,  0.01368921,  0.09578997,  0.08166043,  0.12341015,  0.19137298,  0.00758128,  0.00114166,  0.03472303,  0.02031056,  0.02176257,  0.04298923,  0.00227714,  0.00256678,  0.01443623,  0.0103986 ,  0.02754303,  0.00743275,  0.00066852,  0.02294482,  0.00292756,  0.00231274],
                       [ 0.09311978,  0.00275427,  0.06210637,  0.02288694,  0.00098037,  0.01838902,  0.0090679 ,  0.02685804,  0.04706914,  0.01379787,  0.09346745,  0.08100042,  0.12375257,  0.18422264,  0.00745028,  0.00138174,  0.03559115,  0.0196335 ,  0.02140385,  0.04249269,  0.00231238,  0.00252149,  0.01472975,  0.01059748,  0.02711962,  0.00737082,  0.00067104,  0.02205152,  0.00282073,  0.00237916]])

'''
=======================================================
                  Function definitions
=======================================================
'''

# Pre: probs is an array of n probabilities, should add up to 1
# Post: Returns an integer in the range [0, n)
#       Probability of returning i is probs[i]
def getRandomIndex(probs):    
    randNum = random.random()
    currProb = 0
    
#    print(repr(probs) + " - " + repr(randNum))
    for i in range(len(probs)):
        currProb = currProb + probs[i]
        
        if randNum < currProb:
            return i

    return len(probs) - 1

def randomWalker(mat, loc):
    row = mat[loc]
    return getRandomIndex(row)

def randomWalk(mat, start, target):
    loc = start
    i = 0
    while (loc != target) and (i <= 50000):
        loc = randomWalker(mat, loc)
        i = i + 1
  #      print(loc)

    return i


'''
=======================================================
                     Runtime Stuff
=======================================================
'''

reps = 200

names = ["Adrenal", "Bladder", "Bone", "Brain", "Breast", "Diaphragm", "Gall-bladder", "Heart", "Kidney", "Large Intestine", "Liver", "Lung", "LN (dist)", "LN (reg)", "Omentum", "Ovary", "Pancreas", "Pericardium", "Peritoneum", "Pleura", "Prostate", "Skeletal Muscle", "Skin", "Small Intestine", "Spleen", "Stomach","Testis", "Thyroid", "Uterus", "Vagina"]

for i in range(len(transition)):
    p = 0
    
    for j in range(reps):
        p = p + randomWalk(transition, start, i)
#        print("-", end=" ")

    print(names[i] + ": " + repr(p/reps))
