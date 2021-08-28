from webhook_bot.apis.github_apis import GithubApis

class IssuesOpened(object):
    def __init__(self, event, action, request):
        self.__event = event
        self.__action = action
        self.__request = request
        self.__url, self.__author = self.__parse_request()

    def execute(self):
        print(f'------------- Start -------------')
        print(f'Deal GitHub request with event: {self.__event}, action: {self.__action}')
        self.__greet_author()
        print(f'------------- Final -------------')

        return True

    def __greet_author(self):
        message = [
            f'> ***This is system automated generate message***\r\n\r\n',
            f'Thanks for the report @{self.__author}!\r\n',
            f'Owner will look back into it ASAP!\r\n',
            f'To contact codevience please email to codevience@gmail.com\r\n',
            f'Codevience.'
        ]

        payload = {
            'body': ''.join(message)
        }

        GithubApis(self.__url, payload).call()

    def __parse_request(self):
        url = self.__request.body()['issue']['comments_url']
        author = self.__request.body()['sender']['login']

        return url, author
