from __future__ import annotations

from typing import Dict, List


class APUThesis:
    """Simplified APU thesis template."""

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
            "front_matter": [],
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
        errors: List[str] = []
        if "plagiarism_report" not in content:
            errors.append("Turnitin plagiarism report is required")
        page_count = content.get("page_count")
        if isinstance(page_count, int) and page_count < 75:
            errors.append("Thesis must be at least 75 pages")
        return errors
