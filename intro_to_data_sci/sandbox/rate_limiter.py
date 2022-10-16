import http
import gevent as gevent


class RateLimiter:
    def __init__(self, request_limit, limit_period):
        self.limit_period = limit_period
        self.request_limit = request_limit
        self.requesters = {}
        self.

    def check_rate_limit(self, ip):
        counter =  self.requesters.get(ip, None)
        if not counter:
            self.requesters[ip] = 1
            gevent.spawn(self.monitor_requests, ip)
            return False

        if counter>=self.request_limit:
            return True

        self._increment_counter(ip)
        return False

    def monitor_requests(self, ip):
        gevent.sleep(self.limit_period)
        del self.requesters[ip]

    def _increment_counter(self, ip):
        self.requesters[ip] = self.requesters[ip] +1


class Application:

    def do_something(self):
        return "done"


class EndPoint:

    def __init__(self):
        self.rateLimiter = RateLimiter(request_limit=100, limit_period=60)
        self.application = Application()

    def some_endpoint(self, request):
        if self.rateLimiter.check_rate_limit(request.ip):
            return http.HTTPStatus.TOO_MANY_REQUESTS
        response = self.application.do_something()
        return response


