import requests
from bs4 import BeautifulSoup


headers = {
    'authority': 'www.douyin.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__ac_referer=https://www.douyin.com/user/MS4wLjABAAAAh7MdVA-UbMYLeO3_zhA_Z-Mrkh8cDwBCU_qQqucnrFE?enter_from=general_search&enter_method=general_search&extra_params=%7B%22search_params%22%3A%7B%22search_result_id%22%3A%2285089670734%22%2C%22relation_tag%22%3A1%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202310301214567F10D2B5E7AE4801FECF%22%7D%2C%22search_type%22%3A%22general%22%2C%22impr_id%22%3A%22202310301214567F10D2B5E7AE4801FECF%22%2C%22search_id%22%3A%22202310301214567F10D2B5E7AE4801FECF%22%2C%22search_keyword%22%3A%22gloria%E9%82%93%E7%B4%AB%E6%A3%8B%22%2C%22token_type%22%3A%22discover_list%22%7D%7D; douyin.com; _waftokenid=eyJ2Ijp7ImEiOiJ5K3NEN2RyL2lRS2NyU2xPaENWR1d4SnlJa3JjQkNvYjcxZXlGMEJBeURrPSIsImIiOjE2OTg3MTY3NjIsImMiOiJxYk9Nb1J2UmR2WERjLzZVVjZPRlAxZEJDd2h4ZjkzTHNiNGJDWDR1MnVBPSJ9LCJzIjoiZTVGZjhLaENiZkFrSVRsQkUzT3RRSWI5bHR0ZHNkc1NTRnBaWHhDYlNEOD0ifQ; ttwid=1%7Cgs1GCVxYo-cdridYXzPx3bz_83aYmxPhuTGHnQxh8yI%7C1698636831%7C37790485536232ad6f033e06dd1c4b147b8960f75bb578b13b224649d6b63599; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; webcast_local_quality=null; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=1639a8e60dbd6e2c8ce960b465cbdaf8; passport_csrf_token_default=1639a8e60dbd6e2c8ce960b465cbdaf8; ttcid=eccafbe7001f448cbade094b5b729c6844; s_v_web_id=verify_locciz7n_QrsuPFap_pQr7_4quo_8HXN_DxdH6QdePnpn; xgplayer_user_id=724080581528; passport_assist_user=Cj2c76zTzjTP4JIFOJdX0_1SN3tWa7pXm_IQquqcreZ8RZcVdkwBrXnyLHMoVTzH8U0g8mfNgVzX1vEASnCTGkoKPNEDX6ob-mpYAJRUU04l_gW5YDE8NIwTffYKw8miHdX-94ZMxjn0nEZt0LTDIFW0otyb0Pwrgw2VQu1fWRCH-L8NGImv1lQgASIBA2Hk52I%3D; n_mh=0nEoaTepFk6L9nK9QzgL9yXCByYvoGIqaH2-J7koh78; sso_uid_tt=2c55890388095c5415cd5697a3848397; sso_uid_tt_ss=2c55890388095c5415cd5697a3848397; toutiao_sso_user=bea1a1a0a5351330716a460bfec0af25; toutiao_sso_user_ss=bea1a1a0a5351330716a460bfec0af25; sid_ucp_sso_v1=1.0.0-KGI2NGE5OGFiYjRmZjM5ZWE2OWYyNjU4MjVhMzdlODM4YzNlODVhZDcKHQjagNaPnwMQo8n8qQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgYmVhMWExYTBhNTM1MTMzMDcxNmE0NjBiZmVjMGFmMjU; ssid_ucp_sso_v1=1.0.0-KGI2NGE5OGFiYjRmZjM5ZWE2OWYyNjU4MjVhMzdlODM4YzNlODVhZDcKHQjagNaPnwMQo8n8qQYY7zEgDDCImZHjBTgGQPQHGgJsZiIgYmVhMWExYTBhNTM1MTMzMDcxNmE0NjBiZmVjMGFmMjU; passport_auth_status=e2bda1c994eca98b95401fcb7be07f1b%2C; passport_auth_status_ss=e2bda1c994eca98b95401fcb7be07f1b%2C; uid_tt=6717fa375f454c0c95c398a8449493d6; uid_tt_ss=6717fa375f454c0c95c398a8449493d6; sid_tt=a9b584a7d77247b2e89d018cba581820; sessionid=a9b584a7d77247b2e89d018cba581820; sessionid_ss=a9b584a7d77247b2e89d018cba581820; LOGIN_STATUS=1; store-region=us; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=867e0f2100f2700e59878746b03357fb; __security_server_data_status=1; publish_badge_show_info=%220%2C0%2C0%2C1698636977669%22; csrf_session_id=a7036e68b9896f706256827629100202; sid_guard=a9b584a7d77247b2e89d018cba581820%7C1698636978%7C5183987%7CFri%2C+29-Dec-2023+03%3A36%3A05+GMT; sid_ucp_v1=1.0.0-KDY2M2FmMjA5NmUxOWNkMTI2MDdmZjYwZTg4ZjNmNWNlN2QzOGNiZDgKGQjagNaPnwMQssn8qQYY7zEgDDgGQPQHSAQaAmxxIiBhOWI1ODRhN2Q3NzI0N2IyZTg5ZDAxOGNiYTU4MTgyMA; ssid_ucp_v1=1.0.0-KDY2M2FmMjA5NmUxOWNkMTI2MDdmZjYwZTg4ZjNmNWNlN2QzOGNiZDgKGQjagNaPnwMQssn8qQYY7zEgDDgGQPQHSAQaAmxxIiBhOWI1ODRhN2Q3NzI0N2IyZTg5ZDAxOGNiYTU4MTgyMA; download_guide=%223%2F20231030%2F0%22; pwa2=%220%7C0%7C3%7C0%22; SEARCH_RESULT_LIST_TYPE=%22single%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; __ac_nonce=06540596000cec99b5621; __ac_signature=_02B4Z6wo00f01Hvvm8gAAIDD7znAx8Z3zlx7z79AAHvDNIQxvPaFzTNJNlJXQQdJXiaYv88JCiiW75AgMR8.WPEdMzLMw1QdnsYSe43G1uxjfu60vdQopC-6Pt3rtHnaOm5Iuxh1yzfTH8FF6b; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1280%2C%5C%22screen_height%5C%22%3A800%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.45%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A300%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAjSJ-n-ezIE8OtTDsiCiRP6h0qbQ-IGJA7wngmmvh9xw%2F1698768000000%2F0%2F1698716003984%2F0%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699320804050%2C%22type%22%3A1%7D; strategyABtestKey=%221698716004.321%22; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%220%22; my_rd=2; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQmhPMTcrQTdVQ0FRZjJwT3ZhUzVFUXJiNUVVZ2d4ZHFUNGlEeDliZ2haTS9jcmpRM2Q2bE5LNkd0N0svSVpEU3FUeE93bkl5UGRWS09hWG43WnBxNEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=gNx9RFPiaQ08nzhiMe9yNf5qpKfwbEqCBwQ8WZQS7gqc6wNNrCvTVjn8Jc2QM4KkpTdeQDxlp8X3tx9gw351nBRub1-5c9nrLpFFFX5xK4DYLzRrX9KzN_dkkXvdyout; tt_scid=rfmGw7MkSdxgoA7elMjNgdn0PbeljOi7hpg8dVuRQissRm5PW0LALGTPiltW7ktMb672; odin_tt=1b867698e513a93b21e62691b514ebcc7c350b6651e7c5310bcd9823e09d6676b751666f717f976eae4c246ea7133b94dd48758325de765fd1e61bd0a0d6da6a; msToken=eMLj4T23E3YKfF85bwxoGwqWyEFsCPP2UnYnB0cRC3g51Z4CjlqVCmROdAVfXHXvbFJU1Q9Qn0b3fW9YclAwkLOagBDWx-_Er-D6t0mhl9gGyAQIr2XvvcXrGnCRg712; IsDouyinActive=false',
    'referer': 'https://www.douyin.com/user/self',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

response = requests.get('https://www.douyin.com/user/self', headers=headers)
print(response.text)
with open('a.html','w')as f:
    f.write(response.text)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# 提取所有id为RENDER_DATA的script标签
scripts = soup.find_all('script', {'id': 'RENDER_DATA'})
# 获取第一个script标签的内容
script = scripts[0].string
print(script)