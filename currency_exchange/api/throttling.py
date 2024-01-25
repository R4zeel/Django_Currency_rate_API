from rest_framework.throttling import AnonRateThrottle


class CustomThrottle(AnonRateThrottle):
    def parse_rate(self, rate):
        return (2, 10)
