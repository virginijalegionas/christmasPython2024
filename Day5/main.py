def organizeShoes(shoes):
    organizedShoes = []
    pairs = {}
    for shoe in shoes:
        if not shoe["size"] in pairs.keys():
            pairs[shoe["size"]] = {"I":0, "R":0}          
        pairs[shoe["size"]][shoe["type"]] += 1
    for (size, legs) in pairs.items():
        for _ in range(min(legs["I"], legs["R"])):            
            organizedShoes.append(size)    
    return organizedShoes




shoes = [
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'R', "size": 42 },
  { "type": 'I', "size": 41 },
  { "type": 'I', "size": 42 }
]
print(f" available pairs of shoes are:{organizeShoes(shoes)}")

shoes2 = [
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'I', "size": 38 },
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 }
]
print(f" available pairs of shoes2 are:{organizeShoes(shoes2)}")

shoes3 = [
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 36 },
  { "type": 'R', "size": 42 },
  { "type": 'I', "size": 41 },
  { "type": 'I', "size": 43 }
]
print(f" available pairs of shoes3 are:{organizeShoes(shoes3)}")