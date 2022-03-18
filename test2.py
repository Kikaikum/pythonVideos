import requests



url='https://mp4-c.udemycdn.com/2021-10-23_16-36-05-92ba1449cc92afeac760f68f8532483a/2/WebHD_720p.mp4?Expires=1647535117&Signature=KKqtMBdfl9oQYumTs8BnEe~C~W1uTu56v83h4emsVlEJe3~bRyzkR7BzsVW7jsBZpBNQ1eMLVv1AQWhLvdYXpsGlNnMcVRj9-3ovxks2u6kF1ThKryIDt1qm-G1l-PWXQ~Nm7RqBkeglwGkzwnj~D-bCsgjMdwqUYa-SVj8A~6k-Nm2w0-tR7JJ8wbJwTCrWf9Xe8RiAB1JRaNvyZY~w3I2VXahZKmbizdYYcwL8obK0wpzTgdMlu235~8i8lHmuUbo15guI44IBeOTl59PtBoXBp3L52OsC8i9i5d5d0B8bnuBAucXhPjo~OO~Kms4xnav6yP48PbyeJbYft2HJfg__&Key-Pair-Id=APKAITJV77WS5ZT7262A'
name='kike'
def downloadfile(name,url):
    name=name+".mp4"
    r=requests.get(url)
    
    f=open(name,'wb')
    
    for chunk in r.iter_content(chunk_size=255): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    
    f.close()

downloadfile(name,url)
