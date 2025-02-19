from ....base_templates import BaseTemplates

class UMThesisConfig:
    """UM specific thesis configuration"""
    
    THESIS_FORMAT = {
        "template_files": {
            "thesis": "um_thesis.tex",
            "chapter": "um_chapter.tex"
        },
        "front_matter": {
            "title_page": {
                "template": r"""
                    \begin{titlepage}
                    % UM specific title page format
                    \end{titlepage}
                """
            }
        },
        "faculty_variations": {
            "engineering": {
                "packages": ["amsmath", "algorithm"],
                "chapter_style": "numbered"
            },
            "science": {
                "packages": ["chemfig", "mhchem"],
                "chapter_style": "numbered"
            }
        }
    } 