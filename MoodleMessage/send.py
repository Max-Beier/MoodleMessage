import requests

def send_text(text, coversation_id, base_url, session_token) -> int:
    info = "core_message_send_messages_to_conversation"
    url = f'https://{base_url}/lib/ajax/service.php?sesskey={session_token}&info={info}'

    headers = {
        "authority": f"{base_url}",
        "method": "POST",
        "path": f"/lib/ajax/service.php?sesskey={session_token}&info={info}",
        "scheme": "https",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Length": "129",
        "Content-Type": "application/json",
        "Cookie": "",
        "Origin": f"https://{base_url}",
        "Referer": f"https://{base_url}/my/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    json = [{"index":0,"methodname":info,"args":{"conversationid":coversation_id,"messages":[{"text":text}]}}]

    r = requests.post(url=url, headers=headers, json=json, timeout=5000)

    print(r.status_code)
    print(r.text)

    return r.status_code
    
