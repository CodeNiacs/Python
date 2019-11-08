import json
json_formaat =  '{ "naam":"Codeniacs", "leeftijd":3, "plaats":"Groningen"}'
zet_om_in_array = json.loads(json_formaat)
for onderdeel in zet_om_in_array:
  print(onderdeel + ": " + str(zet_om_in_array[onderdeel]))
naam = input('Wat is jouw naam?\n')
print('Hallo, %s.' %naam)
leeftijd = input('Hoe oud ben je?\n')
verschil = str(int(leeftijd) - int(zet_om_in_array["leeftijd"]))
print('Dat is %s jaar ouder dan ik!' %verschil)
plaats = input('Waar woon je?\n')
if str(plaats) == str(zet_om_in_array["plaats"]):
  print('Oh, daar woon ik ook')
else:
  print('Oh, daar woon ik niet')
