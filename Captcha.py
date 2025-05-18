import requests
from scrapy.selector import Selector
import time
import pdfkit

API_KEY = 'ee8c70227d204c6f47aeac9377508306'
SITE_KEY = "6Lc_msIhAAAAACn5hKGUSsj5wAVihLMZ60SqwBm0"
PAGE_URL = 'https://www.sdboardofdentistry.org/verify/'


def solve_captcha(api_key, site_key, url):
    print("[+] Submitting CAPTCHA to 2Captcha...")
    session = requests.Session()
    response = session.post("http://2captcha.com/in.php", data={
        "key": api_key,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": url,
        "json": 1
    })

    if response.status_code == 200 and response.json().get("status") == 1:
        captcha_id = response.json().get("request")
        print(f"[+] CAPTCHA submitted. ID: {captcha_id}")
        return get_captcha_solution(session, api_key, captcha_id)
    else:
        print("[-] Error submitting CAPTCHA:", response.text)
        return None


def get_captcha_solution(session, api_key, captcha_id, timeout=120):
    print("[*] Waiting for CAPTCHA to be solved...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = session.get("http://2captcha.com/res.php", params={
            "key": api_key,
            "action": "get",
            "id": captcha_id,
            "json": 1
        })

        if response.status_code == 200:
            result = response.json()
            if result.get("status") == 1:
                print("[+] CAPTCHA solved.")
                return result.get("request")
            elif result.get("request") == "CAPCHA_NOT_READY":
                time.sleep(5)
            else:
                print("[-] CAPTCHA Error:", result.get("request"))
                return None
        else:
            print("[-] Failed to fetch CAPTCHA result.")
            return None

    print("[-] CAPTCHA solving timed out.")
    return None


def main():
    token = solve_captcha(API_KEY, SITE_KEY, PAGE_URL)
    if not token:
        print("[-] CAPTCHA solving failed.")
        return

    print("[+] CAPTCHA Token Received.")

    # Data with token and license number
    form_data = {
        "g-recaptcha-response": token,
        "license_number": "DH 1260"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0"
    }

    # Send final request with license number
    response = requests.post(PAGE_URL, data=form_data, headers=headers)
    print("[*] Response Status Code:", response.status_code)

    sel = Selector(text=response.text)
    license_info = sel.xpath('.//*[@id="license_number"]/text()').get()

    if license_info:
        print("[+] License Info:", license_info.strip())
    else:
        print("[-] Could not find license information.")

    # Save HTML and generate PDF
    with open("license_info.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    try:
        pdfkit.from_file("license_info.html", "license_info.pdf")
        print("[+] PDF saved as license_info.pdf")
    except Exception as e:
        print("[-] PDF generation failed:", e)


if __name__ == "__main__":
    main()
