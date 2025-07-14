from __future__ import annotations

from typing import Dict, List, Optional


class BibliographyManager:
    """Simple bibliography manager supporting a few citation styles."""

    SUPPORTED_STYLES: Dict[str, str] = {
        "APA7": "apalike",
        "IEEE": "ieeetr",
        "ACM": "acm",
    }

    def __init__(self, citation_style: str = "APA7") -> None:
        if citation_style not in self.SUPPORTED_STYLES:
            raise ValueError(f"Unsupported citation style: {citation_style}")
        self.citation_style = citation_style
        self.references: List[Dict[str, str]] = []
        self.citations: List[str] = []

    def add_reference(self, reference: Dict[str, str]) -> None:
        required = ["title", "authors", "year"]
        for key in required:
            if key not in reference:
                raise ValueError("Missing required field")
        self.references.append(reference)

    def add_citation(self, key: str, *, page: Optional[str] = None) -> str:
        if self.citation_style == "IEEE":
            cite = f"\\cite{{{key}}}"
        else:
            if page:
                cite = f"\\citep[p.~{page}]{{{key}}}"
            else:
                cite = f"\\citep{{{key}}}"
        self.citations.append(cite)
        return cite

    def validate_references(self) -> List[str]:
        errors: List[str] = []
        seen = set()
        for ref in self.references:
            year = ref.get("year", "")
            if not year.isdigit() or not (1000 <= int(year) <= 2100):
                errors.append(f"Invalid year: {year}")
            key = (ref.get("title"), tuple(ref.get("authors", [])), year)
            if key in seen:
                if "Duplicate references found" not in errors:
                    errors.append("Duplicate references found")
            else:
                seen.add(key)
        return errors

    def generate_bibliography(self) -> str:
        style = self.SUPPORTED_STYLES[self.citation_style]
        return f"\\bibliographystyle{{{style}}}\n\\bibliography{{references}}"
