import requests

cookies = {
    'x-bni-ja': '-666048174',
    'ASPSESSIONIDAEDBDQQA': 'LAIPPNDCBPDKDJADKPJEJENA',
    'BNIS_x-bni-jas': 'w0wBpGSbuQcQP0b/5YOzT4EY8iUPWoaa1lXbeny2ZkXMjp/vCGr6/QCrOLGK8WcS3B9lc7HilKZlp+8McanDrbEIzop3EUHmx8Of6BLi7bycPQrYxRgh3w==',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.sdboardofdentistry.org',
    'Referer': 'https://www.sdboardofdentistry.org/verify/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'x-bni-ja=-666048174; ASPSESSIONIDAEDBDQQA=LAIPPNDCBPDKDJADKPJEJENA; BNIS_x-bni-jas=w0wBpGSbuQcQP0b/5YOzT4EY8iUPWoaa1lXbeny2ZkXMjp/vCGr6/QCrOLGK8WcS3B9lc7HilKZlp+8McanDrbEIzop3EUHmx8Of6BLi7bycPQrYxRgh3w==',
}

data = {
    'action': 'submit',
    'first_name': '',
    'last_name': '',
    "g-recaptcha-response": token,
    'license_number': 'DH1260',
    'logicId': 'dentistSearch',
    'modId': 'members',
    'setHistory': 'no',
    '__ncforminfo': 'UAT1e3LYYWSTGKhPCd0udcIayLVUx_E8JdeMNqnK6YBBFjNkj87y3LZBMBLTD_-01V_ZZRvLEbvhXbaCLNlwm2QKWwFoPs73GQpqEIQMOPIa9AgcVMdSQC5jFJLJoQLO1LWf-Ua6EhZZYHC5fyfXMUfjGH9FEYlCfQaX9BzMtKXej1P2Xud3rDBar-8G8pS1_WvW2wGGBWoNjieC5G3HYc1mgYSnAYA680_M-ZPJKbiWrlYDKxGuheS4PdmiN5pjvr84AU6lYsOpyT1IWb0gaz5w7r35vLc5rrO_m0IzZ6myhqMwMDIr6GIwOfFyhYOIIEIm_kuGtxhaeTbNvCZ72TZ54ZpQcz6-q9SqL0VzV1s=',
}

response = requests.post('https://www.sdboardofdentistry.org/verify/', cookies=cookies, headers=headers, data=data)

import requests

cookies = {
    'x-bni-ja': '-666048174',
    'ASPSESSIONIDAEDBDQQA': 'LAIPPNDCBPDKDJADKPJEJENA',
    'BNIS_x-bni-jas': 'w0wBpGSbuQcQP0b/5YOzT4EY8iUPWoaa1lXbeny2ZkXMjp/vCGr6/QCrOLGK8WcS3B9lc7HilKZlp+8McanDrbEIzop3EUHmx8Of6BLi7bycPQrYxRgh3w==',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.sdboardofdentistry.org/verify/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'x-bni-ja=-666048174; ASPSESSIONIDAEDBDQQA=LAIPPNDCBPDKDJADKPJEJENA; BNIS_x-bni-jas=w0wBpGSbuQcQP0b/5YOzT4EY8iUPWoaa1lXbeny2ZkXMjp/vCGr6/QCrOLGK8WcS3B9lc7HilKZlp+8McanDrbEIzop3EUHmx8Of6BLi7bycPQrYxRgh3w==',
}

response = requests.get('https://www.sdboardofdentistry.org/verify/results/', cookies=cookies, headers=headers)