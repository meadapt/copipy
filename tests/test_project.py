from pathlib import Path
import pytest

@pytest.fixture(scope='session')
def copier_project_defaults():
    return {
            "project_name": "test_copier",
            "module_name": "test_module",
        }

def test_project_folder_creation(copie, copier_project_defaults):
    project_defaults = copier_project_defaults
    project = copie.copy(extra_answers=project_defaults)
    project_folders = [folder for folder in project.project_dir.glob('*')]
    project_path = project_folders[0]

    assert project.exit_code == 0
    assert project.exception is None
    assert len(project_folders) == 1
    assert project_path.is_dir()
    assert project_path.stem == project.answers['project_name']
