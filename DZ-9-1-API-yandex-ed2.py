import os


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        headers_token = {'Authorization': f'OAuth {token}'}
        #print(os.path.basename)


    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '_main_':
    token = 'AgAAAAAy_UpkAADLW4DINWqLNUrUml_SsYrvX7U'  # получен копированием по ссылке на "Полигоне" https://yandex.ru/dev/disk/poligon/#!//v1/disk/resources/CreateResource
    # token = input("Введите токен: ")
    folder_path = '/home/ubuntu-user/PycharmProjects/DZ-9-1-request-HTTP/4upload/'
    print(folder_path)

    uploader = YaUploader(folder_path)
    result = uploader.upload()
    #print(result)
