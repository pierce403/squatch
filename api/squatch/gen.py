import json

data={}

for i in range(1,15):
  data['id']=i
  data['name']="Sqatch "+str(i)
  data['image']="https://art3mis.org/api/squatch"+str(i)+".png"
  f=open(str(i)+'.json','w')
  f.write(json.dumps(data))
