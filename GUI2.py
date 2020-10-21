import PySimpleGUI as sg
from main import meerkeuzevragen_ophalen

data = meerkeuzevragen_ophalen("meerkeuzevragen.txt")

SE = 0
BDAM = 0
FICT = 0
IAT = 0
# dict_richtingen = {'Software Engineering': 0, 'Business Data Management': 0, 'Interactie-technologie': 0,
#                    'Forensisch ICT': 0}
window_teller = 0
se_uitslag = "Software Engineering is voor jou weggelegd! \nUit jouw keuzes blijkt dat je het liefst de hele dag bezig bent met programmeren en dat je het niet erg vindt om fouten te maken. \nJe bent gewend aan constante verandering en je vindt het ook niet erg om altijd nieuwe dingen te leren. \nDaarom past deze specialisatie het best bij jou."
bdam_uitslag = "Je bent een echte carrieretijger. \nJe analytisch vermogen is van hoog niveau en je kan probleemoplossend denken. \nJe hebt verstand van databases en computer mainframes en kan goed samenwerken. \nJe houdt van getallen, vooral op je bankrekening. \nHierom past BDAM het best bij jou."
iat_uitslag = "Mensen vinden jou creatief. \nJe bent sociaal en houdt ervan om te werken met mensen. \nJe vindt technologie interessant en je wilt dit ook graag makkelijker maken voor anderen. \nVerder kan je goed organiseren en kan je je goed dingen inbeelden. \nIAT is dus DE specialisatie voor jou!"
fict_uitslag = "Gerechtigheid is waar het voor jou allemaal om draait. \nJe vindt het leuk om systemen te testen, op speurtocht te gaan en om gevarieerd werk te hebben! \nBij de politie of defensie werken lijkt jou een top baan. Om deze redenen past Forensisch ICT bij jou."
text_uitslag = ""
uitslag = ""

sg.theme("Topanga")
sg.SetOptions(element_padding=((10, 40), 5))
layout1 = [[sg.Button(data[1], size=(25, 3)), sg.Button(data[2], size=(25, 3))]]
layout2 = [[sg.Button(data[3], size=(25, 3)), sg.Button(data[4], size=(25, 3))]]
layout_column_vraag4_1 = [[sg.Button(data[14], size=(30, 3)), sg.Button(data[15], size=(30, 3))]]
layout_column_vraag4_2 = [[sg.Button(data[16], size=(30, 3)), sg.Button(data[17], size=(30, 3))]]
layout_column_vraag13_1 = [[sg.Button(data[55], size=(30, 3)), sg.Button(data[56], size=(30, 3))]]
layout_column_vraag13_2 = [[sg.Button(data[57], size=(30, 3)), sg.Button(data[58], size=(30, 3))]]
layout_column_vraag15_1 = [[sg.Button(data[65], size=(30, 3)), sg.Button(data[66], size=(30, 3))]]
layout_column_vraag15_2 = [[sg.Button(data[67], size=(30, 3)), sg.Button(data[68], size=(30, 3))]]
# layout1 = [
#     [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
#     [sg.Text('Pagina 1 van de quiz')],
#     [sg.Text(data[0])],
#     [sg.Button(data[1]), sg.Button(data[2]), sg.Button(data[3]), sg.Button(data[4])]]
layout_column = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 1 van de quiz')],
    [sg.Text(data[0])],
    [sg.Column(layout1)],
    [sg.Column(layout2)]]

layout2 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 2 van de quiz')],
    [sg.Text(data[5])],
    [sg.Button(data[6]), sg.Button(data[7]), sg.Button(data[8]), sg.Button(data[9])]]

layout3 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 3 van de quiz')],
    [sg.Text(data[10])],
    [sg.Button(data[11]), sg.Button(data[12])]]

layout_column_vraag4 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 4 van de quiz')],
    [sg.Text(data[13])],
    [sg.Column(layout_column_vraag4_1)],
    [sg.Column(layout_column_vraag4_2)]]

layout5 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 5 van de quiz')],
    [sg.Text(data[18])],
    [sg.Button(data[19]), sg.Button(data[20]), sg.Button(data[21]), sg.Button(data[22])]]

