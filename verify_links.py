import re
import urllib.request
import urllib.error
import ssl

def check_url(url):
    try:
        # Create a context that ignores SSL certificate verification (useful for some dev environments)
        context = ssl._create_unverified_context()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=context) as response:
            return response.getcode() == 200, response.getcode()
    except urllib.error.HTTPError as e:
        return False, e.code
    except urllib.error.URLError as e:
        return False, str(e.reason)
    except Exception as e:
        return False, str(e)

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract img src
    img_urls = re.findall(r'<img[^>]+src="([^"]+)"', content)
    # Extract iframe src
    iframe_urls = re.findall(r'<iframe[^>]+src="([^"]+)"', content)

    all_urls = list(set(img_urls + iframe_urls))
    
    print(f"Found {len(all_urls)} unique URLs to check.")
    
    broken_links = []
    for url in sorted(all_urls):
        if url.startswith('http'):
            is_valid, status = check_url(url)
            if is_valid:
                print(f"[OK] {url}")
            else:
                print(f"[BROKEN] {url} - Error: {status}")
                broken_links.append((url, status))
        else:
            # Local file check
            import os
            if os.path.exists(url.split('?')[0]): # Strip query params if any
                print(f"[OK] {url} (Local file)")
            else:
                print(f"[BROKEN] {url} - Error: File not found")
                broken_links.append((url, "File not found"))

    if broken_links:
        print("\nSummary of Broken Links:")
        for url, error in broken_links:
            print(f"- {url}: {error}")
    else:
        print("\nNo broken links found!")

if __name__ == "__main__":
    main()
