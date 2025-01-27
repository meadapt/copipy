import pytest


@pytest.fixture(scope='session')
def copier_project_defaults():
    """
    Create default answers to project creation tests.
    """

    return {
            'project_name': 'test_copier',
            'module_name': 'test_module',
            'change_project_dir_name': 'no',
        }


def project_dir(project):
    """
    Return new project dir structure (ls -la) and Path.
    """

    project_parent_dir = project.project_dir
    project_parent_dir_structure = [folder for folder in project_parent_dir.glob('*')]
    project_path = project_parent_dir_structure[0]
    project_path_structure = [file.name for file in project_path.glob('*')]

    return project_parent_dir, project_parent_dir_structure, project_path, \
        project_path_structure
