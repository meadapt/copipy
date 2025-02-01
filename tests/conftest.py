import pytest


@pytest.fixture(scope='session')
def copier_project_defaults():
    """
    Create default answers to project creation tests.
    """

    return {
            'project_name': 'New Python project',
            'keep_project_dir_name': 'yes',
            'keep_project_scripts_dir_name': 'yes',
        }


@pytest.fixture
def create_project(copie, copier_project_defaults):
    """
    Fixture to create a project using the copier tool.
    """
    def _create_project(overrides=None):
        # Allow overriding defaults
        answers = {**copier_project_defaults, **(overrides or {})}
        return copie.copy(extra_answers=answers)

    return _create_project


def project_dir(project):
    """
    Return new project dir structure (ls -la) and Path.
    """

    project_parent_dir = project.project_dir
    project_parent_dir_structure = [folder for folder in project_parent_dir.glob('*')]
    project_path = project_parent_dir_structure[0]
    project_path_structure = [file.name.split('\n')[0] for file in project_path.glob('*')]

    return project_parent_dir, project_parent_dir_structure, project_path, \
        project_path_structure
