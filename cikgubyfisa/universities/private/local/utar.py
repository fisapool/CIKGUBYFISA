from __future__ import annotations

from typing import Dict, List


class UTARThesis:
    """Simplified UTAR thesis template."""

    THESIS_FORMAT = {
        "formatting": {
            "margins": {"left": "4cm"},
            "font": {"main": "Times New Roman"},
        }
    }

    def __init__(self, faculty: str = "engineering") -> None:
        self.faculty = faculty
        self.requirements = {
            "citation_style": "IEEE" if faculty == "engineering" else "APA7"
        }

    def get_thesis_structure(self) -> Dict[str, List[str]]:
        if self.faculty == "business":
            main = [
                "introduction",
                "literature_review",
                "theoretical_framework",
                "methodology",
                "findings",
                "conclusion",
            ]
        else:  # engineering default
            main = [
                "introduction",
                "literature_review",
                "methodology",
                "results",
                "discussion",
                "conclusion",
            ]
        return {
            "front_matter": ["abstract"],
            "main_matter": main,
            "back_matter": ["references"],
        }

    def validate_content(self, content: Dict[str, object]) -> List[str]:
        errors: List[str] = []
        abstract = content.get("abstract", "")
        if isinstance(abstract, str) and len(abstract.split()) > 300:
            errors.append("Abstract too long")
        required = [
            "introduction",
            "literature_review",
            "methodology",
            "conclusion",
            "references",
        ]
        for section in required:
            if section not in content:
                errors.append(f"Missing required section: {section}")
        refs = content.get("references", [])
        if isinstance(refs, list) and len(refs) < 30:
            errors.append("Minimum 30 references required")
        return errors