layout6 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 6 van de quiz')],
    [sg.Text(data[23])],
    [sg.Button(data[24]), sg.Button(data[25]), sg.Button(data[26]), sg.Button(data[27])]]

layout7 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 7 van de quiz')],
    [sg.Text(data[28])],
    [sg.Button(data[29]), sg.Button(data[30]), sg.Button(data[31]), sg.Button(data[32])]]

layout8 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 8 van de quiz')],
    [sg.Text(data[33])],
    [sg.Button(data[34]), sg.Button(data[35]), sg.Button(data[36]), sg.Button(data[37])]]

layout9 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 9 van de quiz')],
    [sg.Text(data[38])],
    [sg.Button(data[39]), sg.Button(data[40])]]

layout10 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 10 van de quiz')],
    [sg.Text(data[41])],
    [sg.Button(data[42]), sg.Button(data[43])]]

layout11 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 11 van de quiz')],
    [sg.Text(data[44])],
    [sg.Button(data[45]), sg.Button(data[46]), sg.Button(data[47]), sg.Button(data[48])]]

layout12 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 12 van de quiz')],
    [sg.Text(data[49])],
    [sg.Button(data[50]), sg.Button(data[51]), sg.Button(data[52]), sg.Button(data[53])]]

layout13 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 13 van de quiz')],
    [sg.Text(data[54])],
    [sg.Column(layout_column_vraag13_1)],
    [sg.Column(layout_column_vraag13_2)]]

layout14 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 14 van de quiz')],
    [sg.Text(data[59])],
    [sg.Button(data[60]), sg.Button(data[61]), sg.Button(data[62]), sg.Button(data[63])]]

layout15 = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Pagina 15 van de quiz')],
    [sg.Text(data[64])],
    [sg.Column(layout_column_vraag15_1)],
    [sg.Column(layout_column_vraag15_2)]]

# if max(dict_richtingen) == 'Software Engineering':
#     text_uitslag = se_uitslag
#
# elif max(dict_richtingen) == 'Business Data Management':
#         text_uitslag = bdam_uitslag
#
# elif max(dict_richtingen) == 'Interactie-technologie':
#         text_uitslag = iat_uitslag
#
# elif max(dict_richtingen) == 'Forensisch ICT':
#         text_uitslag = fict_uitslag


window1 = sg.Window('Window Title', layout_column, size=(1152, 768))
window2 = sg.Window('window title', layout2, size=(1152, 768))
window3 = sg.Window('Window Title', layout3, size=(1152, 768))
window4 = sg.Window('Window Title', layout_column_vraag4, size=(1152, 768))
window5 = sg.Window('Window Title', layout5, size=(1152, 768))
window6 = sg.Window('Window Title', layout6, size=(1152, 768))
window7 = sg.Window('Window Title', layout7, size=(1152, 768))
window8 = sg.Window('Window Title', layout8, size=(1152, 768))
window9 = sg.Window('Window Title', layout9, size=(1152, 768))
window10 = sg.Window('Window Title', layout10, size=(1152, 768))
window11 = sg.Window('Window Title', layout11, size=(1152, 768))
window12 = sg.Window('Window Title', layout12, size=(1152, 768))
window13 = sg.Window('Window Title', layout13, size=(1152, 768))
window14 = sg.Window('Window Title', layout14, size=(1152, 768))
window15 = sg.Window('Window Title', layout15, size=(1152, 768))

if window_teller == 0:
    while True:  # Event Loop
        event, values = window1.Read()
        if event in (None, 'Exit'):
            window1.close()
            break
        if event == data[1]:
            SE += 1
            window_teller += 1
            window1.close()

        elif event == data[2]:
            IAT += 1
            window_teller += 1
            window1.close()

        elif event == data[3]:
            BDAM += 1
            window_teller += 1
            window1.close()

        elif event == data[4]:
            FICT += 1
            window_teller += 1
            window1.close()

if window_teller == 1:
    while True:  # Event Loop
        event, values = window2.Read()
        if event in (None, 'Exit'):
            window2.close()
            break
        if event == data[6]:
            SE += 1
            window_teller += 1
            window2.close()

        elif event == data[7]:
            IAT += 1
            window_teller += 1
            window2.close()

        elif event == data[8]:
            BDAM += 1
            window_teller += 1
            window2.close()

        elif event == data[9]:
            FICT += 1
            window_teller += 1
            window2.close()

