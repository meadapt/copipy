import pytest

@pytest.fixture(scope='session')
def copier_project_defaults():
    return {
            "project_name": "test_copier",
            "module_name": "test_module",
        }

def test_project_folder(copie, copier_project_defaults):
    project_defaults = copier_project_defaults
    project = copie.copy(extra_answers=project_defaults)

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project_dir.is_dir()
