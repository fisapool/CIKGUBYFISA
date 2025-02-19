class BaseTemplates:
    """Base templates for all universities"""
    
    THESIS_STRUCTURE = {
        "research": {
            "front_matter": [
                "title_page",
                "original_literary_work_declaration",
                "abstract",
                "acknowledgements",
                "table_of_contents",
                "list_of_figures",
                "list_of_tables",
                "list_of_symbols",
                "list_of_abbreviations"
            ],
            "main_chapters": [
                "introduction",
                "literature_review",
                "methodology",
                "results_and_discussion",
                "conclusion"
            ],
            "back_matter": [
                "references",
                "list_of_publications",
                "appendices"
            ]
        },
        "comprehensive": {
            "front_matter": [
                "title_page",
                "declaration",
                "abstract",
                "acknowledgements",
                "table_of_contents",
                "list_of_figures",
                "list_of_tables"
            ],
            "main_chapters": [
                "introduction",
                "literature_review",
                "methodology",
                "results",
                "conclusion"
            ],
            "back_matter": [
                "references",
                "appendices"
            ]
        },
        "focused": {
            "front_matter": [
                "title_page",
                "declaration",
                "abstract",
                "acknowledgements",
                "table_of_contents"
            ],
            "main_chapters": [
                "introduction",
                "background",
                "methodology",
                "results",
                "conclusion"
            ],
            "back_matter": [
                "references",
                "appendices"
            ]
        }
    }

    FORMATTING_RULES = {
        "research": {
            "margins": {
                "top": "4cm",
                "bottom": "4cm",
                "left": "4cm",
                "right": "2.5cm"
            },
            "spacing": 1.5,
            "font": {
                "main": "Times New Roman",
                "size": 12,
                "chapter_title": 14
            }
        },
        "comprehensive": {
            "margins": {
                "all": "2.5cm"
            },
            "spacing": 2.0,
            "font": {
                "main": "Times New Roman",
                "size": 12
            }
        },
        "focused": {
            "margins": {
                "all": "2.5cm"
            },
            "spacing": 1.5,
            "font": {
                "main": "Times New Roman",
                "size": 12
            }
        }
    } 