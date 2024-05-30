import requests


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'xgplayer_user_id=995754743782; live_use_vvc=%22false%22; SEARCH_RESULT_LIST_TYPE=%22single%22; ttwid=1%7C0ydWU0_nzbQ4nbWqrzZ629phgTnIDkCkiqgfk9dFBcU%7C1713870088%7C7971a5edf7e1de020d07fb5aa7f748cc9df4b20fb0619b8433fb80f9fa8a37d5; bd_ticket_guard_client_web_domain=2; passport_csrf_token=28939e4cf77c7b0fe61e5e55b374fb94; passport_csrf_token_default=28939e4cf77c7b0fe61e5e55b374fb94; douyin.com; s_v_web_id=verify_lwt6doeu_1mbgeZSA_3UWu_4YnV_AaVK_DXihSPNHk1ei; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; dy_swidth=1920; dy_sheight=1080; strategyABtestKey=%221717068716.579%22; csrf_session_id=944cde4aa4e7091fb7d65b71ad7f08f2; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; WallpaperGuide=%7B%22showTime%22%3A1717068719536%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A7%2C%22cursor2%22%3A0%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; odin_tt=f7818271cd3686f7cdb2224ce1fe41597d654a7f7854ab27c19bff9b88bc491b16b13a4ebef87d6dcce2bf71fb35ba2e32405bc6a7a2697a33ad0cdcf3a7d32e30eefca674161aaa7d4312d45f146c88; __live_version__=%221.1.2.670%22; webcast_local_quality=null; live_can_add_dy_2_desktop=%220%22; xg_device_score=7.611784116721971; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=0665880ef00a22bd18f6; __ac_signature=_02B4Z6wo00f01fU7paAAAIDA27xoiubt5s31G6EAABsYYmCaZzm0Ret1feoCF3qZ0vEnjtF.4L26cvNeBUYTmVKn3K9E06mR3YCgfgZ1TQ56yL4gNYSkuWiqzl0gLQUSXArYgrD2hhBi0iFn34; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQmZwbkNzS3BoT3FFMVR0UUJFdkhPc2hOeWNZZUd5Tm1VS0ZKeXIwaytVK2U1dm1kN0o1RzhIb3p4Ymd5NDMwTWxSUU0xUUg4eHZrUWI2ZWNlV0x5L289IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=oeW7AoEds0gUuyoNEsu8LF-xDy2dXbKzVOb2H7dZ9dF1X001i0eo8UoJoSje7xHTX5CJXfdBVlukdzMrRmlXi5_qZR1JEisSGlqQ9ZbsMP4Mnz_j4Q==; download_guide=%223%2F20240530%2F0%22; pwa2=%220%7C0%7C2%7C0%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAzczhd43T8_7201euis4MqUMhT_x-7208Gl3d_L8gK_8',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAzczhd43T8_7201euis4MqUMhT_x-7208Gl3d_L8gK_8',
    'max_cursor': '0',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '1',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1920',
    'screen_height': '1080',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Edge',
    'browser_version': '125.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '125.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '16',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '100',
    'webid': '7361015925317568040',
    'verifyFp': 'verify_lwt6doeu_1mbgeZSA_3UWu_4YnV_AaVK_DXihSPNHk1ei',
    'fp': 'verify_lwt6doeu_1mbgeZSA_3UWu_4YnV_AaVK_DXihSPNHk1ei',
    'msToken': 'DtolrgUnR7xbC6dacUkB-i_4U1kV4uWdU9irXrLKRfHPys7vD4YsizPnQIX7fvRr8gLB4DL9P02uRx5TADoMB6IMkU94694xqqrzdipBVTIekT33Gw==',
    'a_bogus': 'Qjmh/QhDDk2kkfyh569LfY3q6vF3Y8MB0trEMD2fFxvcmy39HMTF9exo1K0vcCbjLG/lIeYjy4hjTNaMx5/bA3vRHuDKUIcgmESkKl5Q5xSSs1Xce6UgrUkE-wsACFrQsv1lxOfkwwQeSY8gWnAJ5kIlO62-zo0/916=',
}

response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', params=params, headers=headers)

aweme_list = response.json()['aweme_list'] 

for aweme in aweme_list:
    name = aweme["desc"]
    auther = aweme["author"]["nickname"]
    url = aweme["video"]["play_addr"]["url_list"][0]
    video_request = requests.get(url)
    with open(f"{name}-{auther}.mp4","wb") as f:
        f.write(video_request.content)