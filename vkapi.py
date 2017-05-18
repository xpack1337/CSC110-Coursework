import vk,os,time,math
from math import log
from urllib.request import urlretrieve


login = ''
password = ''
vk_id = '6035548'


session = vk.AuthSession(app_id=vk_id,user_login=login,user_password = password)
vkapi = vk.API(session)

url = '{}'.format('https://vk.com/album-54530371_212428070')

album_id = url.split('/')[-1].split('_')[1]
owner_id = url.split('/')[-1].split('_')[0].replace('album','')

photos_count = vkapi.photos.getAlbums(owner_id=owner_id,
                            album_ids = album_id)[0]['size']

counter,prog,breaked = 0,0,0
time_now = time.time()

if not os.path.exists('saved'):
    os.mkdir('saved')
photo_folder = './saved/album{}_{}'.format(owner_id,album_id)
if not os.path.exists('photo_folder'):
    os.mkdir(photo_folder)

for j in range(math.ceil(photos_count / 1000)): # Подсчитаем сколько раз нужно получать список фото, так как число получится не целое - округляем в большую сторону
    photos = vkapi.photos.get(owner_id=owner_id, album_id=album_id, count=1000, offset=j*1000) # Получаем список фото

    for photo in photos:
        counter += 1
        url = photo['src'] # Получаем адрес изображения
        print('Загружаю фото № {} из {}. Прогресс: {} %'.format(counter, photos_count, prog))
        prog = round(100/photos_count*counter,2)
        try:
            urlretrieve(url, photo_folder + "/" + os.path.split(url)[1]) # Загружаем и сохраняем файл
        except Exception:
            print('Произошла ошибка, файл пропущен.')
            breaked += 1
            continue
time_for_dw = time.time() - time_now
print("\nВ очереди было {} файлов. Из них удачно загружено {} файлов, {} не удалось загрузить. Затрачено времени: {} сек.". format(photos_count, photos_count-breaked, breaked, round(time_for_dw,1)))
