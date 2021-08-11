import requests

def findStat(msg_split, message):
  item = requests.get("https://mlb21.theshow.com/apis/items.json?type=mlb_card&page=1") #first page of items
  stats = list(item.json()['items'][0].keys())[0] + "\n"
  for stat in list(item.json()['items'][0].keys()):
    stats += stat + "\n"
  total_pages = int(item.json()['total_pages']) #total item pages
  firstName = "" #first name on page

  #check if message has valid length
  if (len(msg_split) < 5) : 
    if (len(msg_split) == 2 and msg_split[1] == 'stats_list'):
      return [stats]
    else:
      return ["Either player, stat, or both are missing. Format your message as \"!stat player_name series stat_name\"", "If you would like a list of stat names, please send \"!stat stats_list\""]

  else:
    #check if valid stat is inputted
    input_stat = msg_split[len(msg_split) - 1].lower()
    isStat = False
    for stat in list(item.json()['items'][0].keys()):
      if (input_stat == stat):
        isStat = True

    if (not isStat):
      return ["Invalid stat name. If you would like a list of stat names, please send \"!stat stats_list\""]

    #build list corresponding to name
    name = []
    for i in range(len(msg_split) - 3):
      name.append(msg_split[i + 1].lower())
    print(name)
    series = msg_split[len(msg_split) - 2].lower()
    print(series)
    
    #parse through pages to find if there is a card with same name
    pageNumber = int(total_pages / 2)

    #foundPlayers = [] #list of players found with the same name
    #found = 0 #integer representing whether player has been found yet, 0 means not found yet, 1 means found and still searching, 2 means found all players with same name
    #print(len(foundPlayers))

    while (not pageNumber <= 0 and not pageNumber > total_pages):
      print(pageNumber)
      page = requests.get("https://mlb21.theshow.com/apis/items.json?type=mlb_card&page=" + str(pageNumber))
      print(type(page.json()['items'][0]))
      for i in range(len(page.json()['items'])):
        player_name = page.json()['items'][i]['name'].split()
        if (i == 0):
          firstName = page.json()['items'][i]['name'].split()
        for j in range(len(player_name)):
          player_name[j] = player_name[j].lower()
          if (i == 0):
            firstName[j] = firstName[j].lower()
        print("Player name")
        print(player_name)
        #print("First name")
        #print(firstName)
        cont = True
        if (len(name) == len(player_name)):
          cont = False
          for x in range(len(name)):
            if (name[x] != player_name[x]):
              cont = True
              #if (found == 1):
              # found = 2
              break
        if (not cont) :
          print(page.json()['items'][i]['series'])
          if (series == page.json()['items'][i]['series'].lower()):
            statValue = page.json()['items'][i][input_stat]
            return [page.json()['items'][i]['name'] + "\'s " + input_stat + " is " + str(statValue)]
          else:
            cont = True

          #found = 1
          #foundPlayers.extend([page.json()['items'][i]])
          
        #elif (found == 2):
         # if (len(foundPlayers) == 1):
          #  statValue = page.json()['items'][i][input_stat]
        #  return [page.json()['items'][i]['name'] + "\'s " + input_stat + " is " + str(statValue)]
      
      #increases page number by 1 if still searching for players with same name
      #if (found == 1):
       # pageNumber += 1

      if (firstName[0] > name[0]):
        pageNumber -= 1
        print("first" + str(pageNumber))
      else:
        pageNumber += 1
        print("second" + str(pageNumber))
  return ["The card you searched for could not be found. Please enter the player's full name as it is displayed in MLB The Show 21 and the card's series"]