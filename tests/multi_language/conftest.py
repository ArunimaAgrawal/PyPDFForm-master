# -*- coding: utf-8 -*-

import os

import pytest


@pytest.fixture
def multi_language_pdf_samples():
    return os.path.join(
        os.path.dirname(__file__), "..", "..", "pdf_samples", "multi_language"
    )


@pytest.fixture
def zh_cn(multi_language_pdf_samples):
    return os.path.join(multi_language_pdf_samples, "zh_cn")


@pytest.fixture
def ko(multi_language_pdf_samples):
    return os.path.join(multi_language_pdf_samples, "ko")
