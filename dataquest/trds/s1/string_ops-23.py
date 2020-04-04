from pprint import pprint as pp
lyrics = ' white lips, pale face \n breathing in snowflakes \n burnt lungs sour taste \n lights gone days end \n struggling to pay rent \n long nights strange men \n and they say \n shes in the class a team \n stuck in her daydream \n been this way since 18 \n but lately her face seems  \n slowly sinking wasting \n crumbling like pastries \n they scream \n the worst things in life come free to us \n cause were just under the upperhand \n and go mad for a couple grams \n and she dont want to go outside tonight \n and in a pipe she flies to the motherland \n or sells love to another man \n its too cold outside \n for angels to fly \n angels to fly \n ripped gloves raincoat \n tried to swim stay afloat \n dry house wet clothes \n loose change bank notes \n wearyeyed dry throat \n cool girl no phone \n and they say \n shes in the class a team \n stuck in her daydream \n been this way since 18 \n but lately her face seems \n slowly sinking wasting \n crumbling like pastries \n and they scream \n the worst things in life come free to us \n cause were just under the upperhand \n and go mad for a couple grams \n but she dont want to go outside tonight \n and in a pipe she flies to the motherland \n or sells love to another man \n its too cold outside \n for angels to fly \n an angel will die \n covered in white \n closed eye \n and hoping for a better life \n this time well fade out tonight \n straight down the line \n and they say \n shes in the class a team \n stuck in her daydream \n been this way since 18 \n but lately her face seems \n slowly sinking wasting \n crumbling like pastries \n they scream \n the worst things in life come free to us \n and were all under the upperhand \n go mad for a couple grams \n and we dont want to go outside tonight \n and in a pipe we fly to the motherland \n or sell love to another man \n its too cold outside \n for angels to fly \n angels to fly \n to fly fly \n for angels to fly to fly to fly \n angels to die'

#print(lyrics)

a_team = lyrics.split("\n")


ed_sheeran = [list(x) for x in a_team]

#pp(ed_sheeran[:2])


ed_sheeran = [ [chars[0]]+[chars[1].upper()] + chars[2:] for chars in ed_sheeran ]

ed_sheeran = ["".join(chars) for chars in ed_sheeran]

ed_sheeran_full = "\n".join(ed_sheeran)


ed_sheeran_full = ""
for line in ed_sheeran:
    ed_sheeran_full += line+'\n'


#print(ed_sheeran_full)

mad_libs =  [' {ADJ} {NOUN}, pale face ', ' Breathing in {NOUN} ', ' Burnt {NOUN} {ADJ} taste ', ' Lights gone days end ', ' Struggling to pay {NOUN} ', ' Long nights strange {NOUN} ', ' And they say ', ' Shes in the class a team ', ' Stuck in her {NOUN} ', ' Been this way since {AGE}', 'But lately her {NOUN} seems  ', ' Slowly sinking wasting ', ' Crumbling like {NOUN_PLURAL} ', ' They {VERB} ', ' The worst things in life come free to us ', ' Cause were just under the upperhand ', ' And go mad for a couple {NOUN_PLURAL} ', ' And she dont want to go outside tonight ', ' And in a pipe she flies to the {LOCATION} ', ' Or sells love to {CELEBRITY} ', ' Its too cold outside ', ' For angels to {VERB} ', ' Angels to {VERB} ', ' Ripped {NOUN} raincoat ', ' Tried to {VERB} stay afloat ', ' {ADJ} house wet clothes ', ' Loose change bank notes ', ' Weary eyed {ADJ} throat ', ' Cool girl no phone ', ' And they say ', ' Shes in the class a team ', ' Stuck in her {NOUN} ', ' Been this way since {AGE} ', ' But lately her face seems ', ' Slowly sinking wasting ', ' Crumbling like {NOUN} ', ' And they {VERB} ', ' The worst things in life come free to us ', ' Cause were just under the {NOUN} ', ' And go mad for a couple grams ', ' But she dont want to go outside tonight ', ' And in a pipe she flies to the {LOCATION} ', ' Or sells love to another man ', ' Its too cold outside ', ' For angels to {VERB} ', ' An angel will die ', ' Covered in white ', ' Closed eye ', ' And hoping for a better life ', ' This time well fade out tonight ', ' Straight down the line ', ' And they {VERB} ', ' Shes in the class a team ', ' Stuck in her {NOUN} ', ' Been this way since {AGE} ', ' But lately her face seems ', ' Slowly sinking wasting ', ' Crumbling like pastries ', ' They {VERB} ', ' The worst things in life come free to us ', ' And were all under the upperhand ', ' Go mad for a couple grams ', ' And we dont want to go outside tonight ', ' And in a pipe we {VERB} to the motherland ', ' Or {VERB} love to another man ', ' Its too cold outside ', ' For angels to fly ', ' Angels to fly ', ' To fly fly ', ' For angels to {VERB} to {VERB} to {VERB} ', ' Angels to {VERB}']

mad_libs_joined = "\n".join(mad_libs)

mad_libs_joined = mad_libs_joined.replace("{ADJ}", "stinky")
mad_libs_joined = mad_libs_joined.replace("{NOUN}", "piano")
mad_libs_joined = mad_libs_joined.replace("{AGE}", "99")
mad_libs_joined = mad_libs_joined.replace("{NOUN_PLURAL}", "phones")
mad_libs_joined = mad_libs_joined.replace("{VERB}", "crush")
mad_libs_joined = mad_libs_joined.replace("{LOCATION}", "Antarctica")
mad_libs_joined = mad_libs_joined.replace("{CELEBRITY}", "Beyonce")


#print(mad_libs_joined)

s = "White lips, pale face"
first_line = "White {0}, pale {1}".format("hat","skin")
pp(first_line)

mad_libs_joined = "\n".join(mad_libs)

final = mad_libs_joined.format(ADJ="stinky", NOUN="piano", AGE="99",
                              NOUN_PLURAL="phones", VERB="crush",
                              LOCATION="Antarctica", CELEBRITY="Beyonce")

pp(final)

