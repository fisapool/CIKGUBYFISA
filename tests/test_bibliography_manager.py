"""
Tests for bibliography manager
"""

import pytest
from cikgubyfisa import BibliographyManager

@pytest.fixture
def sample_reference():
    """Sample reference fixture"""
    return {
        "title": "Sample Paper Title",
        "authors": ["John Doe", "Jane Smith"],
        "year": "2023",
        "journal": "Journal of Testing",
        "volume": "1",
        "pages": "1-10"
    }

@pytest.fixture
def bib_manager():
    """Bibliography manager fixture"""
    return BibliographyManager()

def test_bibliography_manager_init():
    """Test bibliography manager initialization"""
    # Test default citation style
    bib_manager = BibliographyManager()
    assert bib_manager.citation_style == "APA7"
    assert isinstance(bib_manager.references, list)
    assert isinstance(bib_manager.citations, list)
    
    # Test valid citation style
    bib_manager = BibliographyManager(citation_style="IEEE")
    assert bib_manager.citation_style == "IEEE"
    
    # Test invalid citation style
    with pytest.raises(ValueError) as exc_info:
        BibliographyManager(citation_style="InvalidStyle")
    assert "Unsupported citation style" in str(exc_info.value)

def test_add_reference(bib_manager, sample_reference):
    """Test adding references"""
    # Test adding valid reference
    bib_manager.add_reference(sample_reference)
    assert len(bib_manager.references) == 1
    assert bib_manager.references[0] == sample_reference
    
    # Test adding reference with missing required fields
    invalid_references = [
        {"authors": ["John Doe"], "year": "2023"},  # Missing title
        {"title": "Test", "year": "2023"},  # Missing authors
        {"title": "Test", "authors": ["John Doe"]},  # Missing year
    ]
    
    for invalid_ref in invalid_references:
        with pytest.raises(ValueError) as exc_info:
            bib_manager.add_reference(invalid_ref)
        assert "Missing required field" in str(exc_info.value)

def test_add_citation(bib_manager):
    """Test adding citations"""
    # Test IEEE style citations
    bib_manager.citation_style = "IEEE"
    assert bib_manager.add_citation("ref1") == "\\cite{ref1}"
    
    # Test APA style citations
    bib_manager.citation_style = "APA7"
    assert bib_manager.add_citation("ref2") == "\\citep{ref2}"
    assert bib_manager.add_citation("ref3", page="42") == "\\citep[p.~42]{ref3}"
    
    # Verify citations are stored
    assert len(bib_manager.citations) == 3

def test_validate_references(bib_manager, sample_reference):
    """Test reference validation"""
    # Test valid reference
    bib_manager.add_reference(sample_reference)
    assert len(bib_manager.validate_references()) == 0
    
    # Test duplicate references
    bib_manager.add_reference(sample_reference)
    errors = bib_manager.validate_references()
    assert len(errors) == 1
    assert "Duplicate references found" in errors[0]
    
    # Test invalid year formats
    invalid_years = ["invalid", "0", "3000"]
    for year in invalid_years:
        invalid_ref = sample_reference.copy()
        invalid_ref["year"] = year
        bib_manager = BibliographyManager()
        bib_manager.add_reference(invalid_ref)
        errors = bib_manager.validate_references()
        assert any("Invalid year" in error for error in errors)

def test_generate_bibliography(bib_manager):
    """Test bibliography generation"""
    for style, latex_style in BibliographyManager.SUPPORTED_STYLES.items():
        bib_manager.citation_style = style
        bibliography = bib_manager.generate_bibliography()
        assert f"\\bibliographystyle{{{latex_style}}}" in bibliography
        assert "\\bibliography{references}" in bibliography

def test_supported_citation_styles():
    """Test supported citation styles"""
    bib_manager = BibliographyManager()
    assert "APA7" in bib_manager.SUPPORTED_STYLES
    assert "IEEE" in bib_manager.SUPPORTED_STYLES
    assert "ACM" in bib_manager.SUPPORTED_STYLES
    assert isinstance(bib_manager.SUPPORTED_STYLES, dict) 