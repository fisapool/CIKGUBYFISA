from ..base import BaseUniversity

class UTMThesis(BaseUniversity):
    """UTM Thesis Template"""
    
    THESIS_FORMAT = {
        "margins": {
            "top": "4cm",
            "bottom": "4cm",
            "left": "4cm",
            "right": "2.5cm"
        },
        "front_matter": {
            "title_page": {
                "template": r"""
                    \begin{titlepage}
                    \begin{center}
                    \MakeUppercase{%(title)s}\\
                    \vspace{1.5cm}
                    \MakeUppercase{%(author)s}\\
                    \vspace{1.5cm}
                    A thesis submitted in fulfillment of the\\
                    requirements for the award of the degree of\\
                    %(degree)s\\
                    \vspace{1.5cm}
                    %(faculty)s\\
                    Universiti Teknologi Malaysia\\
                    \vspace{1.5cm}
                    %(month)s %(year)s
                    \end{center}
                    \end{titlepage}
                """
            },
            "declaration": {
                "template": r"""
                    \chapter*{DECLARATION}
                    \addcontentsline{toc}{chapter}{DECLARATION}
                    
                    I declare that this thesis titled "%(title)s" is the result of my own research
                    except as cited in the references...
                """
            }
        }
    } 