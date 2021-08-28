import hmac


class GithubRequest(object):
    def __init__(self, request, secret=""):
        self.__raw_header = request.headers
        self.__raw_body = request.get_data()
        self.__header = self.__header_parser()
        self.__body = request.get_json()
        self.__secret = secret
        self.__verify = self.__verify_request()
        self.__event = self.__get_header_info('X-Github-Event')
        self.__action = self.__body['action']

    def __header_parser(self):
        result = dict()
        for key, value in self.__raw_header.items():
            result[key] = value
        return result

    def __get_header_info(self, key):
        if key in self.__header:
            return self.__header[key]
        else:
            return None

    def __verify_request(self):
        if 'X-Hub-Signature-256' in self.__header:
            signature_prefix = 'sha256='
            signature = self.__header['X-Hub-Signature-256']
            hmac_ = hmac.new(self.__secret.encode('UTF-8'), msg=self.__raw_body, digestmod="sha256")
            calc_signature = signature_prefix + hmac_.hexdigest()
            return hmac.compare_digest(signature, calc_signature)
        else:
            return True

    def header(self):
        return self.__header

    def body(self):
        return self.__body

    def event(self):
        return self.__event

    def action(self):
        return self.__action

    def verify(self):
        return self.__verify