if window_teller == 2:
    while True:  # Event Loop
        event, values = window3.Read()
        if event in (None, 'Exit'):
            window3.close()
            break
        if event == data[11]:
            SE += 1
            FICT += 1
            window_teller += 1
            window3.close()

        elif event == data[12]:
            IAT += 1
            BDAM += 1
            window_teller += 1
            window3.close()

if window_teller == 3:
    while True:  # Event Loop
        event, values = window4.Read()
        if event in (None, 'Exit'):
            window4.close()
            break
        if event == data[14]:
            SE += 1
            window_teller += 1
            window4.close()

        elif event == data[15]:
            IAT += 1
            window_teller += 1
            window4.close()

        elif event == data[16]:
            BDAM += 1
            window_teller += 1
            window4.close()

        elif event == data[17]:
            FICT += 1
            window_teller += 1
            window4.close()

if window_teller == 4:
    while True:  # Event Loop
        event, values = window5.Read()
        if event in (None, 'Exit'):
            window5.close()
            break
        if event == data[19]:
            SE += 1
            window_teller += 1
            window5.close()

        elif event == data[20]:
            IAT += 1
            window_teller += 1
            window5.close()

        elif event == data[21]:
            BDAM += 1
            window_teller += 1
            window5.close()

        elif event == data[22]:
            FICT += 1
            window_teller += 1
            window5.close()

if window_teller == 5:
    while True:  # Event Loop
        event, values = window6.Read()
        if event in (None, 'Exit'):
            window6.close()
            break
        if event == data[24]:
            SE += 1
            window_teller += 1
            window6.close()

        elif event == data[25]:
            IAT += 1
            window_teller += 1
            window6.close()

        elif event == data[26]:
            BDAM += 1
            window_teller += 1
            window6.close()

        elif event == data[27]:
            FICT += 1
            window_teller += 1
            window6.close()

if window_teller == 6:
    while True:  # Event Loop
        event, values = window7.Read()
        if event in (None, 'Exit'):
            window7.close()
            break
        if event == data[29]:
            SE += 1
            window_teller += 1
            window7.close()

        elif event == data[30]:
            IAT += 1
            window_teller += 1
            window7.close()

        elif event == data[31]:
            BDAM += 1
            window_teller += 1
            window7.close()

        elif event == data[32]:
            FICT += 1
            window_teller += 1
            window7.close()

if window_teller == 7:
    while True:  # Event Loop
        event, values = window8.Read()
        if event in (None, 'Exit'):
            window8.close()
            break
        if event == data[34]:
            SE += 1
            window_teller += 1
            window8.close()

        elif event == data[35]:
            IAT += 1
            window_teller += 1
            window8.close()

        elif event == data[36]:
            BDAM += 1
            window_teller += 1
            window8.close()

        elif event == data[37]:
            FICT += 1
            window_teller += 1
            window8.close()

if window_teller == 8:
    while True:  # Event Loop
        event, values = window9.Read()
        if event in (None, 'Exit'):
            window9.close()
            break
        if event == data[39]:
            SE += 1
            FICT += 1
            window_teller += 1
            window9.close()

        elif event == data[40]:
            BDAM += 1
            IAT += 1
            window_teller += 1
            window9.close()

if window_teller == 9:
    while True:  # Event Loop
        event, values = window10.Read()
        if event in (None, 'Exit'):
            window10.close()
            break
        if event == data[42]:
            SE += 1
            FICT += 1
            window_teller += 1
            window10.close()

        elif event == data[43]:
            BDAM += 1
            IAT += 1
            window_teller += 1
            window10.close()

if window_teller == 10:
    while True:  # Event Loop
        event, values = window11.Read()
        if event in (None, 'Exit'):
            window11.close()
            break
        if event == data[45]:
            SE += 1
            window_teller += 1
            window11.close()

        elif event == data[46]:
            IAT += 1
            window_teller += 1
            window11.close()

        elif event == data[47]:
            BDAM += 1
            window_teller += 1
            window11.close()

        elif event == data[48]:
            FICT += 1
            window_teller += 1
            window11.close()

