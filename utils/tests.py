import unittest

from utils.html import remove_csfr


class HtmlUtilsTestCase(unittest.TestCase):
    def test_crsf_token_wordt_verwijderd(self):
        html_code = (
            '<input type="hidden" name="csrfmiddlewaretoken" '
            'value="ru90yepiTGwTWGp4Fmubk6HFX8ILl4WsuJT6dH3YtFkJTZlvg3ctpfb0JjL4wrRJ" >'
        )

        result = remove_csfr(html_code)

        self.assertEqual(result, '', 'csfr token present in html!')
        self.assertNotIn(html_code, result, 'html contains csfr token!')
