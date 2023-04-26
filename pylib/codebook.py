
import textract

"""Codebook and Unweighted Frequencies for the 2021 General Social Survey (GSS)
Replicating Core
Variable: HAPMAR

Type: Numeric

Label:
(IF CURRENTLY MARRIED, ASK HAPMAR)
Taking things all together,
how would you describe your marriage?
Would you say that your marriage is very happy,
pretty happy, or not too happy?
Notes: See HAPPY

LABEL

VALUE COUNT
"""

def get_codebook_text(pkg):
    fn = pkg.reference('gss_2021_codes').resolved_url.get_resource().get_target().fspath

    text = textract.process(fn).decode('latin1')

    return text.splitlines()
