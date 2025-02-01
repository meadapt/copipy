from tests.conftest import project_dir

import pytest


def test_project_dir_creation(create_project):
    """
    Test new project creation in general.
    """
    
    project = create_project()
    _project_dir = project_dir(project)
    project_parent_dir_structure = _project_dir[1]
    project_path = _project_dir[2]

    assert project.exit_code == 0
    assert project.exception is None
    assert len(project_parent_dir_structure) == 1
    assert project_path.is_dir()
    assert project_path.stem == 'new-python-project'


@pytest.mark.parametrize('project_name, project_dir_name', [
    ('1Meu Lindo Projeto', '1meu-lindo-projeto'),
    ('MEU LINDO PROJETO', 'meu-lindo-projeto'),
    ('meu-lindo-projeto', 'meu-lindo-projeto'),
    ('meu_lindo_projeto', 'meu-lindo-projeto'),
    ('Python Copier COM Café', 'python-copier-com-cafe'),
    ('PYTHON COPIER COM VOCÊ', 'python-copier-com-voce'),
    ('PYTHON copier com fumaça', 'python-copier-com-fumaca'),
    ('copier à Grega', 'copier-a-grega'),
    ('copier_à_Grega', 'copier-a-grega'),
    ('copier___à_ Grega', 'copier-a-grega'),
    ('copipy', 'copipy'),
    ('COPIPY', 'copipy'),
    ('Copipy', 'copipy'),
])
def test_project_dir_name_slugify(create_project, project_name, project_dir_name):
    """
    Test new project directory name and the slugify process.
    The `project_dir_name` variable must contains lowercase letters, digits or hyphens.
    If the  `change_project_dir_name` is 'no' it must use the  `slugify` filter provided by the
    `cookiecutter.extensions.SlugifyExtension` Jinja extension.
    """
    project = create_project(overrides={'project_name': project_name})
    _project_dir = project_dir(project)
    project_path = _project_dir[2]

    assert project_path.stem == project_dir_name
