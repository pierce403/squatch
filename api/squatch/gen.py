import json

data={}

for i in range(1,15):
  data['id']=i
  data['name']="BSidesPDX Squatch #"+str(i)
  data['image']="https://squatch.fun/api/squatch/squatch"+str(i)+".png"
  f=open(str(i)+'.json','w')
  f.write(json.dumps(data))
