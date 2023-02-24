from urllib.parse import urlencode, unquote, quote_plus
import requests
import json


serviceKey = "Za7CRA50UMNQz3oCW0FBl3fTCeJsF5avNAHWVIy8qdXCZ1YXy5oA%2Fel79lf%2FtIr4%2BeZbLszqfMyyirXVpNWceg%3D%3D"
# serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def api():
    status_url = f"https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey={serviceKey}&returnType=JSON&numOfRows=100&pageNo=1"
    validate_url = f"http://api.odcloud.kr/api/nts-businessman/v1/validate?serviceKey={serviceKey}&returnType=JSON&numOfRows=100&pageNo=1"
    # returnType = "json"
    # numOfRows = "100"
    # pageNo = "1"

    data_status = {
        "b_no": [
            "0000000000",
        ]
    }

    data_validate = {
        "businesses": [
            {
                "b_no": "0000000000",
                "start_dt": "20000101",
                "p_nm": "홍길동",
                "p_nm2": "홍길동",
                "b_nm": "(주)테스트",
                "corp_no": "0000000000000",
                "b_sector": "",
                "b_type": ""
            }
        ]
    }

    # res = requests.post(status_url, data=data_status)
    res = requests.post(validate_url, data=json.dumps(data_validate))

    return res
