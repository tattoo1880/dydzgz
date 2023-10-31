import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoidHMuMS5iZDk2MWM2NjliY2YwOTc2MTk4MzYyYTQ0MWY0NmZkZGVlOGY0NDc3ODFlZmU1MThjOThhY2M0NzYyYmJmY2IzYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVFDSUFIN2FwZkpTR1hBWGxUVk1zUnN1TzlLUmJsVFgxRXdHNDZWd1MwcHZIZmpBaUJhSGFOVmNxK3FFSTA2ZzY0Q3NJcjRZcnpNdUxGWlhmMk9XTTkyZDVrUzBnPT0iLCJ0aW1lc3RhbXAiOjE2OTg2NDE4MTl9',
    'bd-ticket-guard-iteration-version': '1',
    'bd-ticket-guard-ree-public-key': 'BBhO17+A7UCAQf2pOvaS5EQrb5EUggxdqT4iDx9bghZM/crjQ3d6lNK6Gt7K/IZDSqTxOwnIyPdVKOaXn7Zpq4A=',
    'bd-ticket-guard-version': '2',
    'bd-ticket-guard-web-version': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'ttwid=1%7Cgs1GCVxYo-cdridYXzPx3bz_83aYmxPhuTGHnQxh8yI%7C1698636831%7C37790485536232ad6f033e06dd1c4b147b8960f75bb578b13b224649d6b63599; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; webcast_local_quality=null; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=1639a8e60dbd6e2c8ce960b465cbdaf8; passport_csrf_token_default=1639a8e60dbd6e2c8ce960b465cbdaf8; strategyABtestKey=%221698636852.862%22; ttcid=eccafbe7001f448cbade094b5b729c6844; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; s_v_web_id=verify_locciz7n_QrsuPFap_pQr7_4quo_8HXN_DxdH6QdePnpn; xgplayer_user_id=724080581528; passport_assist_user=Cj2c76zTzjTP4JIFOJdX0_1SN3tWa7pXm_IQquqcreZ8RZcVdkwBrXnyLHMoVTzH8U0g8mfNgVzX1vEASnCTGkoKPNEDX6ob-mpYAJRUU04l_gW5YDE8NIwTffYKw8miHdX-94ZMxjn0nEZt0LTDIFW0otyb0Pwrgw2VQu1fWRCH-L8NGImv1lQgASIBA2Hk52I%3D; n_mh=0nEoaTepFk6L9nK9QzgL9yXCByYvoGIqaH2-J7koh78; sso_uid_tt=2c55890388095c5415cd5697a3848397; sso_uid_tt_ss=2c55890388095c5415cd5697a3848397; toutiao_sso_user=bea1a1a0a5351330716a460bfec0af25; toutiao_sso_user_ss=bea1a1a0a5351330716a460bfec0af25; sid_ucp_sso_v1=1.0.0-KGI2NGE5OGFiYjRmZjM5ZWE2OWYyNjU4MjVhMzdlODM4YzNlODVhZDcKHQjagNaPnwMQo8n8qQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgYmVhMWExYTBhNTM1MTMzMDcxNmE0NjBiZmVjMGFmMjU; ssid_ucp_sso_v1=1.0.0-KGI2NGE5OGFiYjRmZjM5ZWE2OWYyNjU4MjVhMzdlODM4YzNlODVhZDcKHQjagNaPnwMQo8n8qQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgYmVhMWExYTBhNTM1MTMzMDcxNmE0NjBiZmVjMGFmMjU; passport_auth_status=e2bda1c994eca98b95401fcb7be07f1b%2C; passport_auth_status_ss=e2bda1c994eca98b95401fcb7be07f1b%2C; uid_tt=6717fa375f454c0c95c398a8449493d6; uid_tt_ss=6717fa375f454c0c95c398a8449493d6; sid_tt=a9b584a7d77247b2e89d018cba581820; sessionid=a9b584a7d77247b2e89d018cba581820; sessionid_ss=a9b584a7d77247b2e89d018cba581820; LOGIN_STATUS=1; store-region=us; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=867e0f2100f2700e59878746b03357fb; __security_server_data_status=1; publish_badge_show_info=%220%2C0%2C0%2C1698636977669%22; csrf_session_id=a7036e68b9896f706256827629100202; sid_guard=a9b584a7d77247b2e89d018cba581820%7C1698636978%7C5183987%7CFri%2C+29-Dec-2023+03%3A36%3A05+GMT; sid_ucp_v1=1.0.0-KDY2M2FmMjA5NmUxOWNkMTI2MDdmZjYwZTg4ZjNmNWNlN2QzOGNiZDgKGQjagNaPnwMQssn8qQYY7zEgDDgGQPQHSAQaAmxxIiBhOWI1ODRhN2Q3NzI0N2IyZTg5ZDAxOGNiYTU4MTgyMA; ssid_ucp_v1=1.0.0-KDY2M2FmMjA5NmUxOWNkMTI2MDdmZjYwZTg4ZjNmNWNlN2QzOGNiZDgKGQjagNaPnwMQssn8qQYY7zEgDDgGQPQHSAQaAmxxIiBhOWI1ODRhN2Q3NzI0N2IyZTg5ZDAxOGNiYTU4MTgyMA; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699242837577%2C%22type%22%3A1%7D; download_guide=%223%2F20231030%2F0%22; pwa2=%220%7C0%7C3%7C0%22; SEARCH_RESULT_LIST_TYPE=%22single%22; passport_fe_beating_status=true; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAjSJ-n-ezIE8OtTDsiCiRP6h0qbQ-IGJA7wngmmvh9xw%2F1698681600000%2F0%2F0%2F1698642043444%22; __ac_nonce=0653f34d700e03a441d; __ac_signature=_02B4Z6wo00f013gUyLQAAIDA7MKTuyGv6Wd4NOwAALtFLay7.uYRokQt5xkkevVit2.KtTr.4zYhG.EJ9vTS5YJXvDqyg4cR6dSa3ivsMacC6TCbX23nQBP6nn13zYqrAwV8p5fMeiC2qV522c; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1280%2C%5C%22screen_height%5C%22%3A800%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.25%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A300%7D%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQmhPMTcrQTdVQ0FRZjJwT3ZhUzVFUXJiNUVVZ2d4ZHFUNGlEeDliZ2haTS9jcmpRM2Q2bE5LNkd0N0svSVpEU3FUeE93bkl5UGRWS09hWG43WnBxNEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=3STfd2qs0.idcN-uH12knTfIhONgKkMUPmpu.7M61M45bwWFfacxIlpjMH1TuouK5b1a; msToken=FLJBAH938h-TYUIKycALBLnyvfmKNVEWGBPD6bsxfLZ82tSm8AUzowJHzW4JVMC7JbQmDZiWERFBPeb7beDmfiR_2s58WWhyLF0Xc1FOEmS2etve5CMPS1ENJAF99GM=; odin_tt=7f7fb73cc31cf879dea13f14818257411c7ab78b8d511b43759dc6239fd0c6c21cc9dabb6556a998261b9f1b295eaeab; msToken=NDYz_7tSbI7wWMy7-rF77WlotTxvRK-bBWye62reLs5t5kN8xgeWluE7xyoiLvwv7ANiDAqOfoNf0lw7bO3wdZxlFQ38TubzmFhJlcpuP0osc8na9_P_FimaWi8ve1GV',
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAh7MdVA-UbMYLeO3_zhA_Z-Mrkh8cDwBCU_qQqucnrFE',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-secsdk-csrf-token': '000100000001d049b1219f8e3b0afb1484b5701cd10e888a4f1eca645279dc141fbb7b52e71c1792c9b69f635554',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'pc_client_type': '1',
    'version_code': '170400',
    'version_name': '17.4.0',
    'cookie_enabled': 'true',
    'screen_width': '1280',
    'screen_height': '800',
    'browser_language': 'zh-CN',
    'browser_platform': 'MacIntel',
    'browser_name': 'Chrome',
    'browser_version': '118.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '118.0.0.0',
    'os_name': 'Mac OS',
    'os_version': '10.15.7',
    'cpu_core_num': '4',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '1.25',
    'effective_type': '3g',
    'round_trip_time': '300',
    'webid': '7295589591254976040',
    'msToken': 'NDYz_7tSbI7wWMy7-rF77WlotTxvRK-bBWye62reLs5t5kN8xgeWluE7xyoiLvwv7ANiDAqOfoNf0lw7bO3wdZxlFQ38TubzmFhJlcpuP0osc8na9_P_FimaWi8ve1GV',
    'X-Bogus': 'DFSzswRLmawzyPPFtYFrtp7TlqSX',
}

data = {
    'type': '1',
    'user_id': '85089670734',
}

response = requests.post('https://www.douyin.com/aweme/v1/web/commit/follow/user/', params=params, headers=headers, data=data)
print(response.text)