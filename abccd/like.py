import requests

headers = {
    'authority': 'mcs.zijieapi.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

json_data = [
    {
        'events': [
            {
                'event': 'like',
                'params': '{"author_id":"85089670734","group_id":"7137966302055894306","log_pb":"\\"{\\\\\\"impr_id\\\\\\":\\\\\\"202310290959461CF075AE7DCAAFA04DBD\\\\\\"}\\"","enter_from":"main_page","previous_page":"","is_full_screen":"0","is_full_webscreen":"0","tab_name":"","click_method":"icon","from_follow_list":"0","relation":"1","clarity":"","aweme_type":"0","from_push":0,"item_duration_ms":39310,"is_modal_first_enter":"1","is_card_expand":"0","from_group_id":"7137966302055894306","music_id":"7137966334092004127","from_xigua":0,"insert_task_id":"0","enter_from_merge":"others_homepage","search_params":{"item_rank":1},"is_seen":"","is_update":0,"post_time":"2022年8月31日","is_from_skylight":0,"is_auto":1,"clarity_real":["normal_1080_0","normal_720_0","normal_540_0","lower_540_0"],"is_co_publish":0,"if_qianchuan_ad":0,"is_click_cover":0,"x_timestamp":1698544785103,"event_index":1698544840722}',
                'local_time_ms': 1698544785246,
                'is_bav': 0,
                'ab_sdk_version': '90108915,7166996,90097389,7133361,7360304,6958463,90108830,6586598,90109235,7195650,7395221,7324533,7323697,7296528,7406132,7438579,7102612,7212506,7374985,7022937,7321381,90094332,6912601,6461275,90094277,90107071,90107072,90108924,90108281,7149336,7198426,6071955,90107982,6528497,90108835,90097344,90097485,7312569,7273550,90109228,7160809,6882316',
                'session_id': '8e648aa8-8368-48e7-afba-fa67d2fd8cf3',
            },
        ],
        'user': {
            'user_unique_id': '7294595007625201179',
            'user_type': 12,
            'user_id': '111433580634',
            'user_is_auth': True,
            'user_is_login': True,
            'device_id': '7294595007625201179',
            'web_id': '7294595092375291401',
        },
        'header': {
            'app_id': 6383,
            'app_channel': '',
            'os_name': 'mac',
            'os_version': '10_15_7',
            'device_model': '',
            'language': 'zh-CN',
            'platform': 'web',
            'sdk_version': '5.0.52_1',
            'sdk_lib': 'js',
            'timezone': 8,
            'tz_offset': -28800,
            'resolution': '1280x800',
            'browser': 'Chrome',
            'browser_version': '118.0.0.0',
            'referrer': 'https://www.douyin.com/user/MS4wLjABAAAAh7MdVA-UbMYLeO3_zhA_Z-Mrkh8cDwBCU_qQqucnrFE?modal_id=7137966302055894306',
            'referrer_host': 'www.douyin.com',
            'width': 1280,
            'height': 800,
            'screen_width': 1280,
            'screen_height': 800,
            'tracer_data': '{"$utm_from_url":1}',
            'custom': '{"pathname":"/user/MS4wLjABAAAAh7MdVA-UbMYLeO3_zhA_Z-Mrkh8cDwBCU_qQqucnrFE","is_client":false,"client_version":"","first_install_time":1698405262,"douyin_pc_seo_page_id":"586084945848317857","in_piture_enable":true,"arch":"","tce_cluster":"default","browser_is_360":"0","scm_version":"1.0.3.9467","web_cpu_core":4,"web_memory_size":8,"session_init_time":1698544658349,"ms_token":"puP-BtkHMdYCHQlup6l7kAXqWgoCMKb3Md4vmmra7m2wyRgkhQpmNzoS79mC6dyAaBwiTcmrvNe8lEqfUy8HeLbfDiVTJvVkFexlxF6JWUtKFo1h29YmAg==","h265_hard_parse_supported":true,"web_wid":"","GUID":"","manufacturer":"","custom_js_heap_can_use":"1","custom_js_heap_limit_size":"2172649472","custom_js_heap_total_size":"63676841","custom_js_heap_used_size":"58084141","custom_js_event_counts":"36"}',
        },
        'local_time': 1698544785,
        'verbose': 1,
    },
]

response = requests.post('https://mcs.zijieapi.com/list', headers=headers, json=json_data)

print(response.text)