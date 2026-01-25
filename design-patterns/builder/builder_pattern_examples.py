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

# ----------------------------------------------------------------------------
# Example 2: Basic Builder Pattern
# ----------------------------------------------------------------------------

class HTTPRequest:
    """The product - what we're building"""
    def __init__(self, url):
        self.url = url
        self.method = "GET"
        self.headers = {}
        self.body = None
        self.timeout = 30
        self.auth = None
        self.verify_ssl = True
        self.allow_redirects = True
        self.max_redirects = 5
        self.cookies = {}
        self.proxies = {}
    
    def execute(self):
        """Simulate executing the request"""
        auth_str = f" (auth: {self.auth[0]})" if self.auth else ""
        return f"{self.method} {self.url}{auth_str} - timeout: {self.timeout}s"


class HTTPRequestBuilder:
    """The builder - constructs HTTPRequest step by step"""
    def __init__(self, url):
        self._request = HTTPRequest(url)
    
    def method(self, method):
        """Set HTTP method (GET, POST, etc.)"""
        self._request.method = method.upper()
        return self
    
    def header(self, key, value):
        """Add a header"""
        self._request.headers[key] = value
        return self
    
    def headers(self, headers_dict):
        """Add multiple headers at once"""
        self._request.headers.update(headers_dict)
        return self
    
    def body(self, body):
        """Set request body"""
        self._request.body = body
        return self
    
    def timeout(self, seconds):
        """Set timeout in seconds"""
        self._request.timeout = seconds
        return self
    
    def auth(self, username, password):
        """Set basic authentication"""
        self._request.auth = (username, password)
        return self
    
    def disable_ssl_verification(self):
        """Disable SSL certificate verification"""
        self._request.verify_ssl = False
        return self
    
    def disable_redirects(self):
        """Disable automatic redirects"""
        self._request.allow_redirects = False
        self._request.max_redirects = 0
        return self
    
    def build(self):
        """Return the constructed request"""
        return self._request



