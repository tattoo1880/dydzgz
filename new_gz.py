import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoidHMuMS5iZDk2MWM2NjliY2YwOTc2MTk4MzYyYTQ0MWY0NmZkZGVlOGY0NDc3ODFlZmU1MThjOThhY2M0NzYyYmJmY2IzYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVVDSVFDbDVFZFhvSkwzYnBnMkN6V3lMTjR4TG92MzFLejduaW1JbElWODV0Y0p5QUlnTG8vVmtDcnVCbmxhaVBlYTlzZFhiQ0l3MTdLTW9wTUlXZllVcWR2cmZ5UT0iLCJ0aW1lc3RhbXAiOjE2OTg2NDI4NTF9',
    'bd-ticket-guard-iteration-version': '1',
    'bd-ticket-guard-ree-public-key': 'BBhO17+A7UCAQf2pOvaS5EQrb5EUggxdqT4iDx9bghZM/crjQ3d6lNK6Gt7K/IZDSqTxOwnIyPdVKOaXn7Zpq4A=',
    'bd-ticket-guard-version': '2',
    'bd-ticket-guard-web-version': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'ttwid=1%7Cgs1GCVxYo-cdridYXzPx3bz_83aYmxPhuTGHnQxh8yI%7C1698636831%7C37790485536232ad6f033e06dd1c4b147b8960f75bb578b13b224649d6b63599; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; webcast_local_quality=null; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=1639a8e60dbd6e2c8ce960b465cbdaf8; passport_csrf_token_default=1639a8e60dbd6e2c8ce960b465cbdaf8; strategyABtestKey=%221698636852.862%22; ttcid=eccafbe7001f448cbade094b5b729c6844; s_v_web_id=verify_locciz7n_QrsuPFap_pQr7_4quo_8HXN_DxdH6QdePnpn; xgplayer_user_id=724080581528; passport_assist_user=Cj2c76zTzjTP4JIFOJdX0_1SN3tWa7pXm_IQquqcreZ8RZcVdkwBrXnyLHMoVTzH8U0g8mfNgVzX1vEASnCTGkoKPNEDX6ob-mpYAJRUU04l_gW5YDE8NIwTffYKw8miHdX-94ZMxjn0nEZt0LTDIFW0otyb0Pwrgw2VQu1fWRCH-L8NGImv1lQgASIBA2Hk52I%3D; n_mh=0nEoaTepFk6L9nK9QzgL9yXCByYvoGIqaH2-J7koh78; sso_uid_tt=2c55890388095c5415cd5697a3848397; sso_uid_tt_ss=2c55890388095c5415cd5697a3848397; toutiao_sso_user=bea1a1a0a5351330716a460bfec0af25; toutiao_sso_user_ss=bea1a1a0a5351330716a460bfec0af25; sid_ucp_sso_v1=1.0.0-KGI2NGE5OGFiYjRmZjM5ZWE2OWYyNjU4MjVhMzdlODM4YzNlODVhZDcKHQjagNaPnwMQo8n8qQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgYmVhMWExYTBhNTM1MTMzMDcxNmE0NjBiZmVjMGFmMjU; ssid_ucp_sso_v1=1.0.0-KGI2NGE5OGFiYjRmZjM5ZWE2OWYyNjU4MjVhMzdlODM4YzNlODVhZDcKHQjagNaPnwMQo8n8qQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgYmVhMWExYTBhNTM1MTMzMDcxNmE0NjBiZmVjMGFmMjU; passport_auth_status=e2bda1c994eca98b95401fcb7be07f1b%2C; passport_auth_status_ss=e2bda1c994eca98b95401fcb7be07f1b%2C; uid_tt=6717fa375f454c0c95c398a8449493d6; uid_tt_ss=6717fa375f454c0c95c398a8449493d6; sid_tt=a9b584a7d77247b2e89d018cba581820; sessionid=a9b584a7d77247b2e89d018cba581820; sessionid_ss=a9b584a7d77247b2e89d018cba581820; LOGIN_STATUS=1; store-region=us; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=867e0f2100f2700e59878746b03357fb; __security_server_data_status=1; publish_badge_show_info=%220%2C0%2C0%2C1698636977669%22; csrf_session_id=a7036e68b9896f706256827629100202; sid_guard=a9b584a7d77247b2e89d018cba581820%7C1698636978%7C5183987%7CFri%2C+29-Dec-2023+03%3A36%3A05+GMT; sid_ucp_v1=1.0.0-KDY2M2FmMjA5NmUxOWNkMTI2MDdmZjYwZTg4ZjNmNWNlN2QzOGNiZDgKGQjagNaPnwMQssn8qQYY7zEgDDgGQPQHSAQaAmxxIiBhOWI1ODRhN2Q3NzI0N2IyZTg5ZDAxOGNiYTU4MTgyMA; ssid_ucp_v1=1.0.0-KDY2M2FmMjA5NmUxOWNkMTI2MDdmZjYwZTg4ZjNmNWNlN2QzOGNiZDgKGQjagNaPnwMQssn8qQYY7zEgDDgGQPQHSAQaAmxxIiBhOWI1ODRhN2Q3NzI0N2IyZTg5ZDAxOGNiYTU4MTgyMA; download_guide=%223%2F20231030%2F0%22; pwa2=%220%7C0%7C3%7C0%22; SEARCH_RESULT_LIST_TYPE=%22single%22; __ac_nonce=0653f34d700e03a441d; __ac_signature=_02B4Z6wo00f013gUyLQAAIDA7MKTuyGv6Wd4NOwAALtFLay7.uYRokQt5xkkevVit2.KtTr.4zYhG.EJ9vTS5YJXvDqyg4cR6dSa3ivsMacC6TCbX23nQBP6nn13zYqrAwV8p5fMeiC2qV522c; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAjSJ-n-ezIE8OtTDsiCiRP6h0qbQ-IGJA7wngmmvh9xw%2F1698681600000%2F0%2F1698642467837%2F0%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699247509497%2C%22type%22%3A1%7D; passport_fe_beating_status=true; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1280%2C%5C%22screen_height%5C%22%3A800%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.45%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A650%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQmhPMTcrQTdVQ0FRZjJwT3ZhUzVFUXJiNUVVZ2d4ZHFUNGlEeDliZ2haTS9jcmpRM2Q2bE5LNkd0N0svSVpEU3FUeE93bkl5UGRWS09hWG43WnBxNEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=lu3fADnJqXcwgnadI28q_4QgEMpj7P7ZzCjUgRZXCq45b6PFkqOlHZdIcuJ9RCvixLXdEwwDZft7KLgsDc3PL9_OFLCEnYpVQLraweXJqj1YTOgxQPzkeHotfMKs9Kk=; msToken=rHK0I83B2QTFl0f7_-hPbfkwOYMyFp9mi_6SiW5sk8-_-ihkBuhUHFct_NpBmb3esPzQ9iIlstHVRRvoLeUTXVanTrVq3-jOG82tUo_xW4CYGcolxgaNBz_-RO-sI2Y=; odin_tt=a722a9737a969b3e32e3e824a78c05f277bafdc3fb39529fe6c454805ad920ff377a94d771daf57e207c44a77631118bf21a77d7d4152a712a97e0dedcc12ab0; tt_scid=BZNKeVA671U8Ce09qtcbZtKc9f.esw9iJdmeWKoy2Hcsi.1c7C2TDFMnlZFOA803f8fb; IsDouyinActive=true',
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAh7MdVA-UbMYLeO3_zhA_Z-Mrkh8cDwBCU_qQqucnrFE',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-secsdk-csrf-token': '000100000001d0163aca7d2ae14fb30f5143164a8cb13580223f22f694a6d65407ff9c6235361792caaca5b81f83',
}

data = {
    'type': '1',
    'user_id': '85089670734',
}

response = requests.post(
    'https://www.douyin.com/aweme/v1/web/commit/follow/user/?device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=118.0.0.0&browser_online=true&engine_name=Blink&engine_version=118.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=4&device_memory=8&platform=PC&downlink=1.45&effective_type=3g&round_trip_time=650&webid=7295589591254976040&msToken=rHK0I83B2QTFl0f7_-hPbfkwOYMyFp9mi_6SiW5sk8-_-ihkBuhUHFct_NpBmb3esPzQ9iIlstHVRRvoLeUTXVanTrVq3-jOG82tUo_xW4CYGcolxgaNBz_-RO-sI2Y=&X-Bogus=DFSzswRLpmAzyPPFtYFerp7TlqeZ',
    headers=headers,
    data=data,
)

print(response.text)