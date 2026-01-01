import requests

# 想要抓取的免费订阅链接（可以换成你找的其他源）
url = "https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml"

def fetch_nodes():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("clash.yaml", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("节点更新成功！")
        else:
            print(f"下载失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    fetch_nodes()
