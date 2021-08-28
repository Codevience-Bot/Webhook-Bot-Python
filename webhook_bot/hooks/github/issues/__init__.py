from .issues_opened import IssuesOpened

GITHUB_EVENT_ISSUES = {
    'opened': [IssuesOpened, True]
}
