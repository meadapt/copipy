from tests.conftest import project_dir

import pytest

@pytest.mark.parametrize('project_name, project_scripts_dir_name', [
    ('New Python project', 'new_python_project'),
    ('1Meu Lindo Projeto', 'meu_lindo_projeto'),
    ('MEU LINDO PROJETO', 'meu_lindo_projeto'),
    ('meu-lindo-projeto', 'meu_lindo_projeto'),
    ('meu_lindo_projeto', 'meu_lindo_projeto'),
    ('Python Copier COM Café', 'python_copier_com_cafe'),
    ('PYTHON COPIER COM VOCÊ', 'python_copier_com_voce'),
    ('PYTHON copier com fumaça', 'python_copier_com_fumaca'),
    ('copier à Grega', 'copier_a_grega'),
    ('copier_à_Grega', 'copier_a_grega'),
    ('copier___à_ Grega', 'copier_a_grega'),
    ('copipy', 'copipy'),
    ('COPIPY', 'copipy'),
    ('Copipy', 'copipy'),
])
def test_project_scripts_dir_creation(create_project, project_name, project_scripts_dir_name):
    """
    Test new project structure and the slugify process.
    The `project_scripts_dir_name` variable must contains lowercase letters, digits or underscore.
    If the  `change_project_scripts_dir_name` is 'no' it must use the  `slugify` filter provided by the
    `cookiecutter.extensions.SlugifyExtension` Jinja extension and underscore not hyphen.
    If the  `change_project_scripts_dir_name` is 'yes',
    it could be one of the `common_scripts_dir_name` suggested or created by the user.
    """

    project = create_project(overrides={'project_name': project_name})
    _project_dir = project_dir(project)
    project_path_structure = _project_dir[3]

    assert project_scripts_dir_name in project_path_structure
