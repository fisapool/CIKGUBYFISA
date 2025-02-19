class BaseUniversity:
    """Base class for university thesis templates"""
    
    def get_thesis_structure(self):
        """Default thesis structure"""
        return {
            "front_matter": [
                "title_page",
                "declaration",
                "abstract",
                "acknowledgement",
                "table_of_contents",
                "list_of_figures",
                "list_of_tables"
            ],
            "main_matter": [
                "chapter1_introduction",
                "chapter2_literature",
                "chapter3_methodology",
                "chapter4_results",
                "chapter5_conclusion"
            ],
            "back_matter": [
                "references",
                "appendices"
            ]
        } 