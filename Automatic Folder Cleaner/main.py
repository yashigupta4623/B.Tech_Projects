import os 
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir()
files.remove('main.py')

createIfNotExists('Images')
createIfNotExists('Docs')
createIfNotExists('Media')
createIfNotExists('Others')

#docs 
docsExtns = ['.txt','.docx','doc','.pdf']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExtns]
for doc in docs:
    os.replace(doc, f"Docs/{doc}")

#images
imgExtns = ['.png','.jpg','.jpeg'] 
#[0] is root part and [1] is extension part.
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExtns]
for image in images:
    os.replace(image, f"Images/{image}")

#media
mediaExtns = ['.mp3','.mp4','.flv']
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExtns]
for media in medias:
    os.replace(media, f"Media/{media}")

others = []
for file in files :
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExtns) and (ext not in imgExtns)  and (ext not in docsExtns) and os.path.isfile(file):
        others.append(file)
for other in others:
    os.replace(other, f"Others/{other}")
