import re


class InfoReader:
    def __init__(self, text: str):
        self.text = text if text else ""

    # ---------------------------------------------------------
    # EMAILS
    # ---------------------------------------------------------
    def getEmails(self):
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(pattern, self.text)
        return list(set(emails))  # unique list

    # ---------------------------------------------------------
    # PHONE NUMBERS
    # ---------------------------------------------------------
    def getPhoneNumbers(self):
        pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?){1}\d{3}[-.\s]?\d{4}\b"
        numbers = re.findall(pattern, self.text)
        return list(set(numbers))

    # ---------------------------------------------------------
    # SOCIAL MEDIA URLs
    # ---------------------------------------------------------
    def getSocials(self):
        social_pattern = r"https?://(?:www\.)?(facebook|twitter|instagram|linkedin|github|youtube)\.com/[^\s]+"
        socials = re.findall(social_pattern, self.text)
        return socials

    # ---------------------------------------------------------
    # OPTIONAL: SOCIAL INFO (SAFE DEFAULT)
    # ---------------------------------------------------------
    def getSocialsInfo(self):
        return []   # empty so it never crashes
