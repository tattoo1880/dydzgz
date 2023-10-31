import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoidHMuMS5jMzIwMDMwMWI0NGNjMmRhMzA3NDhhODU3ZWMyYzUzMDc2MzdiZGU1MDdlYzA2NDA0N2IzOTY0ZjBhMjE0OWZkYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVFDSUFzYldHbWRyQkZmTmdCU3ArMDBqVHp4MWp3cFJvNkNVeWZXTHdETjhnejBBaUIzWVFtd0tEbGpuWlFXUC9EVzJCMnY4SHZGOTRUam53ajJJcFkxVmVCQjZ3PT0iLCJ0aW1lc3RhbXAiOjE2OTg3MjgzODR9',
    'bd-ticket-guard-iteration-version': '1',
    'bd-ticket-guard-ree-public-key': 'BFO50QZiuGVxHVL+bzBqMb4xjaoI2s+czqKlcL4YCWnTtpfjjzw06SRipArwDlDQkLNWOoE8d4alfL/liruJJ+Q=',
    'bd-ticket-guard-version': '2',
    'bd-ticket-guard-web-version': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'ttwid=1%7CXXNsoppCtIV6M6XCqlxShyFwoaC50ODvIWVFhUwgfkA%7C1698405262%7C8c6ca390756ab916e80e6d4c8307a846727866e05b09b0859a9596f9198df71a; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; webcast_local_quality=null; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; passport_csrf_token=9f2e8e9a3abf542dc823e1d5e1f1be4a; passport_csrf_token_default=9f2e8e9a3abf542dc823e1d5e1f1be4a; ttcid=ee5134633ad34f1292ba8053ac93e34423; s_v_web_id=verify_lo8inp0a_GeURcDDk_OXSt_4tA7_AgoX_Y5FmrE5JY93B; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699059843849%2C%22type%22%3A1%7D; n_mh=0nEoaTepFk6L9nK9QzgL9yXCByYvoGIqaH2-J7koh78; sso_uid_tt=53eef47d25d91c41c54c317ff6f07c42; sso_uid_tt_ss=53eef47d25d91c41c54c317ff6f07c42; toutiao_sso_user=52158f0a842b47ccec9baabd9d3b3860; toutiao_sso_user_ss=52158f0a842b47ccec9baabd9d3b3860; passport_auth_status=cab8e3787981b54eadc80d845eb12577%2C; passport_auth_status_ss=cab8e3787981b54eadc80d845eb12577%2C; uid_tt=07220920f67e196eedc5dcd67b350254; uid_tt_ss=07220920f67e196eedc5dcd67b350254; sid_tt=d60b1bafa7e5ea61e0074eb3bb020e8a; sessionid=d60b1bafa7e5ea61e0074eb3bb020e8a; sessionid_ss=d60b1bafa7e5ea61e0074eb3bb020e8a; odin_tt=46ad1ca19c53968ee36999dc291768f0996c654df6ce82a99637e2cc86b41176338a182f9bf0cef419042232611fde3a852b70c47654a3e40a5b311afeb9d8aa; passport_assist_user=Cj3I9pgwNxzqA1ZLvpQKoyNNHrMerUXdiF_1eQdhHhEfdjN6SiMSkIkuPRP3pkTaH014t_CtsKkIfD-gM2VgGkoKPAmI-B6SCE8ZJPje1w4MNmNQHQZcaWj0bMrNsD-8PGe3j_BOI2l22LxoVT1QuVOodXyhjmHaeRj6CTWtGBC45L8NGImv1lQgASIBA7P2F5k%3D; sid_ucp_sso_v1=1.0.0-KGExYzQwYTFjMDNlYWI2MjU2ZjM4YmM4NWY1YmY2NTc3YzM2ODQ3NDEKHQjagNaPnwMQ7uDzqQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgNTIxNThmMGE4NDJiNDdjY2VjOWJhYWJkOWQzYjM4NjA; ssid_ucp_sso_v1=1.0.0-KGExYzQwYTFjMDNlYWI2MjU2ZjM4YmM4NWY1YmY2NTc3YzM2ODQ3NDEKHQjagNaPnwMQ7uDzqQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgNTIxNThmMGE4NDJiNDdjY2VjOWJhYWJkOWQzYjM4NjA; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=631b962f609c1d756089a9a6ff81411d; publish_badge_show_info=%220%2C0%2C0%2C1698492529182%22; LOGIN_STATUS=1; __security_server_data_status=1; csrf_session_id=c9e054e5dee47c600c763a217c38d811; store-region=us; store-region-src=uid; sid_guard=d60b1bafa7e5ea61e0074eb3bb020e8a%7C1698492533%7C5183991%7CWed%2C+27-Dec-2023+11%3A28%3A44+GMT; sid_ucp_v1=1.0.0-KDdiOTc3MWVhMzM4YjJjNDhmZGNiYzViZGM5MjljZmE5NWIyNmIzMDEKGQjagNaPnwMQ9eDzqQYY7zEgDDgGQPQHSAQaAmhsIiBkNjBiMWJhZmE3ZTVlYTYxZTAwNzRlYjNiYjAyMGU4YQ; ssid_ucp_v1=1.0.0-KDdiOTc3MWVhMzM4YjJjNDhmZGNiYzViZGM5MjljZmE5NWIyNmIzMDEKGQjagNaPnwMQ9eDzqQYY7zEgDDgGQPQHSAQaAmhsIiBkNjBiMWJhZmE3ZTVlYTYxZTAwNzRlYjNiYjAyMGU4YQ; download_guide=%223%2F20231029%2F0%22; pwa2=%220%7C0%7C3%7C0%22; passport_fe_beating_status=true; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAjSJ-n-ezIE8OtTDsiCiRP6h0qbQ-IGJA7wngmmvh9xw%2F1698595200000%2F0%2F1698555085519%2F0%22; strategyABtestKey=%221698726317.027%22; __ac_nonce=06540890e00cb580c4c1b; __ac_signature=_02B4Z6wo00f01mBqv1wAAIDB9LzkUktF2TpgSrvAAP1pNVfIILj.eAxkbFgVBzLdJB9W5nk1IMbb7wA4NDtEbUlSFEWpI6VL0SxaLlctz5VhcsVVbsSFcueEnEDaRwCBlM8xCKsOybpedCb.26; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1280%2C%5C%22screen_height%5C%22%3A800%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A0.7%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A800%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRk81MFFaaXVHVnhIVkwrYnpCcU1iNHhqYW9JMnMrY3pxS2xjTDRZQ1duVHRwZmpqencwNlNSaXBBcndEbERRa0xOV09vRThkNGFsZkwvbGlydUpKK1E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=n48c.QeYYg05FXQDNOqMXHViYniFpcMtumj3zk0BtZNge7NbsGjOWmh8DB4PeSjw011f; home_can_add_dy_2_desktop=%221%22; IsDouyinActive=true; msToken=koyFc_egsF2-P8v-iz1VMD-HPwsx_NMyFJ-NODydixiTLVL06TgmgPTyKrFBJi2W7DzScDwvseUhdxsDghytOWv5BFWry-6qjFllAEVaEArSTUy9I6N8TA==; msToken=oqHLUcBwuCEg62ls8IRUxnPtcdtwfNRYhppyqrSaSEJiaHsHGJnfFcxFBAyoUPzN5I01RWS341ZQ6JR6aadE6btxFGzTd7vsJD5DVhdK-ft2Ao1CJm2qhg==',
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/video/7258607067722747197',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-secsdk-csrf-token': '00010000000172498f8e1d4d8bb3c00917eb5c757f729062e59e79ea8e6dd2012432230b921c17931877633f47e9',
}

data = {
    'aweme_id': '7258607067722747197',
    'item_type': '0',
    'type': '1',
}

response = requests.post(
    'https://www.douyin.com/aweme/v1/web/commit/item/digg/?device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=118.0.0.0&browser_online=true&engine_name=Blink&engine_version=118.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=4&device_memory=8&platform=PC&downlink=0.75&effective_type=3g&round_trip_time=900&webid=7294595007625201179&msToken=oqHLUcBwuCEg62ls8IRUxnPtcdtwfNRYhppyqrSaSEJiaHsHGJnfFcxFBAyoUPzN5I01RWS341ZQ6JR6aadE6btxFGzTd7vsJD5DVhdK-ft2Ao1CJm2qhg==&X-Bogus=DFSzswVLKGkyBsuVtFvKA37TlqSG',
    headers=headers,
    data=data,
)


print(response.text)