if window_teller == 11:
    while True:  # Event Loop
        event, values = window12.Read()
        if event in (None, 'Exit'):
            window12.close()
            break
        if event == data[50]:
            SE += 1
            window_teller += 1
            window12.close()

        elif event == data[51]:
            IAT += 1
            window_teller += 1
            window12.close()

        elif event == data[52]:
            BDAM += 1
            window_teller += 1
            window12.close()

        elif event == data[53]:
            FICT += 1
            window_teller += 1
            window12.close()

if window_teller == 12:
    while True:  # Event Loop
        event, values = window13.Read()
        if event in (None, 'Exit'):
            window13.close()
            break
        if event == data[55]:
            SE += 1
            window_teller += 1
            window13.close()

        elif event == data[56]:
            IAT += 1
            window_teller += 1
            window13.close()

        elif event == data[57]:
            BDAM += 1
            window_teller += 1
            window13.close()

        elif event == data[58]:
            FICT += 1
            window_teller += 1
            window13.close()

if window_teller == 13:
    while True:  # Event Loop
        event, values = window14.Read()
        if event in (None, 'Exit'):
            window14.close()
            break
        if event == data[60]:
            SE += 1
            window_teller += 1
            window14.close()

        elif event == data[61]:
            IAT += 1
            window_teller += 1
            window14.close()

        elif event == data[62]:
            BDAM += 1
            window_teller += 1
            window14.close()

        elif event == data[63]:
            FICT += 1
            window_teller += 1
            window14.close()

if window_teller == 14:
    while True:  # Event Loop
        event, values = window15.Read()
        if event in (None, 'Exit'):
            window15.close()
            break
        if event == data[65]:
            SE += 1
            window_teller += 1
            window15.close()

        elif event == data[66]:
            IAT += 1
            window_teller += 1
            window15.close()

        elif event == data[67]:
            BDAM += 1
            window_teller += 1
            window15.close()

        elif event == data[68]:
            FICT += 1
            window_teller += 1
            window15.close()


if max(SE, BDAM, IAT, FICT) == SE:
    uitslag = "Software Engineering"
    text_uitslag = se_uitslag

elif max(SE,BDAM,FICT,IAT) == BDAM:
    uitslag = "Business Data Management"
    text_uitslag = bdam_uitslag

elif max(SE,BDAM,FICT,IAT) == FICT:
    uitslag = "Forensisch ICT"
    text_uitslag = fict_uitslag

elif max(SE,BDAM,FICT,IAT) == IAT:
    uitslag = "Interactie-technologie"
    text_uitslag = iat_uitslag

layout_resultaat = [
    [sg.Image("MinervaMcGonagall_PM_B1C7M2_HarryPotterBeingSortedInGreatHall_Moment(2).png")],
    [sg.Text('Resultaat van de quiz')],
    [sg.Text(f"Je resultaat is : {uitslag}")],
    [sg.Text(text_uitslag)]]

window_resultaat = sg.Window('Window Title', layout_resultaat, size=(1152, 768))

if window_teller == 15:
    while True:  # Event Loop
        event, values = window_resultaat.Read()
        if event in (None, 'Exit'):
            window_resultaat.close()
            break

event, values = window1.read()
event, values = window2.read()
event, values = window3.read()
event, values = window4.read()
event, values = window5.read()
event, values = window6.read()
event, values = window7.read()
event, values = window8.read()
event, values = window9.read()
event, values = window10.read()
event, values = window11.read()
event, values = window12.read()
event, values = window13.read()
event, values = window14.read()
event, values = window15.read()
event, values = window_resultaat.read()


def print_resultaat():
    print(f'je score voor software engineering:  {SE}', f'je score voor bdam:   {BDAM}', f'je score voor fict: {FICT}',
          f'je score voor iat: {IAT}')


def schrijf_resultaat_naar_text(bestand):
    with open(bestand, 'w') as w:
        w.write(f"SE is: {SE}, BDAM is : {BDAM}, FICT is :{FICT}, IAT is :{IAT}")


schrijf_resultaat_naar_text('resultaat.txt')
