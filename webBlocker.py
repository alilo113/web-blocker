hosts_file_path = r'C:\Windows\System32\drivers\etc\hosts'

website_links = [
    "https://www.youtube.com/"
    "https://www.facebook.com/"
]

with open(hosts_file_path, "a") as file:
    for website in website_links:
        file.write(f"\n127.0.0.1 {website}\n")
        print("website has blocked")