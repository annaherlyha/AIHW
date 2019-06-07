import pytest
from app.model.input_model_from_config import InputModelFromConfig
from app.service.url_provider import UrlProvider
from app.controller.process_flow import ProcessFlow


@pytest.fixture()
def checkConfig():
    CheckConfig = InputModelFromConfig()
    return CheckConfig


def test_server_url(checkConfig):
    checkConfig.config_file == 'Configurations.ini'


def test_base_url(checkConfig):
    checkConfig.base_url == 'https://www.aihw.gov.au/reports-data/health-welfare-services/homelessness-services/data'


def test_base_dir(checkConfig):
    checkConfig.base_dir


def test_temp_dir(checkConfig):
    checkConfig.temp_dir


def test_work_dir(checkConfig):
    checkConfig.work_dir


def test_output_dir(checkConfig):
    checkConfig.output_dir


def test_file_name(checkConfig):
    checkConfig.file_name == 'Data tables: Historical tables'


def test_output_file(checkConfig):
    checkConfig.output_file


def test_get_download_link(checkConfig):
    processor = ProcessFlow(config_model=checkConfig)
    assert processor._get_link() == 'https://www.aihw.gov.au/getmedia/5e16ec41-9bfa-4a33-bffa-9081a759cd9b/aihw-hou-299-historical.xlsx.aspx'


def test_download_file(checkConfig):
    processor = ProcessFlow(config_model=checkConfig)
    assert processor.download_file()
