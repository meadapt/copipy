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
