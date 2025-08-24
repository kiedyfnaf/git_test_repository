import random
k = 1
a = input("Hasło: ")
sus = ['Symbol', 'Liczba atomowa', 'Masa atomowa', 'Stan skupienia', 'Charakter chemiczny']
H = ['1', '1,0', 'gaz', 'niemetal', 'H']
if a == 'los':
    v = random.choice(('wodór', 'hel', 'lit', 'beryl', 'bor', 'węgiel', 'azot', 'tlen', 'fluor', 'neon', 'sód', 'magnez', 'glin', 'krzem', 'fosfor', 'siarka', 'chlor', 'argon', 'potas', 'wapń', 'skand', 'tytan', 'wanad', 'chrom', 'mangan', 'żelazo', 'kobalt', 'nikiel', 'miedź', 'cynk', 'gal', 'german', 'arsen', 'selen', 'brom', 'krypton', 'rubid', 'stront', 'itr', 'cyrkon', 'niob', 'molibden', 'technet', 'ruten', 'rod', 'pallad', 'srebro', 'kadm', 'ind', 'cyna', 'antymon', 'tellur', 'jod', 'ksenon', 'cez', 'bar', 'lantan', 'cer', 'prazeodym', 'neodym', 'promet', 'samar', 'europ', 'gadolin', 'terb', 'dysproz', 'holm', 'erb', 'tul', 'iterb', 'lutet', 'hafn', 'tantal', 'wolfram', 'ren', 'osm', 'iryd', 'platyna', 'złoto', 'rtęć', 'tal', 'ołów', 'bizmut', 'polon', 'astat', 'radon', 'frans', 'rad', 'aktyn', 'tor', 'protaktyn', 'uran', 'neptun', 'pluton', 'ameryk', 'kiur',  'berkel', 'kaliforn', 'einstein', 'ferm', 'mendelew',  'nobel', 'lorens', 'rutherford', 'dubn', 'seaborg', 'bohr', 'has', '	meitner', 'darmsztadt', 'roentgen', 'kopernik', 'nihon', 'flerow', 'moskow', 'liwermor', 'tenes', 'oganeson'))
    if v == v:
        print(f'Pierwiastek: [{v}]')
        f = input(f'Napisz {random.choice(sus)}:  ')
        if v == 'wodór':
            H =  ['1', '1,0', 'gaz', 'niemetal', 'H']
        elif v == 'hel':
            H =  ['2', '4,0', 'gaz', 'niemetal/gaz', 'He']
        elif v == 'lit':
            H =  ['3', '6,9', 'stały', 'metal', 'Li']
        elif v == 'beryl':
            H =  ['4', '9,0', 'stały', 'metal', 'Be']
        elif v == 'bor':
            H =  ['5', '10,8', 'stały', 'niemetal/półmetal', 'B']
        elif v == 'węgiel':
            H =  ['6', '12,0', 'stałe', 'niemetal/półmetal', 'C']
        elif v == 'azot':
            H =  ['7', '14,0', 'gaz', 'niemetal', 'N']
        elif v == 'tlen':
            H =  ['8', '15,9', 'gaz', 'niemetal', 'O']
        elif v == 'fluor':
            H =  ['9', '18,9', 'gaz', 'niemetal', 'F']
        elif v == 'neon':
            H =  ['10', '20,1', 'gaz', 'niemetal/gaz', 'Ne']
        elif v == 'sód':
            H =  ['11', '22,9', 'stały', 'metal', 'Na']
        elif v == 'magnez':
            H =  ['12', '24,3', 'stały', 'metal', 'Mg']
        elif v == 'glin':
            H =  ['13', '26,9', 'stały', 'metal/półmetal', 'Al']
        elif v == 'krzem':
            H =  ['14', '28,0', 'stały', 'niemetal/półmetal', 'Si']
        elif v == 'fosfor':
            H =  ['15', '30,9', 'stały', 'niemetal/półmetal', 'P']
        elif v == 'siarka':
            H =  ['16', '32,0', 'stały', 'niemetal', 'S']
        elif v == 'chlor':
            H =  ['17', '35,4', 'gaz', 'niemetal', 'Cl']
        elif v == 'argon':
            H =  ['18', '39,9', 'gaz', 'niemetal/gaz', 'Ar']
        elif v == 'potas':
            H =  ['19', '39,0', 'stały', 'metal', 'K']
        elif v == 'wapń':
            H =  ['20', '40,0', 'stały', 'metal', 'Ca']
        elif v == 'skand':
            H =  ['21', '44,9', 'stały', 'metal', 'Sc']
        elif v == 'tytan':
            H =  ['22', '47,8', 'stały', 'metal', 'Ti']
        elif v == 'wanad':
            H =  ['23', '50,9', 'stały', 'metal', 'V']
        elif v == 'chrom':
            H =  ['24', '51,9', 'stały', 'metal', 'Cr']
        elif v == 'mangan':
            H =  ['25', '54,9', 'stały', 'metal', 'Mn']
        elif v == 'żelazo':
            H =  ['26', '55,8', 'stały', 'metal', 'Fe']
        elif v == '	kobalt':
            H =  ['27', '58,9', 'stały', 'metal', 'Co']
        elif v == 'nikiel':
            H =  ['28', '58,6', 'stały', 'metal', 'Ni']
        elif v == 'miedź':
            H =  ['29', '63,5', 'stały', 'metal', 'Cu']
        elif v == 'cynk':
            H =  ['30', '65,3', 'stały', 'metal', 'Zn']
        elif v == 'gal':
            H =  ['31', '69,7', 'stały', 'metal', 'Ga']
        elif v == 'german':
            H =  ['32', '72,6', 'stały', 'metal/półmetal', 'Ge']
        elif v == 'arsen':
            H =  ['33', '74,9', 'stały', 'niemetal/półmetal', 'As']
        elif v == 'selen':
            H =  ['34', '78,9', 'stały', 'niemetal', 'Se']
        elif v == 'brom':
            H =  ['35', '79,9', 'ciecz', 'niemetal', 'Br']
        elif v == 'krypton':
            H =  ['36', '83,7', 'gaz', 'niemetal/gaz', 'Kr']
        elif v == 'rubid':
            H =  ['37', '85,4', 'stały', 'metal', 'Rb']
        elif v == 'stront':
            H =  ['38', '87,6', 'stały', 'metal', 'Sr']
        elif v == 'itr':
            H =  ['39', '88,9', 'stały', 'metal', 'Y']
        elif v == 'cyrkon':
            H =  ['40', '91,2', 'stały', 'metal', 'Zr']
        elif v == 'niob':
            H =  ['41', '92,9', 'stały', 'metal', 'Nb']
        elif v == 'molibden':
            H =  ['42', '95,9', 'stały', 'metal', 'Mo']
        elif v == 'technet':
            H =  ['43', '97.9', 'stały', 'metal', 'Tc']
        elif v == 'ruten':
            H =  ['44', '101,0', 'stały', 'metal', 'Ru']
        elif v == '	rod':
            H =  ['45', '102,9', 'stały', 'metal', 'Rh']
        elif v == 'pallad':
            H =  ['46', '106,4', 'stały', 'metal', 'Pd']
        elif v == 'srebro':
            H =  ['47', '107,8', 'stały', 'metal', 'Ag']
        elif v == 'kadm':
            H =  ['48', '112,4', 'stały', 'metal', 'Cd']
        elif v == 'ind':
            H =  ['49', '114,8', 'stały', 'metal', 'In']
        elif v == 'cyna':
            H =  ['50', '118,7', 'stały', 'metal', 'Sn']
        elif v == 'antymon':
            H =  ['51', '121,7', 'stały', 'metal', 'Sb']
        elif v == 'tellur':
            H =  ['52', '127,6', 'stały', 'metal', 'Te']
        elif v == 'jod':
            H =  ['53', '126,9', 'stały', 'niemetal', 'I']
        elif v == 'ksenon':
            H =  ['54', '131,2', 'gaz', 'metal', 'Xe']
        elif v == 'cez':
            H =  ['55', '132,9', 'stały', 'metal', 'Cs']
        elif v == 'bar':
            H =  ['56', '137,3', 'stały', 'metal', 'Ba']
        elif v == 'lantan':
            H =  ['57', '138,9', 'stały', 'metal', 'La']
        elif v == 'cer':
            H =  ['58', '140,1', 'stały', 'metal', 'Ce']
        elif v == 'prazeodym':
            H =  ['59', '140,9', 'stały', 'metal', 'Pr']
        elif v == 'neodym':
            H =  ['60', '144,2', 'stały', 'metal', 'Nd']
        elif v == 'promet':
            H =  ['61', '144.9', 'stały', 'metal', 'Pm']
        elif v == 'samar':
            H =  ['62', '150,3', 'stały', 'metal', 'Sm']
        elif v == 'europ':
            H =  ['63', '151,9', 'stały', 'metal', 'Eu']
        elif v == 'gadolin':
            H =  ['64', '157,2', 'stały', 'metal', 'Gd']
        elif v == 'terb':
            H =  ['65', '158,9', 'stały', 'metal', 'Tb']
        elif v == 'dysproz':
            H =  ['66', '162,5', 'stały', 'metal', 'Dy']
        elif v == 'holm':
            H =  ['67', '164,9', 'stały', 'metal', 'Ho']
        elif v == 'erb':
            H =  ['68', '167,2', 'stały', 'metal', 'Er']
        elif v == 'tul':
            H =  ['69', '168,9', 'stały', 'metal', 'Tm']
        elif v == 'iterb':
            H =  ['70', '173,0', 'stały', 'metal', 'Yb']
        elif v == 'lutet':
            H =  ['71', '174,9', 'stały', 'metal', 'Lu']
        elif v == 'hafn':
            H =  ['72', '178,4', 'stały', 'metal', 'Hf']
        elif v == 'tantal':
            H =  ['73', '180,9', 'stały', 'metal', 'Ta']
        elif v == 'wolfram':
            H =  ['74', '183,8', 'stały', 'metal', 'W']
        elif v == 'ren':
            H =  ['75', '186,2', 'stały', 'metal', 'Re']
        elif v == 'osm':
            H =  ['76', '190,2', 'stały', 'metal', 'Os']
        elif v == 'iryd':
            H =  ['77', '192,2', 'stały', 'metal', 'Ir']
        elif v == 'platyna':
            H =  ['78', '195,0', 'stały', 'metal', 'Pt']
        elif v == 'złoto':
            H =  ['79', '196,9', 'stały', 'metal', 'Au']
        elif v == 'rtęć':
            H =  ['80', '200,5', 'ciecz', 'metal', 'Hg']
        elif v == 'tal':
            H =  ['81', '204,3', 'stały', 'metal', 'Tl']
        elif v == 'ołów':
            H =  ['82', '207,2', 'stały', 'metal', 'Pb']
        elif v == 'bizmut':
            H =  ['83', '208,9', 'stały', 'metal', 'Bi']
        elif v == 'polon':
            H =  ['84', '208.9', 'stały', 'metal/półmetal', 'Po']
        elif v == 'astat':
            H =  ['85', '209.9', 'stały', 'niemetal/półmetal', 'At']
        elif v == 'radon':
            H =  ['86', '222.0', 'gaz', 'niemetal/gaz', 'Rn']
        elif v == 'frans':
            H =  ['87', '223.0', 'stały', 'metal', 'Fr']
        elif v == 'rad':
            H =  ['88', '226.0', 'stały', 'metal', 'Ra']
        elif v == 'aktyn':
            H =  ['89', '227.0', 'stały', 'metal', 'Ac']
        elif v == 'tor':
            H =  ['90', '232,0', 'stały', 'metal', 'Th']
        elif v == 'protaktyn':
            H =  ['91', '231,0', 'stały', 'metal', 'Pa']
        elif v == 'uran':
            H =  ['92', '238,0', 'stały', 'metal', 'U']
        elif v == 'neptun':
            H =  ['93', '237.0', 'stały', 'metal', 'Np']
        elif v == 'pluton':
            H =  ['94', '244.0', 'stały', 'metal', 'Pu']
        elif v == 'ameryk':
            H =  ['95', '243.0', 'stały', 'metal', 'Am']
        elif v == 'kiur':
            H =  ['96', '247,0', 'stały', 'metal', 'Cm']
        elif v == 'berkel':
            H =  ['97', '247,0', 'stały', 'metal', 'Bk']
        elif v == 'kaliforn':
            H =  ['98', '251,0', 'stały', 'metal', 'Cf']
        elif v == 'einstein':
            H =  ['99', '252,0', 'stały', 'metal', 'Es']
        elif v == 'ferm':
            H =  ['100', '257,0', 'stały', 'metal', 'Fm']
        elif v == 'mendelew':
            H =  ['101', '258,0', 'stały', 'metal', 'Md']
        elif v == 'nobel':
            H =  ['102', '259,0', 'stały', 'metal', 'No']
        elif v == 'lorens':
            H =  ['103', '262,0', 'stały', 'metal', 'Lr']
        elif v == 'rutherford':
            H =  ['104', '267,0', 'stały', 'metal', 'Rf']
        elif v == 'dubn':
            H =  ['105', '268,0', 'stały', 'metal', 'Db']
        elif v == 'seaborg':
            H =  ['106', '269,0', 'stały', 'metal', 'Sg']
        elif v == 'bohr':
            H =  ['107', '270,0', 'stały', 'metal', 'Bh']
        elif v == 'has':
            H =  ['108', '269,0', 'stały', 'metal', 'Hs']
        elif v == 'meitner':
            H =  ['109', '277,0', 'stały', 'metal', 'Mt']
        elif v == 'darmsztadt':
            H =  ['110', '281,0', 'stały', 'metal', 'Ds']
        elif v == 'roentgen':
            H =  ['111', '282,0', 'stały', 'metal', 'Rg']
        elif v == 'kopernik':
            H =  ['112', '285,0', 'stały', 'metal', 'Cn']
        elif v == 'nihon':
            H =  ['113', '286,0', 'stały', 'metal', 'Nh']
        elif v == 'flerow':
            H =  ['114', '290,0', 'stały', 'metal', 'Fl']
        elif v == 'moskow':
            H =  ['115', '290,0', 'stały', 'metal', 'Mc']
        elif v == 'liwermor':
            H =  ['116', '293,0', 'stały', 'metal', 'Lv']
        elif v == 'tenes':
            H =  ['117', '294,0', 'stały', 'niemetal', 'Ts']
        elif v == 'oganeson':
            H =  ['118', '294,0', 'stały', 'niemetal', 'Og']
        if f in H:
            print('Well done.')
        else:
            print(H[:5])

    


   