import re

from pr_agent.tools.pr_code_suggestions import PRCodeSuggestions
from pr_agent.tools.pr_description import PRDescription
from pr_agent.tools.pr_questions import PRQuestions
from pr_agent.tools.pr_reviewer import PRReviewer


class PRAgent:
    def __init__(self):
        pass

    async def handle_request(self, pr_url, request) -> bool:
        if any(cmd in request for cmd in ["/review", "/review_pr"]):
            await PRReviewer(pr_url).review()
        elif any(cmd in request for cmd in ["/describe", "/describe_pr"]):
            await PRDescription(pr_url).describe()
        elif any(cmd in request for cmd in ["/improve", "/improve_code"]):
            await PRCodeSuggestions(pr_url).suggest()
        elif any(cmd in request for cmd in ["/ask", "/ask_question"]):
            pattern = r'(/ask|/ask_question)\s*(.*)'
            matches = re.findall(pattern, request, re.IGNORECASE)
            if matches:
                question = matches[0][1]
                await PRQuestions(pr_url, question).answer()
        else:
            return False

        return True
