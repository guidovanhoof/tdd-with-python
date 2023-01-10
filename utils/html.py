import re


def remove_csfr(html_code):
    csfr_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
    return re.sub(csfr_regex, '', html_code)
