import json
import os
import requests

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
    #     """Метод загружает файлы по списку file_list на яндекс диск"""
    # открыть файл на БИНАР чтение, передать его в яндекс!
        with open(real_path, 'rb') as f:
            data_4upload = f.read()
            print('Полная строка для загрузки файла', common_path_upload + upload_postfix + '&url=' + url_upload, 'data=', data_4upload, 'headers=', headers_token)
        respond_upload2 = requests.put(url_upload, data=data_4upload)
        #print('Ответ сервера2 (загрузка файла): ', respond_upload2)
        print(respond_upload2.text)
        return print(f'Файл: "{loc_file}" - успешно загружен!')

if __name__ == '__main__':
    # uploader = YaUploader('c:\my_folder\file.txt')
    # result = uploader.upload()

    token = 'AgAAAAAy_UpkAADLW4DINWqLNUrUml_SsYrvX7U'  # получен копированием по ссылке на "Полигоне" https://yandex.ru/dev/disk/poligon/#!//v1/disk/resources/CreateResource

    headers_token = {'Authorization': f'OAuth {token}'}
    real_path = '/home/ubuntu-user/PycharmProjects/DZ-9-1-request-HTTP/4upload/presentation-1-9.pdf'
    print(r'Реальный полный путь к загружаемому файлу: ', real_path)
    loc_file = os.path.basename(real_path) #выдает ИМЯ файла
    print('Загружаемый файл: ', loc_file)
    uploader = YaUploader(loc_file)

    common_path_upload = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path='
    upload_postfix = '%2F' + loc_file
    #print('Путь для запроса ссылки ВВЕРХ: ', common_path_upload + upload_postfix)
    respond = requests.get(common_path_upload + upload_postfix, headers=headers_token)
    url_upload = json.loads(respond.content)['href']
    uploader.upload()


