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

# ----------------------------------------------------------------------------
# Example 3: SQL Query Builder
# ----------------------------------------------------------------------------

class SQLQuery:
    """The product - represents a SQL query"""
    def __init__(self):
        self.select_columns = []
        self.from_table = None
        self.joins = []
        self.where_conditions = []
        self.group_by_columns = []
        self.having_conditions = []
        self.order_by_columns = []
        self.limit_value = None
        self.offset_value = None
    
    def to_sql(self):
        """Convert the query object to SQL string"""
        if not self.from_table:
            raise ValueError("FROM clause is required")
        
        # Build SELECT clause
        columns = ", ".join(self.select_columns) if self.select_columns else "*"
        sql = f"SELECT {columns}"
        
        # Add FROM clause
        sql += f"\nFROM {self.from_table}"
        
        # Add JOINs
        for join in self.joins:
            sql += f"\n{join}"
        
        # Add WHERE clause
        if self.where_conditions:
            conditions = " AND ".join(self.where_conditions)
            sql += f"\nWHERE {conditions}"
        
        # Add GROUP BY
        if self.group_by_columns:
            columns = ", ".join(self.group_by_columns)
            sql += f"\nGROUP BY {columns}"
        
        # Add HAVING
        if self.having_conditions:
            conditions = " AND ".join(self.having_conditions)
            sql += f"\nHAVING {conditions}"
        
        # Add ORDER BY
        if self.order_by_columns:
            columns = ", ".join(self.order_by_columns)
            sql += f"\nORDER BY {columns}"
        
        # Add LIMIT and OFFSET
        if self.limit_value:
            sql += f"\nLIMIT {self.limit_value}"
        if self.offset_value:
            sql += f"\nOFFSET {self.offset_value}"
        
        return sql


class QueryBuilder:
    """Builder for SQL queries"""
    def __init__(self):
        self._query = SQLQuery()
    
    def select(self, *columns):
        """Add columns to SELECT clause"""
        self._query.select_columns.extend(columns)
        return self
    
    def from_table(self, table):
        """Set the FROM table"""
        self._query.from_table = table
        return self
    
    def join(self, table, on_condition, join_type="INNER"):
        """Add a JOIN clause"""
        join_clause = f"{join_type} JOIN {table} ON {on_condition}"
        self._query.joins.append(join_clause)
        return self
    
    def left_join(self, table, on_condition):
        """Convenience method for LEFT JOIN"""
        return self.join(table, on_condition, "LEFT")
    
    def where(self, condition):
        """Add a WHERE condition"""
        self._query.where_conditions.append(condition)
        return self
    
    def group_by(self, *columns):
        """Add GROUP BY columns"""
        self._query.group_by_columns.extend(columns)
        return self
    
    def having(self, condition):
        """Add a HAVING condition"""
        self._query.having_conditions.append(condition)
        return self
    
    def order_by(self, *columns):
        """Add ORDER BY columns"""
        self._query.order_by_columns.extend(columns)
        return self
    
    def limit(self, value):
        """Set LIMIT"""
        self._query.limit_value = value
        return self
    
    def offset(self, value):
        """Set OFFSET"""
        self._query.offset_value = value
        return self
    
    def build(self):
        """Return the constructed query"""
        return self._query

# ----------------------------------------------------------------------------
# Example 4: Builder with Validation
# ----------------------------------------------------------------------------

class HTTPRequestBuilderWithValidation:
    """Enhanced builder with validation"""
    VALID_METHODS = {"GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"}
    
    def __init__(self, url):
        if not url:
            raise ValueError("URL cannot be empty")
        if not url.startswith(("http://", "https://")):
            raise ValueError("URL must start with http:// or https://")
        
        self._request = HTTPRequest(url)
    
    def method(self, method):
        """Set HTTP method with validation"""
        method = method.upper()
        if method not in self.VALID_METHODS:
            raise ValueError(f"Invalid HTTP method: {method}")
        self._request.method = method
        return self
    
    def timeout(self, seconds):
        """Set timeout with validation"""
        if seconds <= 0:
            raise ValueError("Timeout must be positive")
        if seconds > 300:
            raise ValueError("Timeout cannot exceed 300 seconds")
        self._request.timeout = seconds
        return self
    
    def header(self, key, value):
        """Add header with validation"""
        if not key or not value:
            raise ValueError("Header key and value cannot be empty")
        self._request.headers[key] = value
        return self
    
    def body(self, body):
        """Set request body"""
        self._request.body = body
        return self
    
    def build(self):
        """Validate and return the request"""
        if self._request.method in {"POST", "PUT", "PATCH"} and not self._request.body:
            raise ValueError(f"{self._request.method} requests typically require a body")
        
        return self._request



# ----------------------------------------------------------------------------
# Example 5: Pythonic Builder Pattern
# ----------------------------------------------------------------------------

class EmailMessage:
    """Email message with builder pattern using kwargs"""
    def __init__(self, **kwargs):
        self.to = kwargs.get('to', [])
        self.cc = kwargs.get('cc', [])
        self.bcc = kwargs.get('bcc', [])
        self.subject = kwargs.get('subject', '')
        self.body = kwargs.get('body', '')
        self.attachments = kwargs.get('attachments', [])
        self.priority = kwargs.get('priority', 'normal')
    
    def send(self):
        """Simulate sending the email"""
        recipients = len(self.to) + len(self.cc) + len(self.bcc)
        attachments = f" with {len(self.attachments)} attachment(s)" if self.attachments else ""
        return f"Sending '{self.subject}' to {recipients} recipient(s){attachments}"


class EmailBuilder:
    """Pythonic email builder"""
    def __init__(self):
        self._params = {}
    
    def to(self, *addresses):
        """Add TO recipients"""
        self._params.setdefault('to', []).extend(addresses)
        return self
    
    def cc(self, *addresses):
        """Add CC recipients"""
        self._params.setdefault('cc', []).extend(addresses)
        return self
    
    def subject(self, subject):
        """Set email subject"""
        self._params['subject'] = subject
        return self
    
    def body(self, body):
        """Set email body"""
        self._params['body'] = body
        return self
    
    def attach(self, *files):
        """Attach files"""
        self._params.setdefault('attachments', []).extend(files)
        return self
    
    def priority(self, level):
        """Set priority (low, normal, high)"""
        if level not in ('low', 'normal', 'high'):
            raise ValueError("Priority must be low, normal, or high")
        self._params['priority'] = level
        return self
    
    def build(self):
        """Build the email message"""
        if not self._params.get('to'):
            raise ValueError("At least one recipient is required")
        if not self._params.get('subject'):
            raise ValueError("Subject is required")
        
        return EmailMessage(**self._params)
