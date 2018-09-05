# -*- coding: utf-8 -*-

# Scrapy settings for JDSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JDSpider'

SPIDER_MODULES = ['JDSpider.spiders']
NEWSPIDER_MODULE = 'JDSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JDSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'JDSpider.middlewares.JdspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'JDSpider.middlewares.JdspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'JDSpider.pipelines.JdspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DOWNLOADER_MIDDLEWARES = {
    # 'JDSpider.middlewares.JdspiderDownloaderMiddleware': 543,
    'JDSpider.middlewares.RandomUserAgent': 1,
    'JDSpider.middlewares.ProxyMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543
}
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
# 这里使用的代理IP，因为IP的存活期的限制，请定期更新下面的IP，可从http://www.xicidaili.com/ 中找免费的代理IP
PROXYS = [
    {'ip_port': '120.78.185.175:8118', 'user_pass': None},
    {'ip_port': '37.59.203.132:1080', 'user_pass': None},
    {'ip_port': '117.78.50.121:8118', 'user_pass': None},
    {'ip_port': '221.219.147.182:3128', 'user_pass': None},
    {'ip_port': '195.178.207.241:80', 'user_pass': None},
    {'ip_port': '39.137.69.7:8080', 'user_pass': None},
    {'ip_port': '118.190.95.35:9001', 'user_pass': None},
    {'ip_port': '120.78.215.151:808', 'user_pass': None},
    {'ip_port': '142.93.253.39:80', 'user_pass': None},
    {'ip_port': '78.153.4.122:9001', 'user_pass': None},
    {'ip_port': '118.190.95.43:9001', 'user_pass': None},
    {'ip_port': '109.188.81.101:8080', 'user_pass': None},
    {'ip_port': '106.12.32.43:3128', 'user_pass': None},
    {'ip_port': '180.76.111.69:3128', 'user_pass': None},
    {'ip_port': '103.242.219.242:8080', 'user_pass': None},
    {'ip_port': '116.0.54.30:8080', 'user_pass': None},
    {'ip_port': '182.61.59.147:9999', 'user_pass': None},
    {'ip_port': '98.190.250.150:48678', 'user_pass': None},
    {'ip_port': '190.96.91.243:8080', 'user_pass': None},
    {'ip_port': '219.141.153.3:80', 'user_pass': None},
    {'ip_port': '218.207.212.86:80', 'user_pass': None},
    {'ip_port': '39.137.77.66:80', 'user_pass': None},
    {'ip_port': '219.141.153.43:80', 'user_pass': None},
    {'ip_port': '176.53.2.122:8080', 'user_pass': None},
    {'ip_port': '49.51.70.42:1080', 'user_pass': None},
    {'ip_port': '111.231.87.160:8088', 'user_pass': None},
    {'ip_port': '101.4.136.34:81', 'user_pass': None},
    {'ip_port': '59.108.125.241:8080', 'user_pass': None},
    {'ip_port': '39.137.69.7:80', 'user_pass': None},
    {'ip_port': '118.190.200.139:8080', 'user_pass': None},
    {'ip_port': '39.137.69.10:8080', 'user_pass': None},
    {'ip_port': '37.59.248.186:1080', 'user_pass': None},
    {'ip_port': '178.128.104.174:8080', 'user_pass': None},
    {'ip_port': '39.135.24.12:8080', 'user_pass': None},
    {'ip_port': '191.252.185.161:8090', 'user_pass': None},
    {'ip_port': '120.78.59.193:8080', 'user_pass': None},
    {'ip_port': '138.122.171.190:53281', 'user_pass': None},
    {'ip_port': '178.49.139.13:80', 'user_pass': None},
    {'ip_port': '61.135.18.206:8888', 'user_pass': None},
    {'ip_port': '190.128.203.214:3128', 'user_pass': None},
    {'ip_port': '180.210.206.53:3129', 'user_pass': None},
    {'ip_port': '111.205.6.206:8088', 'user_pass': None},
    {'ip_port': '118.31.220.3:8888', 'user_pass': None},
    {'ip_port': '39.137.77.66:8080', 'user_pass': None},
    {'ip_port': '119.28.118.116:1080', 'user_pass': None},
    {'ip_port': '49.51.193.134:1080', 'user_pass': None},
    {'ip_port': '39.137.69.10:80', 'user_pass': None},
    {'ip_port': '124.206.133.219:3128', 'user_pass': None},
    {'ip_port': '49.51.195.24:1080', 'user_pass': None},
    {'ip_port': '49.51.193.128:1080', 'user_pass': None},
    {'ip_port': '49.51.68.122:1080', 'user_pass': None},
    {'ip_port': '118.190.94.254:9001', 'user_pass': None},
    {'ip_port': '118.144.149.206:3128', 'user_pass': None},
    {'ip_port': '176.15.225.193:53281', 'user_pass': None},
    {'ip_port': '200.229.208.154:53281', 'user_pass': None},
    {'ip_port': '125.39.9.34:9000', 'user_pass': None},
    {'ip_port': '101.227.5.36:9000', 'user_pass': None},
    {'ip_port': '117.131.235.198:8060', 'user_pass': None},
    {'ip_port': '58.247.46.123:8088', 'user_pass': None},
    {'ip_port': '125.39.9.35:9000', 'user_pass': None},
    {'ip_port': '140.207.95.94:8060', 'user_pass': None},
    {'ip_port': '49.51.228.166:1080', 'user_pass': None},
    {'ip_port': '125.62.26.197:3128', 'user_pass': None},
    {'ip_port': '60.8.42.137:8908', 'user_pass': None},
    {'ip_port': '60.8.42.132:8908', 'user_pass': None},
    {'ip_port': '60.8.42.36:8908', 'user_pass': None},
    {'ip_port': '221.193.177.45:8060', 'user_pass': None},
    {'ip_port': '221.193.222.7:8060', 'user_pass': None},
    {'ip_port': '118.25.220.214:3128', 'user_pass': None},
    {'ip_port': '106.113.242.167:9999', 'user_pass': None},
    {'ip_port': '59.48.237.6:8060', 'user_pass': None},
    {'ip_port': '222.33.192.238:8118', 'user_pass': None},
    {'ip_port': '218.60.8.98:3129', 'user_pass': None},
    {'ip_port': '218.60.8.83:3129', 'user_pass': None},
    {'ip_port': '218.60.8.99:3129', 'user_pass': None},
    {'ip_port': '120.131.9.254:1080', 'user_pass': None},
    {'ip_port': '218.26.227.108:80', 'user_pass': None},
    {'ip_port': '1.63.153.153:80', 'user_pass': None},
    {'ip_port': '223.68.190.130:8181', 'user_pass': None},
    {'ip_port': '112.24.107.108:8908', 'user_pass': None},
    {'ip_port': '112.27.129.54:3128', 'user_pass': None},
    {'ip_port': '112.24.107.102:8908', 'user_pass': None},
    {'ip_port': '223.93.172.248:3128', 'user_pass': None},
    {'ip_port': '183.129.207.74:12580', 'user_pass': None},
    {'ip_port': '183.129.207.73:16644', 'user_pass': None},
    {'ip_port': '121.40.138.161:8000', 'user_pass': None},
    {'ip_port': '223.93.145.186:8060', 'user_pass': None},
    {'ip_port': '112.16.28.103:8060', 'user_pass': None},
    {'ip_port': '111.3.122.245:8060', 'user_pass': None},
    {'ip_port': '111.3.154.196:8060', 'user_pass': None},
    {'ip_port': '183.129.207.74:11493', 'user_pass': None},
    {'ip_port': '183.129.207.73:14051', 'user_pass': None},
    {'ip_port': '183.129.207.73:13016', 'user_pass': None},
    {'ip_port': '183.129.207.74:13846', 'user_pass': None},
    {'ip_port': '183.129.207.74:18186', 'user_pass': None},
    {'ip_port': '36.33.25.31:808', 'user_pass': None},
    {'ip_port': '125.77.25.123:80', 'user_pass': None},
    {'ip_port': '27.154.240.222:8060', 'user_pass': None},
    {'ip_port': '119.27.172.241:80', 'user_pass': None},
    {'ip_port': '117.28.97.70:808', 'user_pass': None},
    {'ip_port': '117.127.0.210:80', 'user_pass': None},
    {'ip_port': '117.127.0.205:8080', 'user_pass': None},
    {'ip_port': '117.127.0.197:80', 'user_pass': None},
    {'ip_port': '117.127.0.201:8080', 'user_pass': None},
    {'ip_port': '117.127.0.195:8080', 'user_pass': None},
    {'ip_port': '117.127.0.198:80', 'user_pass': None},
    {'ip_port': '117.127.0.196:80', 'user_pass': None},
    {'ip_port': '118.212.95.34:53281', 'user_pass': None},
    {'ip_port': '117.127.0.209:80', 'user_pass': None},
    {'ip_port': '117.127.0.210:8080', 'user_pass': None},
    {'ip_port': '117.127.0.209:8080', 'user_pass': None},
    {'ip_port': '117.127.0.205:80', 'user_pass': None},
    {'ip_port': '117.127.0.197:8080', 'user_pass': None},
    {'ip_port': '117.127.0.201:80', 'user_pass': None},
    {'ip_port': '117.127.0.203:8080', 'user_pass': None},
    {'ip_port': '117.127.0.195:80', 'user_pass': None},
    {'ip_port': '221.215.182.95:8060', 'user_pass': None},
    {'ip_port': '124.128.76.142:8060', 'user_pass': None},
    {'ip_port': '221.2.175.238:8060', 'user_pass': None},
    {'ip_port': '221.2.174.99:8060', 'user_pass': None},
    {'ip_port': '106.75.9.39:8080', 'user_pass': None},
    {'ip_port': '221.2.174.3:8060', 'user_pass': None},
    {'ip_port': '119.179.134.153:8060', 'user_pass': None},
    {'ip_port': '218.198.80.8:80', 'user_pass': None},
    {'ip_port': '42.236.123.17:80', 'user_pass': None},
    {'ip_port': '222.88.147.121:8060', 'user_pass': None},
    {'ip_port': '221.14.140.66:80', 'user_pass': None},
    {'ip_port': '171.10.31.67:8080', 'user_pass': None},
    {'ip_port': '219.150.189.212:9999', 'user_pass': None},
    {'ip_port': '115.159.31.195:8080', 'user_pass': None},
    {'ip_port': '119.36.161.37:80', 'user_pass': None},
    {'ip_port': '119.36.161.38:80', 'user_pass': None},
    {'ip_port': '175.9.177.63:8060', 'user_pass': None},
    {'ip_port': '113.105.98.110:3128', 'user_pass': None},
    {'ip_port': '120.198.67.93:63000', 'user_pass': None},
    {'ip_port': '183.62.196.10:3128', 'user_pass': None},
    {'ip_port': '120.198.118.116:63000', 'user_pass': None},
    {'ip_port': '183.2.212.2:3128', 'user_pass': None},
    {'ip_port': '119.28.179.87:8080', 'user_pass': None},
    {'ip_port': '121.8.98.196:80', 'user_pass': None},
    {'ip_port': '36.36.115.170:8197', 'user_pass': None},
]

MYSQL_HOST = "localhost"
MYSQL_DBNAME = "test"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_PORT = "3306"