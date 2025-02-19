"""
Tests for university thesis templates
"""

import pytest
from cikgubyfisa.universities.private.local.utar import UTARThesis
from cikgubyfisa.universities.private.local.inti import INTIThesis
from cikgubyfisa.universities.private.local.apu import APUThesis

def test_utar_thesis_structure():
    """Test UTAR thesis structure for different faculties"""
    # Engineering faculty
    eng_thesis = UTARThesis(faculty="engineering")
    eng_structure = eng_thesis.get_thesis_structure()
    
    assert "introduction" in eng_structure["main_matter"]
    assert "methodology" in eng_structure["main_matter"]
    assert eng_thesis.requirements["citation_style"] == "IEEE"
    
    # Business faculty
    bus_thesis = UTARThesis(faculty="business")
    bus_structure = bus_thesis.get_thesis_structure()
    
    assert "theoretical_framework" in bus_structure["main_matter"]
    assert "findings" in bus_structure["main_matter"]
    assert bus_thesis.requirements["citation_style"] == "APA7"

def test_utar_content_validation():
    """Test UTAR thesis content validation"""
    thesis = UTARThesis(faculty="engineering")
    
    # Test with valid content
    valid_content = {
        "abstract": "Valid abstract " * 50,  # 100 words
        "introduction": "Chapter 1",
        "literature_review": "Chapter 2",
        "methodology": "Chapter 3",
        "results": "Chapter 4",
        "discussion": "Chapter 5",
        "conclusion": "Chapter 6",
        "references": ["ref1", "ref2"] * 15,  # 30 references
        "citations": ["citation1", "citation2"]
    }
    
    errors = thesis.validate_content(valid_content)
    assert len(errors) == 0
    
    # Test with invalid content
    invalid_content = {
        "abstract": "Too long abstract " * 200,  # 400 words
        "introduction": "Chapter 1",
        # Missing required chapters
        "references": ["ref1", "ref2"],  # Too few references
        "citations": ["invalid_citation"]
    }
    
    errors = thesis.validate_content(invalid_content)
    assert len(errors) > 0
    assert any("Abstract too long" in error for error in errors)
    assert any("Missing required section" in error for error in errors)
    assert any("Minimum 30 references required" in error for error in errors)

def test_inti_thesis_structure():
    """Test INTI thesis structure for computing faculty"""
    thesis = INTIThesis(faculty="computing")
    structure = thesis.get_thesis_structure()
    
    assert "system_design" in structure["main_matter"]
    assert "implementation" in structure["main_matter"]
    assert thesis.requirements["citation_style"] == "ACM"
    
    # Check front matter requirements
    assert "supervisor_approval" in structure["front_matter"]
    assert "copyright_notice" in structure["front_matter"]

def test_apu_thesis_validation():
    """Test APU thesis content validation"""
    thesis = APUThesis(faculty="computing")
    
    # Test with missing plagiarism report
    content = {
        "abstract": "Valid abstract " * 50,
        "introduction": "Chapter 1",
        "literature_review": "Chapter 2",
        "methodology": "Chapter 3",
        "system_design": "Chapter 4",
        "implementation": "Chapter 5",
        "testing": "Chapter 6",
        "conclusion": "Chapter 7",
        "page_count": 80
    }
    
    errors = thesis.validate_content(content)
    assert any("Turnitin plagiarism report is required" in error for error in errors)
    
    # Test with insufficient page count
    content["plagiarism_report"] = "report.pdf"
    content["page_count"] = 50
    
    errors = thesis.validate_content(content)
    assert any("must be at least 75 pages" in error for error in errors)

@pytest.fixture
def sample_thesis_content():
    """Fixture for sample thesis content"""
    return {
        "title": "Sample Thesis",
        "author": "John Doe",
        "student_id": "12345",
        "abstract": "Sample abstract " * 50,
        "keywords": "keyword1, keyword2, keyword3",
        "introduction": "Chapter 1 content",
        "literature_review": "Chapter 2 content",
        "methodology": "Chapter 3 content",
        "results": "Chapter 4 content",
        "discussion": "Chapter 5 content",
        "conclusion": "Chapter 6 content",
        "references": ["ref1", "ref2"] * 20,
        "page_count": 100
    }

def test_thesis_formatting(sample_thesis_content):
    """Test thesis formatting across different universities"""
    universities = [
        UTARThesis(faculty="engineering"),
        INTIThesis(faculty="computing"),
        APUThesis(faculty="computing")
    ]
    
    for uni_thesis in universities:
        # Check basic formatting requirements
        assert uni_thesis.THESIS_FORMAT["formatting"]["margins"]["left"] == "4cm"
        assert "font" in uni_thesis.THESIS_FORMAT["formatting"]
        
        # Validate content
        errors = uni_thesis.validate_content(sample_thesis_content)
        print(f"Validation errors for {uni_thesis.__class__.__name__}: {errors}") 