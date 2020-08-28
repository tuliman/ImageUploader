import requests
import datetime
import imghdr


def get_images(url):
    data = requests.get(url)
    f = str(datetime.datetime.now().date()) + url[-6::].replace('/', str(datetime.datetime.now().second)) + '.jpg'

    if data.status_code == 200 and len(data.content) != 0:
        img_file = open('/TestTaskUploader/media/' + f, 'wb')
        img_file.write(data.content)
        img_file.close()
        if imghdr.what('/TestTaskUploader/media/' + f) is not None:

            return f
        else:
            return None
    else:
        return None

