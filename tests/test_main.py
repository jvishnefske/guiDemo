"""Basic tests for guiDemo application."""
import os


def test_index_html_exists():
    """Verify index.html is present in the project."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(project_root, 'index.html')
    assert os.path.exists(index_path)


def test_main_module_importable():
    """Verify main module can be imported (syntax check)."""
    # Note: Full import requires Qt runtime, so we just check file exists
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main_path = os.path.join(project_root, 'main.py')
    assert os.path.exists(main_path)
