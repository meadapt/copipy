import pytest


def project_dir(project):
    """
    Return new project dir structure (ls -la) and Path.
    """

    project_dir_structure = [folder for folder in project.project_dir.glob('*')]
    project_dir_path = project_dir_structure[0]
    return project_dir_structure, project_dir_path


def test_project_dir_creation(copie, copier_project_defaults):
    """
    Test new project creation in general.
    """
    project_defaults = copier_project_defaults
    project = copie.copy(extra_answers=project_defaults)
    project_dir_path = project_dir(project)

    assert project.exit_code == 0
    assert project.exception is None
    assert len(project_dir_path[0]) == 1
    assert project_dir_path[1].is_dir()
    assert project_dir_path[1].stem == 'test-copier'


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
def test_project_dir_name_slugify(copie,
                          copier_project_defaults, project_name, project_dir_name):
    """
    Test new project directory name and the slugify process.
    The `project_dir_name` variable must contains lowercase letters, digits or hyphens.
    If the  `change_project_dir_name` is 'no' it must use the  `slugify` filter provided by the
    `cookiecutter.extensions.SlugifyExtension` Jinja extension.
    """
    copier_project_defaults['project_name'] = project_name
    project_defaults = copier_project_defaults
    project = copie.copy(extra_answers=project_defaults)
    project_dir_path = project_dir(project)

    assert project_dir_path[1].stem == project_dir_name
