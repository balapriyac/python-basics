# ----------------------------------------------------------------------------
# Example 1: The Problem - Complex Constructor
# ----------------------------------------------------------------------------

class HTTPRequestNaive:
    """Naive approach with many constructor parameters"""
    def __init__(self, url, method="GET", headers=None, body=None, 
                 timeout=30, auth=None, verify_ssl=True, allow_redirects=True,
                 max_redirects=5, cookies=None, proxies=None):
        self.url = url
        self.method = method
        self.headers = headers or {}
        self.body = body
        self.timeout = timeout
        self.auth = auth
        self.verify_ssl = verify_ssl
        self.allow_redirects = allow_redirects
        self.max_redirects = max_redirects
        self.cookies = cookies or {}
        self.proxies = proxies or {}

