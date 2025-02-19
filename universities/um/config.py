from ..base import BaseUniversity

class UMThesis(BaseUniversity):
    """UM Thesis Template"""
    
    THESIS_FORMAT = {
        "margins": {
            "top": "2.5cm",
            "others": "3.0cm"
        },
        "front_matter": {
            "title_page": {
                "template": r"""
                    \begin{titlepage}
                    \begin{center}
                    \MakeUppercase{%(title)s}\\
                    \vspace{2cm}
                    \MakeUppercase{%(author)s}\\
                    \vspace{2cm}
                    FACULTY OF %(faculty)s\\
                    UNIVERSITY OF MALAYA\\
                    KUALA LUMPUR\\
                    \vspace{2cm}
                    %(year)s
                    \end{center}
                    \end{titlepage}
                """
            }
        }
    } 