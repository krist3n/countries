import random

regions=["all","af","as","au","eu","na","oc","sa"]
countries={"afghanistan":"as","albania":"eu","algeria":"af","andorra":"eu","angola":"af","antigua and barbuda":"na","argentina":"sa","armenia":"as",
           "australia":"oc","austria":"eu","azerbaijan":"as","bahamas":"na","bahrain":"as","bangladesh":"as","barbados":"na","belarus":"eu",
           "belgium":"eu","belize":"na","benin":"af","bolivia":"sa","bosnia and herzegovina":"eu","botswana":"af","brazil":"sa","brunei":"as",
           "bulgaria":"eu","burkina faso":"af","burma":"as","burundi":"af","cabo verde":"af","cambodia":"as","cameroon":"af","canada":"na",
           "cayman islands":"na","central african republic":"af","chad":"af","chile":"sa","china":"as","colombia":"sa","comoros":"af", "cook islands":"oc",
           "costa rica":"na","cote d'ivoire":"af","croatia":"ea","cuba":"na","cyprus":"eu","czech republic":"eu","congo":"af","denmark":"eu",
           "djibouti":"af","dominica":"na","dominican republic":"na","ecuador":"sa","egypt":"af","el salvador":"na","equatorial guinea":"af","eritrea":"af",
           "estonia":"eu","swaziland":"af","ethiopia":"af","fiji":"oc","finland":"eu","france":"eu","gabon":"af","gambia":"af","georgia":"as",
           "germany":"eu","ghana":"af","greece":"eu","grenada":"na","guatemala":"na","guinea":"af","guinea-bissau":"af","guyana":"sa","haiti":"na",
           "vatican city":"eu","honduras":"na","hungary":"eu","iceland":"eu","india":"as","indonesia":"as","iran":"as","iraq":"as","ireland":"eu",
           "italy":"eu","jamaica":"af","japan":"as","jordan":"as","kazakhstan":"as","kenya":"af","kiribati":"oc","north korea":"as","kosovo":"eu",
           "kuwait":"as","kyrgyzstan":"as","laos":"as","latvia":"eu","lebanon":"as","lesotho":"af","liberia":"af","libya":"af","liechtenstein":"eu",
           "lithuania":"eu","luxembourg":"eu","madagascar":"af","malawi":"af","malaysia":"as","maldives":"as","mali":"af","malta":"eu",
           "marshall islands":"oc","mauritania":"af","mauritius":"af","mexico":"na","micronesia":"oc","moldova":"eu","monaco":"eu","mongolia":"as",
           "montenegro":"eu","morocco":"af","mozambique":"af","namibia":"af","nauru":"oc","nepal":"as","netherlands":"eu","new zealand":"oc",
           "nicaragua":"na","niger":"af","nigeria":"af","niue":"oc","north macedonia":"eu","norway":"eu","oman":"as","pakistan":"as","palau":"oc",
           "panama":"na","papua new guinea":"oc","paraguay":"sa","peru":"sa","philippines":"as","poland":"eu","portugal":"eu","qatar":"as",
           "south korea":"as","democratic republic of congo":"af","romania":"eu","russia":"as","rwanda":"af","saint kitts and nevis":"na",
           "saint lucia":"na","saint vincent and the grenadines":"na","samoa":"oc","san marino":"eu","sao tome and principe":"af",
           "saudi arabia":"as","senegal":"af","serbia":"eu","seychelles":"af","sierra leone":"af","singapore":"as","slovakia":"eu","slovenia":"eu",
           "solomon islands":"oc","somalia":"af","south africa":"af","south sudan":"af","spain":"eu","sri lanka":"as","sudan":"af","suriname":"sa",
           "sweden":"eu","switzerland":"eu","syria":"eu","tajikistan":"as","tanzania":"af","thailand":"as","timor-leste":"as","togo":"af","tonga":"oc",
           "trinidad and tobago":"na","tunisia":"af","turkey":"as","turkmenistan":"as","tuvalu":"oc","uganda":"af","ukraine":"eu",
           "united arab emirates":"as","united states of america":"na","uruguay":"sa","uzbekistan":"as","vanuatu":"oc","venezuela":"sa","vietnam":"as",
           "yemen":"as","zambia":"af","zimbabwe":"af"}
guessed={}

def gamemode():
    while True:
        mode = input("select gamemode (all, af, as, au, eu, na, oc, sa): ")
        if mode=="all":
            break
        elif mode in regions:
            updCountries(mode)
            break
        else:
            print("invalid gamemode!")

def updCountries(mode):
    for country in list(countries.keys()):
        if countries[country]!=mode:
            del countries[country]

def update(guess):
    guessed[guess]=countries[guess]
    del countries[guess]

def c_turn():
    c_guess=random.choice(list(countries.keys()))
    update(c_guess)
    print("computer's turn: "+c_guess)

def p_turn():
    while True:
        p_guess=input("your turn: ")
        if p_guess=="quit":
            return p_guess
        if p_guess in countries.keys() and p_guess not in guessed.keys():
            update(p_guess)
            return p_guess
        print("invalid guess! try again!")

def score():
    if len(countries)!=0:
        print("these are the countries you did not guess:")
        for country in countries.keys():
            print("\t"+country)
    print("guessed "+str(len(guessed))+" countries!")

def main():
    gamemode()
    while len(countries)!=0:
        c_turn()
        p_guess=p_turn()

        if p_guess=="quit":
            print("game end.")
            break
    score()

if __name__ == "__main__":
    main()