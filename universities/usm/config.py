from ..base import BaseUniversity

class USMThesis(BaseUniversity):
    """USM Thesis Template"""
    
    THESIS_FORMAT = {
        "margins": {
            "all": "2.5cm"
        },
        "front_matter": {
            "title_page": {
                "template": r"""
                    \begin{titlepage}
                    \begin{center}
                    %(title)s\\
                    \vspace{2cm}
                    by\\
                    \vspace{1cm}
                    %(author)s\\
                    \vspace{2cm}
                    Thesis submitted in fulfillment\\
                    of the requirements for the degree of\\
                    %(degree)s\\
                    \vspace{2cm}
                    %(month)s %(year)s
                    \end{center}
                    \end{titlepage}
                """
            }
        }
    } 