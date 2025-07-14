from __future__ import annotations

from typing import Dict, List


class INTIThesis:
    """Simplified INTI thesis template."""

    THESIS_FORMAT = {
        "formatting": {
            "margins": {"left": "4cm"},
            "font": {"main": "Times New Roman"},
        }
    }

    def __init__(self, faculty: str = "computing") -> None:
        self.faculty = faculty
        self.requirements = {"citation_style": "ACM"}

    def get_thesis_structure(self) -> Dict[str, List[str]]:
        return {
            "front_matter": ["supervisor_approval", "copyright_notice"],
            "main_matter": [
                "introduction",
                "system_design",
                "implementation",
                "testing",
                "conclusion",
            ],
            "back_matter": ["references"],
        }

    def validate_content(self, content: Dict[str, object]) -> List[str]:
        return []
