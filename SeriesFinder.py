import requests

def findSeries(msg_split, message):
  item = requests.get("https://mlb21.theshow.com/apis/items.json?type=mlb_card&page=1") #first page of items
  stats = list(item.json()['items'][0].keys())[0] + "\n"
  for stat in list(item.json()['items'][0].keys()):
    stats += stat + "\n"
  total_pages = int(item.json()['total_pages']) #total item pages
  firstName = "" #first name on page

  if len(msg_split) < 3:
    return "Please enter a valid player name"

  pageNumber = total_pages // 2
  name = msg_split[1:]
  for i in range(len(name)):
    name[i] = name[i].lower()
  series = []
  found = 0
  while (pageNumber <= total_pages):
    page = requests.get("https://mlb21.theshow.com/apis/items.json?type=mlb_card&page=" + str(pageNumber))
    for i in range(len(page.json()['items'])):
      player_name = page.json()['items'][i]['name'].split()
      if (i == 0):
        firstName = page.json()['items'][i]['name'].split()
      for j in range(len(player_name)):
        player_name[j] = player_name[j].lower()
        if i == 0:
          firstName[j] = firstName[j].lower()
      if (len(name) == len(player_name)):
        cont = False
        for x in range(len(name)):
          if (name[x] != player_name[x]):
            cont = True
            if (found == 1):
              found = 2
            break
      if (not cont):
        found = 1
        series.extend([page.json()['items'][i]['series']])
      else:
        if (found == 2):
          seriesString = ""
          for x in range(len(series)):
            if (x == len(series) - 1):
              seriesString += series[x]
            else:
              seriesString += series[x] + ", "
          nameString = ""
          for word in name:
            nameString += word.capitalize() + " "
          return "There are " + str(len(series)) + " cards of " + nameString + "in MLB The Show 21 and their series are " + seriesString
    if (pageNumber == total_pages):
      break
    if (firstName[0] > name[0]):
      total_pages = pageNumber
      pageNumber = pageNumber // 2
      print("first" + str(pageNumber))
    else:
      if (pageNumber == total_pages - 1):
        pageNumber += 1
        continue
      pageNumber += (total_pages - pageNumber) // 2
      print("second" + str(pageNumber))
  return "Please enter a valid player in MLB The Show 21"
  