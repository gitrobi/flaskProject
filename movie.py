import requests

# 爱奇艺,QQ视频,bilibili 解析
url1 = 'https://api.lhh.la/vip/?url='
url2 = 'https://www.cuan.la/m3u8.php?url='


def _vip_play_url(url):
    return url1 + url


def _short_desc(desc):
    return desc if len(desc) <= 130 else desc[0:130]


def _get_request(url):
    res = requests.get(url)
    return res


def _post_request(url):
    res = requests.post(url)
    return res


class iqiyi:

    """
    [
    {'name':'姜子牙', 'image_url': 'xxx', 'play_url': 'xxx', 'description': 'xxx' }
    ]
    """
    @staticmethod
    def get_latest_list():
        latest_list = []
        url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=1&data_type=1&mode=11&page_id=1&ret_num=48'
        res = _get_request(url)
        res_json = res.json()
        data = res_json.get('data', None)
        list = data.get('list', None)
        # print(list)
        for one in list:
            name = one.get('name')
            image_url = one.get('imageUrl')
            desc = _short_desc(one.get('description'))
            play_url = _vip_play_url(one.get('playUrl'))
            latest_list.append({'name':name, 'image_url': image_url, 'play_url': play_url, 'desc': desc})
        # print(latest_list)
        return latest_list




class qq:
    pass


class bili:
    pass


if __name__ == '__main__':
    iqiyi.get_latest_list()
