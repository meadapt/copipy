from tests.conftest import project_dir

import pytest

def test_readme_creation(create_project):
    """
    Test new project creation with README.md file.
    """

    project = create_project()
    _project_dir = project_dir(project)
    project_path_structure = _project_dir[3]

    assert 'README.md' in project_path_structure

@pytest.mark.parametrize('project_name', [
    ('1Meu Lindo Projeto'),
    ('MEU LINDO PROJETO'),
    ('meu-lindo-projeto'),
    ('meu_lindo_projeto'),
    ('Python Copier COM Café'),
    ('PYTHON COPIER COM VOCÊ'),
    ('PYTHON copier com fumaça'),
    ('copier à Grega'),
    ('copier_à_Grega'),
    ('copier___à_ Grega'),
    ('copipy'),
    ('COPIPY'),
    ('Copipy'),
])
def test_readme_content(create_project, project_name):
    """
    Test new project's README.md content.
    """

    project = create_project(overrides={'project_name': project_name})
    _project_dir = project_dir(project)
    project_path = _project_dir[2]

    readme_path = project_path / 'README.md'
    readme_content = readme_path.read_text(encoding='utf-8')

    assert readme_content == f"## {project_name}\n"
