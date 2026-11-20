import base64,json,os,shutil
s=open('src.html').read()
names=[f[:-5] for f in os.listdir('img')]
uri={n:'data:image/webp;base64,'+base64.b64encode(open(f'img/{n}.webp','rb').read()).decode() for n in names}
single=s.replace('__IMGS__',json.dumps(uri)).replace('__IMG_logo__',uri['logo'])
open('fodmbcs-redesign.html','w').write(single)
d='deploy';shutil.rmtree(d,ignore_errors=True);os.makedirs(d+'/img')
for n in names:shutil.copy(f'img/{n}.webp',d+'/img/')
open(d+'/index.html','w').write(s.replace('__IMGS__',json.dumps({n:f'img/{n}.webp' for n in names})).replace('__IMG_logo__','img/logo.webp'))
json.dump({"cleanUrls":True},open(d+'/vercel.json','w'))
print(os.path.getsize('fodmbcs-redesign.html')//1024,'KB')
