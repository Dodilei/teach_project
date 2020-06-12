import os


def add_cjk():

    tex_template = os.path.join(os.path.dirname(__file__), "assets", "cjk_latex.tex")

    with open(tex_template, "r") as infile:
        TEMPLATE_TEXT_FILE_BODY = infile.read()
        TEMPLATE_TEX_FILE_BODY = TEMPLATE_TEXT_FILE_BODY.replace(
            "YourTextHere",
            "\\begin{align*}\n" + "YourTextHere" + "\n\\end{align*}",
        )

        return TEMPLATE_TEXT_FILE_BODY
